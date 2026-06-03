# Date and time variables
default current_day = 13
default current_month = 12
default current_year = 2025
default current_hour = 9
default current_minute = 0
default delay = 1/30

# Calendar display variables
default display_month = current_month
default display_year = current_year

# Calendar event data
default calendar_events = [
    {
        "day": 9,
        "month": 1,
        "year": 2026,
        "title": "Deadline Pengumpulan Proposal",
        "description": "Batas akhir untuk mengumpulkan proposal penelitian tesis. Pastikan proposal sudah lengkap dan disetujui oleh dosen pembimbing sebelum tanggal ini."
    }
]
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

    def get_total_game_minutes():
        """Returns total elapsed game-minutes from a fixed reference (2025-01-01)."""
        global current_year, current_month, current_day, current_hour, current_minute
        days = (current_year - 2025) * 365 + (current_month - 1) * 30 + current_day
        return days * 1440 + current_hour * 60 + current_minute

    def format_time():
        return "{:02d}:{:02d}".format(current_hour, current_minute)

    def get_calendar_events(day, month, year):
        return [event for event in calendar_events if event["day"] == day and event["month"] == month and event["year"] == year]

    def get_next_calendar_event():
        today = datetime.date(current_year, current_month, current_day)
        future_events = [event for event in calendar_events if datetime.date(event["year"], event["month"], event["day"]) >= today]
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

    def add_calendar_event(day, month, year, title, description, avoid_duplicates=True):
        """
        Append a new event to the calendar.
        
        Args:
            day (int): Day of the month (1-31)
            month (int): Month (1-12)
            year (int): Year
            title (str): Event title
            description (str): Event description
            avoid_duplicates (bool): If True, won't add duplicate events on same date with same title
        
        Returns:
            bool: True if event was added, False if it was a duplicate and skipped
        
        Example:
            add_calendar_event(20, 5, 2026, "Advisor Meeting", "Discuss thesis progress.")
        """
        global calendar_events
        event = {"day": day, "month": month, "year": year, "title": title, "description": description}
        
        if avoid_duplicates:
            for e in calendar_events:
                if (e["day"] == day and e["month"] == month and e["year"] == year and e["title"] == title):
                    return False  # Duplicate found, skip
        
        calendar_events.append(event)
        renpy.retain_after_load()
        return True