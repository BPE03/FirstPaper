# Variable to track if detailed stats window is shown
default show_detailed_stats = False
# Variable to track if calendar window is shown
default show_calendar = False
default show_map = False

# Main stats display (always visible)
screen main_stats():
    showif not in_cutscene:  # Hide during cutscenes, show during interactive gameplay
        frame:
            xalign 0.05
            yalign 0.05
            xsize 280
            ysize 660
            background "#2c3e50cc"
            padding (15, 15)
            
            vbox:
                spacing 15
                
                text "Kerjakan Skripsimu❤" size 24 color "#ecf0f1" bold True
                
                # Current emotion display
                $ current_emotion = get_current_emotion()
                $ emotion_info = get_emotion_info(current_emotion)
                
                # Motivation stat
                text "Motivasi" size 18 color "#ffffff"
                bar:
                    value motivation
                    range max_stat
                    xsize 250
                    ysize 22
                    left_bar "#e74c3c"
                    right_bar "#34495e"
                text "[motivation:.02f]/[max_stat]" size 14 color "#bdc3c7"
                
                # Thesis Progress
                text "Kemajuan Skripsi" size 18 color "#ffffff"
                bar:
                    value thesis_progress
                    range max_stat
                    xsize 250
                    ysize 22
                    left_bar "#2ecc71"
                    right_bar "#34495e"
                text "[thesis_progress:.02f]%" size 14 color "#bdc3c7"

                if bimbingan_bonus_active:
                    $ _bonus_remaining = max(0.0, 10.0 - (thesis_progress - bimbingan_bonus_start_progress))
                    frame:
                        xsize 250
                        background "#27ae6099"
                        padding (8, 6)
                        vbox:
                            spacing 2
                            text "Bonus Bimbingan Aktif" size 12 color "#2ecc71" bold True
                            text "Sisa [_bonus_remaining:.1f]% progress" size 11 color "#a9dfbf"

                frame:
                    xsize 250
                    ysize 50
                    background emotion_info["color"]
                    padding (10, 10)
                    
                    vbox:
                        spacing 3
                        text "Emosi" size 12 color "#ffffff"
                        text "[current_emotion.upper()]" size 16 color "#ffffff" bold True
                        #text "[emotion_info['description']]" size 11 color "#ffffff"
        
                null height 1
                # Alertness display
                $ _aw_label, _aw_color = {
                    "sleeping":  ("Tidur",     "#687279"),
                    "peak":      ("Puncak",    "#2ecc71"),
                    "normal":    ("Normal",    "#3498db"),
                    "fatigued":  ("Lelah",     "#f39c12"),
                    "exhausted": ("Kelelahan", "#e67e22"),
                    "crashed":   ("Ambruk",   "#e74c3c"),
                }.get(sleep_get_state(), ("Normal", "#3498db"))
                frame:
                    xsize 250
                    ysize 40
                    background "#2c3e50"
                    padding (10, 8)
                    hbox:
                        spacing 8
                        text "Kesadaran:" size 13 color "#bdc3c7" yalign 0.5
                        text "[_aw_label]" size 14 color _aw_color bold True yalign 0.5

                null height 1
                # Score display
                text "Skor" size 18 color "#ffffff"
                text "[int(score)]" size 18 color "#f39c12" bold True

                #null height 5
                # Button to show detailed stats
                textbutton "Lihat Statistik Detil" action ToggleVariable("show_detailed_stats") xsize 250 ysize 75
        
        # Timer that affects stats every second
        if not time_stop:
            timer 1.0 repeat True action [
                Function(decrease_stats, 1), 
            ]

screen calendar_now():
    showif not in_cutscene:  # Hide during cutscenes, show during interactive gameplay
        frame:
            xalign 0.95
            yalign 0.05
            xsize 280
            ysize 160
            background "#2c3e50cc"
            padding (15, 15)
            
            vbox:
                spacing 15
                
                text "[current_day]/[current_month]/[current_year]" size 28 color "#ffffff"
                text "[format_time()]" size 28 color "#ffffff"
                textbutton "{size=24}Lihat Kalender" action ToggleVariable("show_calendar")
        # Timer that affects stats every second
        if not time_stop:
            timer 1.0 repeat True action [
                Function(advance_time, 1)
            ]

screen game_maps():
    # zorder 2
    # modal True
    showif show_map:
        frame:
            background "#000000aa"
            xfill True
            yfill True
            frame:
                xalign 0.5 yalign 0.5
                xsize 600
                ysize 800
                padding (20, 20)
                
                vbox:
                    text "Tempat yang Dapat Dikunjungi" xalign 0.5 size 30
                    null height 30
                    
                    for dest in locations[current_location]["explorable"]:
                        $ loc_name = locations[dest]["name"]
                        textbutton "[loc_name]" action Function(move_to_map, dest)
                    
                    null height 30
                    textbutton "Tutup Map":
                        action ToggleVariable("show_map")
                        xalign 0.5

