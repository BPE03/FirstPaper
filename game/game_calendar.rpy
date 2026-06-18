# Date and time variables
default current_day = 13
default current_month = 12
default current_year = 2025
default current_hour = 9
default current_minute = 0
default delay = 1/30
default time_of_day_state = "morning"

# Calendar display variables
default display_month = current_month
default display_year = current_year

# Calendar event data
default calendar_events = {
    "proposal_deadline": {
        "day": 9,
        "month": 1,
        "year": 2026,
        "title": "Deadline Pengumpulan Proposal",
        "description": "Batas akhir untuk mengumpulkan proposal penelitian tesis. Pastikan proposal sudah lengkap dan disetujui oleh dosen pembimbing sebelum tanggal ini."
    },
    "skripsi_deadline": {
        "day": 22,
        "month": 6,
        "year": 2026,
        "title": "Deadline Pengumpulan Skripsi",
        "description": "Batas akhir untuk mengumpulkan skripsi penelitian tesis. Pastikan skripsi sudah lengkap sebelum tanggal ini."
    }
}
default selected_calendar_event = None
default show_event_details = False

# Date and time related functions
init python:
    import datetime
    month_names = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
        5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
        9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    
    def get_days_in_month(month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        else:  # February
            if year % 4 == 0:
                return 29
            return 28
    
    def advance_time(minutes):
        global current_minute, current_hour, current_day, current_month, current_year
        
        current_minute += minutes
        
        # Handle minute overflow
        if current_minute >= 60:
            current_hour += current_minute // 60
            current_minute = current_minute % 60
        
        # Handle hour overflow
        if current_hour >= 24:
            current_day += current_hour // 24
            current_hour = current_hour % 24
        
        # Handle day overflow
        days_in_month = get_days_in_month(current_month, current_year)
        if current_day > days_in_month:
            current_day = 1
            current_month += 1
        
        # Handle month overflow
        if current_month > 12:
            current_month = 1
            current_year += 1

        tod_fsm_step()

        _dl = store.calendar_events.get("proposal_deadline")
        if _dl and (current_year, current_month, current_day) >= (_dl["year"], _dl["month"], _dl["day"]) and \
        store.thesis_fsm_state not in ("post_sempro", "writing", "done"):
            store.interrupted = True
            store.pending_jump = "sempro"
            set_cutscene_mode(True)

        _dl = store.calendar_events.get("skripsi_deadline")
        if _dl and (current_year, current_month, current_day) >= (_dl["year"], _dl["month"], _dl["day"]):
            store.interrupted = True
            store.pending_jump = "sidang_akhir"
            set_cutscene_mode(True)

    def get_total_game_minutes():
        """Returns total elapsed game-minutes from a fixed reference (2025-01-01)."""
        global current_year, current_month, current_day, current_hour, current_minute
        days = (current_year - 2025) * 365 + (current_month - 1) * 30 + current_day
        return days * 1440 + current_hour * 60 + current_minute

    def format_time():
        return "{:02d}:{:02d}".format(current_hour, current_minute)

    def get_calendar_events(day, month, year):
        return [e for e in calendar_events.values() if e["day"] == day and e["month"] == month and e["year"] == year]

    def get_next_calendar_event():
        today = datetime.date(current_year, current_month, current_day)
        future_events = [e for e in calendar_events.values() if datetime.date(e["year"], e["month"], e["day"]) >= today]
        if not future_events:
            return None
        return sorted(future_events, key=lambda e: (e["year"], e["month"], e["day"]))[0]

    def set_selected_calendar_event(event):
        global selected_calendar_event, show_event_details
        selected_calendar_event = event
        show_event_details = True

    def next_display_month():
        global display_month, display_year
        display_month += 1
        if display_month > 12:
            display_month = 1
            display_year += 1

    def prev_display_month():
        global display_month, display_year
        display_month -= 1
        if display_month < 1:
            display_month = 12
            display_year -= 1

    def get_tomorrow():
        today = datetime.date(current_year, current_month, current_day)
        tomorrow = today + datetime.timedelta(days=1)
        return tomorrow.day, tomorrow.month, tomorrow.year

    def add_calendar_event(event_id, day, month, year, title, description, avoid_duplicates=True):
        global calendar_events
        if avoid_duplicates and event_id in calendar_events:
            return False
        calendar_events[event_id] = {"day": day, "month": month, "year": year, "title": title, "description": description}
        renpy.retain_after_load()
        return True

init python:
    # ── Appointment FSM states ────────────────────────────────────────
    APPT_UNSCHEDULED = "unscheduled"
    APPT_SCHEDULED   = "scheduled"

    APPT_HOUR = {
        "bimbingan": 10,
        "workshop":  10,
    }

    _APPT_CALENDAR_TITLE = {
        "bimbingan": "Bimbingan dengan Dosen",
        "workshop":  "Workshop",
    }

    _APPT_CALENDAR_DESC = {
        "bimbingan": "Bimbingan dijadwalkan jam 10:00.",
        "workshop":  "Workshop dijadwalkan jam 10:00.",
    }

    def appt_is_booked(name):
        return getattr(store, "appt_{}_state".format(name)) == APPT_SCHEDULED

    def appt_book(name):
        """Schedule appointment for tomorrow at APPT_HOUR[name] and add a calendar event."""
        day, month, year = get_tomorrow()
        appt_id = "{}_{}_{}_{}".format(name, year, month, day)  # Unique ID based on name and date
        setattr(store, "appt_{}_day".format(name),   day)
        setattr(store, "appt_{}_month".format(name), month)
        setattr(store, "appt_{}_year".format(name),  year)
        setattr(store, "appt_{}_state".format(name), APPT_SCHEDULED)
        add_calendar_event(appt_id, day, month, year, _APPT_CALENDAR_TITLE[name], _APPT_CALENDAR_DESC[name], avoid_duplicates=False)

    def appt_get_time_diff(name):
        """Returns minutes elapsed since scheduled time. Negative means player arrived early."""
        day   = getattr(store, "appt_{}_day".format(name))
        month = getattr(store, "appt_{}_month".format(name))
        year  = getattr(store, "appt_{}_year".format(name))
        sched_days    = (year - 2025) * 365 + (month - 1) * 30 + day
        sched_minutes = sched_days * 1440 + APPT_HOUR[name] * 60
        return get_total_game_minutes() - sched_minutes

    def appt_dismiss(name):
        """Cancel or complete the appointment, resetting it to UNSCHEDULED."""
        setattr(store, "appt_{}_state".format(name), APPT_UNSCHEDULED)

init python:
    # ── Time-of-Day FSM states ────────────────────────────────────────
    TOD_MORNING   = "morning"    # 06:00 – 14:59
    TOD_AFTERNOON = "afternoon"  # 15:00 – 17:59
    TOD_NIGHT     = "night"      # 18:00 – 05:59

    TOD_MUSIC = {
        TOD_MORNING:   "daytime.mp3",
        TOD_AFTERNOON: None,
        TOD_NIGHT:     "nighttime.mp3",
    }

    def _tod_from_hour(hour):
        if 6 <= hour < 15:
            return TOD_MORNING
        elif 15 <= hour < 18:
            return TOD_AFTERNOON
        else:
            return TOD_NIGHT

    def tod_fsm_step():
        """Sync time_of_day_state with current_hour. Called from advance_time()."""
        global time_of_day_state
        new_state = _tod_from_hour(current_hour)
        if new_state != time_of_day_state:
            time_of_day_state = new_state
            fade_music_transition(TOD_MUSIC[new_state], fade_out=2.0, fade_in=1.0)
            renpy.scene() # Clears the current scene
            cg = current_location + "_" + new_state
            renpy.show(cg)
            renpy.transition(dissolve)
            if time_stop:
                renpy.pause(1.0)