# Calendar window
screen calendar_window():
    showif show_calendar:
        # Modal background
        frame:
            background "#000000aa"
            xfill True
            yfill True
            
            # Calendar window
            frame:
                xalign 0.5
                yalign 0.05
                xsize 600
                ysize 640
                background "#34495e"
                padding (25, 25)
                
                vbox:
                    spacing 15
                    
                    hbox:
                        textbutton "✕ Tutup":
                            action [SetVariable("show_calendar", False), SetVariable("show_event_details", False)]
                            text_size 20
                            #xalign 0.95
                    
                    null height 1
                    
                    hbox:
                        xfill True
                        textbutton "Prev":
                            action Function(prev_display_month)
                            text_size 20
                        text "Kalender - [month_names[display_month]] [display_year]" size 25 color "#ecf0f1" bold True xalign 0.5
                        textbutton "Next":
                            action Function(next_display_month)
                            text_size 20
                            xpos 1.0
                            xanchor 1.0
                    # Current date and time display
                    frame:
                        background "#2c3e50"
                        padding (15, 15)
                        xsize 550
                        
                        vbox:
                            spacing 5
                            text "Tanggal & Waktu Saat Ini" size 18 color "#3498db" bold True
                            text "[month_names[current_month]] [current_day], [current_year]" size 22 color "#ffffff"
                            text "{:02d}:{:02d}".format(current_hour, current_minute) size 32 color "#2ecc71" bold True
                    
                    null height 10
                    
                    # Day of week headers
                    hbox:
                        spacing 46
                        for day_name in ["Min", "Sen", "Sel", "Rab", "Kam", "Jum", "Sab"]:
                            text day_name size 16 color "#ecf0f1" bold True xsize 75 text_align 0.5
                    
                    # Calendar grid
                    python:
                        days_in_month = get_days_in_month(display_month, display_year)
                        # Calculate first day of month (simplified - starts on Sunday for demo)
                        first_day = datetime.date(display_year, display_month, 1).weekday()
                        first_day = (first_day + 1) % 7  # Adjust so Sunday = 0
                    
                    # Calendar days
                    vbox:
                        spacing 5
                        for week in range(6):  # Maximum 6 weeks in a month
                            hbox:
                                spacing 5
                                for day_of_week in range(7):
                                    $ day_number = week * 7 + day_of_week - first_day + 1
                                    $ day_events = get_calendar_events(day_number, display_month, display_year)
                                    $ has_event = len(day_events) > 0
                                    if day_number > 0 and day_number <= days_in_month:
                                        if day_number == current_day and display_month == current_month and display_year == current_year:
                                            # Highlight current day
                                            frame:
                                                background "#2ecc72"
                                                xsize 75
                                                ysize 50
                                                padding (5, 5)
                                                text "[day_number]" size 18 color "#ffffff" bold True xalign 0.5 yalign 0.5
                                        elif has_event:
                                            frame:
                                                background "#e67e22"
                                                xsize 75
                                                ysize 50
                                                padding (5, 5)
                                                textbutton "[day_number]":
                                                    text_style "my_textbutton_text"
                                                    xalign 0.5 yalign 0.5
                                                    action Function(set_selected_calendar_event, day_events[0]) 
                                        else:
                                            frame:
                                                background "#7f8c8d"
                                                xsize 75
                                                ysize 50
                                                padding (5, 5)
                                                text "[day_number]" size 18 color "#ecf0f1" xalign 0.5 yalign 0.5
                                    else:
                                        # Empty day slot
                                        frame:
                                            background None
                                            xsize 75
                                            ysize 50

                    #null height 1

                    # Event details section
                    $ next_event = get_next_calendar_event()
                    if next_event is not None:
                        frame:
                            background "#2c3e50"
                            xsize 550
                            padding (10, 10)
                            vbox:
                                spacing 5
                                text "Acara Mendatang" size 18 color "#3498db" bold True
                                textbutton "[next_event['title']] – [month_names[next_event['month']]] [next_event['day']]" action Function(set_selected_calendar_event, next_event) xalign 0.0 text_size 18
                                text "Klik tanggal yang disorot pada kalender untuk melihat detail acara." size 14 color "#bdc3c7"
                    else:
                        frame:
                            background "#2c3e50"
                            xsize 550
                            padding (10, 10)
                            vbox:
                                spacing 5
                                text "Tidak ada acara yang akan datang" size 18 color "#3498db" bold True
                                text "Saat ini tidak ada acara yang dijadwalkan pada kalender." size 16 color "#ecf0f1"

                    if show_event_details and selected_calendar_event is not None:
                        frame:
                            background "#1a252f"
                            xsize 550
                            padding (15, 15)
                            vbox:
                                spacing 8
                                text "[selected_calendar_event['title']]" size 22 color "#ecf0f1" bold True
                                text "Tanggal: [month_names[selected_calendar_event['month']]] [selected_calendar_event['day']], [selected_calendar_event['year']]" size 16 color "#ffffff"
                                text "[selected_calendar_event['description']]" size 16 color "#bdc3c7" text_align 0.0
                                null height 8
                                textbutton "Tutup Detail Acara" action [SetVariable("show_event_details", False), SetVariable("selected_calendar_event", None)] xalign 0.0 text_size 18

# Detailed stats window (shown when button is pressed)
screen detailed_stats_window():
    showif show_detailed_stats:
        # Modal background
        frame:
            background "#000000aa"
            xfill True
            yfill True
            
            # Stats window
            frame:
                xalign 0.5
                yalign 0.2
                xsize 700
                ysize 650
                background "#34495e"
                padding (25, 25)
                
                vbox:
                    spacing 10
                    
                    hbox:
                        spacing 400
                        text "Detil Statistik" size 28 color "#ecf0f1" bold True
                        textbutton "✕ Tutup" action SetVariable("show_detailed_stats", False) text_size 20
                    
                    null height 10
                    
                    # Psychological Needs
                    text "Kebutuhan Psikologis" size 22 color "#3498db" bold True
                    
                    hbox:
                        spacing 20
                        vbox:
                            spacing 5
                            text "Otonomi" size 16 color "#ffffff"
                            bar value autonomy range max_stat xsize 200 ysize 18 left_bar "#9b59b6" right_bar "#2c3e50"
                            text "[autonomy:.02f]/[max_stat]" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            text "Kompetensi" size 16 color "#ffffff"
                            bar value competence range max_stat xsize 200 ysize 18 left_bar "#3498db" right_bar "#2c3e50"
                            text "[competence:.02f]/[max_stat]" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            text "Keterhubungan" size 16 color "#ffffff"
                            bar value relatedness range max_stat xsize 200 ysize 18 left_bar "#1abc9c" right_bar "#2c3e50"
                            text "[relatedness:.02f]/[max_stat]" size 14 color "#bdc3c7"
                    
                    null height 15
                    
                    # Physical Wellbeing
                    text "Kesehatan Fisik" size 22 color "#e67e22" bold True
                    
                    hbox:
                        spacing 20
                        vbox:
                            spacing 5
                            text "Nutrisi" size 16 color "#ffffff"
                            bar value nutrition range max_stat xsize 200 ysize 18 left_bar "#f39c12" right_bar "#2c3e50"
                            text "[nutrition:.02f]/[max_stat]" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            text "Aktivitas Fisik" size 16 color "#ffffff"
                            bar value physical_activity range max_stat xsize 200 ysize 18 left_bar "#e74c3c" right_bar "#2c3e50"
                            text "[physical_activity:.02f]/[max_stat]" size 14 color "#bdc3c7"
                            
                        vbox:
                            spacing 5
                            text "Tidur" size 16 color "#ffffff"
                            bar value sleep range max_stat xsize 200 ysize 18 left_bar "#687279" right_bar "#2c3e50"
                            text "[sleep:.02f]/[max_stat]" size 14 color "#bdc3c7"
                            $ _alertness_label = {
                                "sleeping":  ("Tidur",     "#687279"),
                                "peak":      ("Puncak",    "#2ecc71"),
                                "normal":    ("Normal",    "#3498db"),
                                "fatigued":  ("Lelah",     "#f39c12"),
                                "exhausted": ("Kelelahan", "#e67e22"),
                                "crashed":   ("Ambruk",   "#e74c3c"),
                            }.get(sleep_get_state(), ("Normal", "#3498db"))
                            text "Kesadaran: [_alertness_label[0]]" size 13 color _alertness_label[1] bold True
                    
                    null height 15
                    
                    # Emotional State
                    text "Status Emosional" size 22 color "#e91e63" bold True
                    
                    hbox:
                        spacing 20
                        vbox:
                            spacing 5
                            text "Valence (Kesenangan)" size 16 color "#ffffff"
                            bar value valence range max_stat xsize 200 ysize 18 left_bar "#ff6b9d" right_bar "#2c3e50"
                            text "[valence:.02f]/[max_stat]" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            text "Arousal (Intensitas)" size 16 color "#ffffff"
                            bar value arousal range max_stat xsize 200 ysize 18 left_bar "#ffd93d" right_bar "#2c3e50"
                            text "[arousal:.02f]/[max_stat]" size 14 color "#bdc3c7"
                    
                    null height 15
                    
                    # Skills
                    text "Kemampuan" size 22 color "#27ae60" bold True
                    
                    hbox:
                        spacing 20
                        vbox:
                            spacing 5
                            $ practical_level = get_level_from_xp(practical_xp)
                            $ xp_in_level = get_xp_in_level(practical_xp, practical_level)
                            $ required = get_required_for_level(practical_level)
                            text "Praktis" size 16 color "#ffffff"
                            text "Level [practical_level]" size 16 color "#ffffff"
                            bar value xp_in_level range required xsize 200 ysize 18 left_bar "#16a085" right_bar "#2c3e50"
                            text "[xp_in_level:.02f]/[required] XP" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            $ writing_level = get_level_from_xp(writing_xp)
                            $ xp_in_level = get_xp_in_level(writing_xp, writing_level)
                            $ required = get_required_for_level(writing_level)
                            text "Menulis" size 16 color "#ffffff"
                            text "Level [writing_level]" size 16 color "#ffffff"
                            bar value xp_in_level range required xsize 200 ysize 18 left_bar "#27ae60" right_bar "#2c3e50"
                            text "[xp_in_level:.02f]/[required] XP" size 14 color "#bdc3c7"