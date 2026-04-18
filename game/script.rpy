# Define your stats
default motivation = 100
default thesis_progress = 0
default autonomy = 100
default competence = 100
default relatedness = 100
default nutrition = 100
default physical_activity = 100
default valence = 50  # Emotional positivity
default arousal = 50  # Energy/alertness
default practical_xp = 0
default writing_xp = 0
default practical_level = 1
default writing_level = 1
default max_stat = 100

# Variable to track if detailed stats window is shown
default show_detailed_stats = False
# Variable to track if activity menu is shown
default show_activity_menu = False
# Variable to track if calendar window is shown
default show_calendar = False

# Date and time variables
default current_day = 17
default current_month = 12
default current_year = 2025
default current_hour = 9
default current_minute = 0

# Dictionary for month names
init python:
    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    
    def get_days_in_month(month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        else:  # February
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
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

    def format_time():
        return "{:02d}:{:02d}".format(current_hour, current_minute)

# Level system functions
init python:
    def get_level_from_xp(xp):
        level = 1
        cumulative = 0
        while True:
            required = level * 100
            if xp < cumulative + required:
                return level
            cumulative += required
            level += 1
    
    def get_xp_in_level(xp, level):
        cumulative = sum(i * 100 for i in range(1, level))
        return xp - cumulative
    
    def get_required_for_level(level):
        return level * 100
    
    def update_levels():
        global practical_level, writing_level
        practical_level = get_level_from_xp(practical_xp)
        writing_level = get_level_from_xp(writing_xp)

# Emotion system based on (valence, arousal)
init python:
    # Emotion coordinates in (valence, arousal) space
    emotions_data = {
        "excited": {"valence": 81.3, "arousal": 83.4, "color": "#ff6b9d", "description": "Energized and enthusiastic"},
        "happy": {"valence": 90.1, "arousal": 68.6, "color": "#ffd93d", "description": "Content and joyful"},
        "satisfied": {"valence": 86.8, "arousal": 49.3, "color": "#6bcf7f", "description": "Pleased and content"},
        "relaxed": {"valence": 75.0, "arousal": 17.4, "color": "#4a90e2", "description": "Calm and peaceful"},
        "bored": {"valence": 24.4, "arousal": 22.9, "color": "#95a5a6", "description": "Unengaged and listless"},
        "depressed": {"valence": 10.4, "arousal": 46.5, "color": "#34495e", "description": "Sad and fatigued"},
        "sad": {"valence": 5.4, "arousal": 38.6, "color": "#2c3e50", "description": "Melancholic and withdrawn"},
        "upset": {"valence": 12.5, "arousal": 60.8, "color": "#e74c3c", "description": "Angry and agitated"},
        "stressed": {"valence": 12.5, "arousal": 80.9, "color": "#c0392b", "description": "Anxious and overwhelmed"},
        "nervous": {"valence": 28.6, "arousal": 69.9, "color": "#e67e22", "description": "Anxious and alert"},
        "tense": {"valence": 32.0, "arousal": 69.1, "color": "#d35400", "description": "Tense and activated"},
        "neutral": {"valence": 50.0, "arousal": 50.0, "color": "#7f8c8d", "description": "Neutral and balanced"}
    }
    
    def get_emotion_distance(v1, a1, v2, a2):
        """Calculate Euclidean distance between two (valence, arousal) points."""
        return ((v1 - v2) ** 2 + (a1 - a2) ** 2) ** 0.5
    
    def get_current_emotion():
        """Find the emotion closest to current valence and arousal values."""
        min_distance = float('inf')
        closest_emotion = "neutral"
        
        for emotion_name, emotion_data in emotions_data.items():
            distance = get_emotion_distance(
                valence, arousal,
                emotion_data["valence"],
                emotion_data["arousal"]
            )
            if distance < min_distance:
                min_distance = distance
                closest_emotion = emotion_name
        
        return closest_emotion
    
    def get_emotion_info(emotion_name):
        """Get information about a specific emotion."""
        if emotion_name in emotions_data:
            info = emotions_data[emotion_name].copy()
            info["name"] = emotion_name
            return info
        return None
    
    def get_all_emotions():
        """Get list of all available emotions."""
        return list(emotions_data.keys())
    
    def set_emotion(emotion_name):
        """Set valence and arousal to match a specific emotion."""
        global valence, arousal
        if emotion_name in emotions_data:
            emotion = emotions_data[emotion_name]
            valence = emotion["valence"]
            arousal = emotion["arousal"]
            return True
        return False
    
    def decrease_stats():
        """Decrease stats over time without going negative."""
        global autonomy, competence, relatedness, nutrition, physical_activity, valence, arousal
        
        autonomy = max(0, autonomy - 0.3)
        competence = max(0, competence - 0.2)
        relatedness = max(0, relatedness - 0.4)
        nutrition = max(0, nutrition - 0.8)
        physical_activity = max(0, physical_activity - 0.6)
        valence = max(0, valence - 0.3)
        arousal = max(0, arousal - 0.7)

# Main stats display (always visible)
screen main_stats():
    frame:
        xalign 0.05
        yalign 0.05
        xsize 280
        ysize 350
        background "#2c3e50cc"
        padding (15, 15)
        
        vbox:
            spacing 15
            
            text "Thesis Journey" size 24 color "#ecf0f1" bold True
            
            # Current emotion display
            $ current_emotion = get_current_emotion()
            $ emotion_info = get_emotion_info(current_emotion)
            
            # Motivation stat
            text "Motivation" size 18 color "#ffffff"
            bar:
                value motivation
                range max_stat
                xsize 250
                ysize 22
                left_bar "#e74c3c"
                right_bar "#34495e"
            text "[motivation:.02f]/[max_stat]" size 14 color "#bdc3c7"
            
            # Thesis Progress
            text "Thesis Progress" size 18 color "#ffffff"
            bar:
                value thesis_progress
                range max_stat
                xsize 250
                ysize 22
                left_bar "#2ecc71"
                right_bar "#34495e"
            text "[thesis_progress]%" size 14 color "#bdc3c7"

            frame:
                xsize 250
                ysize 50
                background emotion_info["color"]
                padding (10, 10)
                
                vbox:
                    spacing 3
                    text "Emotion" size 12 color "#ffffff"
                    text "[current_emotion.upper()]" size 16 color "#ffffff" bold True
                    text "[emotion_info['description']]" size 11 color "#ffffff"
    
            null height 30
            # Button to show detailed stats
            textbutton "View Detailed Stats" action ToggleVariable("show_detailed_stats") xsize 250 ysize 75
    
    # Timer that affects stats every second
    timer 1.0 repeat True action [
        Function(decrease_stats),
        Function(update_motivation_and_progress)
    ]

screen calendar_now():
    frame:
        xalign 0.95
        yalign 0.05
        xsize 280
        ysize 120
        background "#2c3e50cc"
        padding (15, 15)
        
        vbox:
            spacing 15
            
            text "[current_day]/[current_month]/[current_year]" size 28 color "#ffffff"
            text "[format_time()]" size 28 color "#ffffff"
            textbutton "{size=24}View Calendar" action ToggleVariable("show_calendar") xsize 200 ysize 75
    # Timer that affects stats every second
    timer 1.0 repeat True action [
        Function(advance_time, 1)
    ]

# Imagemap for interactive areas (always visible)
screen interactive_room():
    # Main room imagemap
    imagemap:
        ground "bg room"  # Your background image
        hover "bg room_hover"  # Optional: hover overlay image
        
        # Define clickable hotspots (x, y, width, height)
        # Adjust these coordinates to match your background image
        
        # Example: Click on desk area to open activity menu
        hotspot (800, 400, 200, 150) action SetVariable("show_activity_menu", True)
        
        # You can add more hotspots for different interactions
        # Example: Click on bed for rest activities
        # hotspot (100, 300, 150, 200) action Jump("rest_activities")
        
        # Example: Click on bookshelf for academic activities
        # hotspot (1200, 200, 180, 300) action Jump("academic_activities")
    
    # Optional: Show a button overlay if you want a visible button
    # You can remove this if you want just invisible hotspots
    # imagebutton:
    #     xalign 0.95
    #     yalign 0.95
    #     idle "gui/button/do_something_idle.png"  # Replace with your image
    #     hover "gui/button/do_something_hover.png"  # Replace with your image
    #     action SetVariable("show_activity_menu", True)
    
    # Alternative text button (remove if using image button above)
    textbutton "Do Something":
        xalign 0.95
        yalign 0.95
        xsize 200
        ysize 60
        text_size 22
        action Jump("main_gameplay")

# Warning screen for low motivation
screen motivation_warning():
    frame:
        background "#000000cc"
        xfill True
        yfill True
        
        frame:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 200
            background "#e74c3c"
            padding (20, 20)
            
            vbox:
                spacing 20
                text "Too Unmotivated!" size 24 color "#ffffff" bold True xalign 0.5
                text "You need more than 30 motivation to work effectively on your thesis." size 16 color "#ffffff" text_align 0.5
                textbutton "OK" action Hide("motivation_warning") xalign 0.5 xsize 150 ysize 45

# Calendar window
screen calendar_window():
    if show_calendar:
        # Modal background
        frame:
            background "#000000aa"
            xfill True
            yfill True
            
            # Calendar window
            frame:
                xalign 0.5
                yalign 0.2
                xsize 600
                ysize 600
                background "#34495e"
                padding (25, 25)
                
                vbox:
                    spacing 15
                    
                    hbox:
                        text "Calendar - [month_names[current_month]] [current_year]" size 28 color "#ecf0f1" bold True
                        xfill True
                        textbutton "✕ Close" action SetVariable("show_calendar", False) text_size 20 xalign 1.0
                    
                    null height 10
                    
                    # Current date and time display
                    frame:
                        background "#2c3e50"
                        padding (15, 15)
                        xsize 550
                        
                        vbox:
                            spacing 5
                            text "Current Date & Time" size 18 color "#3498db" bold True
                            text "[month_names[current_month]] [current_day], [current_year]" size 22 color "#ffffff"
                            text "{:02d}:{:02d}".format(current_hour, current_minute) size 32 color "#2ecc71" bold True
                    
                    null height 10
                    
                    # Day of week headers
                    hbox:
                        spacing 5
                        for day_name in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
                            text day_name size 16 color "#ecf0f1" bold True xsize 75 text_align 0.5
                    
                    # Calendar grid
                    python:
                        days_in_month = get_days_in_month(current_month, current_year)
                        # Calculate first day of month (simplified - starts on Sunday for demo)
                        import datetime
                        first_day = datetime.date(current_year, current_month, 1).weekday()
                        first_day = (first_day + 1) % 7  # Adjust so Sunday = 0
                    
                    # Calendar days
                    vbox:
                        spacing 5
                        for week in range(6):  # Maximum 6 weeks in a month
                            hbox:
                                spacing 5
                                for day_of_week in range(7):
                                    $ day_number = week * 7 + day_of_week - first_day + 1
                                    if day_number > 0 and day_number <= days_in_month:
                                        if day_number == current_day:
                                            # Highlight current day
                                            frame:
                                                background "#2ecc71"
                                                xsize 75
                                                ysize 50
                                                padding (5, 5)
                                                text "[day_number]" size 18 color "#ffffff" bold True xalign 0.5 yalign 0.5
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

# Detailed stats window (shown when button is pressed)
screen detailed_stats_window():
    if show_detailed_stats:
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
                        text "Detailed Statistics" size 28 color "#ecf0f1" bold True
                        textbutton "✕ Close" action SetVariable("show_detailed_stats", False) text_size 20
                    
                    null height 10
                    
                    # Psychological Needs
                    text "Psychological Needs" size 22 color "#3498db" bold True
                    
                    hbox:
                        spacing 20
                        vbox:
                            spacing 5
                            text "Autonomy" size 16 color "#ffffff"
                            bar value autonomy range max_stat xsize 200 ysize 18 left_bar "#9b59b6" right_bar "#2c3e50"
                            text "[autonomy:.02f]/[max_stat]" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            text "Competence" size 16 color "#ffffff"
                            bar value competence range max_stat xsize 200 ysize 18 left_bar "#3498db" right_bar "#2c3e50"
                            text "[competence:.02f]/[max_stat]" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            text "Relatedness" size 16 color "#ffffff"
                            bar value relatedness range max_stat xsize 200 ysize 18 left_bar "#1abc9c" right_bar "#2c3e50"
                            text "[relatedness:.02f]/[max_stat]" size 14 color "#bdc3c7"
                    
                    null height 15
                    
                    # Physical Wellbeing
                    text "Physical Wellbeing" size 22 color "#e67e22" bold True
                    
                    hbox:
                        spacing 20
                        vbox:
                            spacing 5
                            text "Nutrition" size 16 color "#ffffff"
                            bar value nutrition range max_stat xsize 200 ysize 18 left_bar "#f39c12" right_bar "#2c3e50"
                            text "[nutrition:.02f]/[max_stat]" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            text "Physical Activity" size 16 color "#ffffff"
                            bar value physical_activity range max_stat xsize 200 ysize 18 left_bar "#e74c3c" right_bar "#2c3e50"
                            text "[physical_activity:.02f]/[max_stat]" size 14 color "#bdc3c7"
                    
                    null height 15
                    
                    # Emotional State
                    text "Emotional State" size 22 color "#e91e63" bold True
                    
                    hbox:
                        spacing 20
                        vbox:
                            spacing 5
                            text "Valence (Positivity)" size 16 color "#ffffff"
                            bar value valence range max_stat xsize 200 ysize 18 left_bar "#ff6b9d" right_bar "#2c3e50"
                            text "[valence:.02f]/[max_stat]" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            text "Arousal (Alertness)" size 16 color "#ffffff"
                            bar value arousal range max_stat xsize 200 ysize 18 left_bar "#ffd93d" right_bar "#2c3e50"
                            text "[arousal:.02f]/[max_stat]" size 14 color "#bdc3c7"
                    
                    null height 15
                    
                    # Skills
                    text "Skills" size 22 color "#27ae60" bold True
                    
                    hbox:
                        spacing 20
                        vbox:
                            spacing 5
                            $ practical_level = get_level_from_xp(practical_xp)
                            $ xp_in_level = get_xp_in_level(practical_xp, practical_level)
                            $ required = get_required_for_level(practical_level)
                            text "Practical Skill Level [practical_level]" size 16 color "#ffffff"
                            bar value xp_in_level range required xsize 200 ysize 18 left_bar "#16a085" right_bar "#2c3e50"
                            text "[xp_in_level]/[required] XP" size 14 color "#bdc3c7"
                        
                        vbox:
                            spacing 5
                            $ writing_level = get_level_from_xp(writing_xp)
                            $ xp_in_level = get_xp_in_level(writing_xp, writing_level)
                            $ required = get_required_for_level(writing_level)
                            text "Writing Skill Level [writing_level]" size 16 color "#ffffff"
                            bar value xp_in_level range required xsize 200 ysize 18 left_bar "#27ae60" right_bar "#2c3e50"
                            text "[xp_in_level]/[required] XP" size 14 color "#bdc3c7"

# Python function to calculate motivation and progress
init python:
    def update_motivation_and_progress():
        global motivation, thesis_progress, autonomy, competence, relatedness
        global nutrition, physical_activity, valence, arousal
        global practical_level, writing_level
        
        # Calculate motivation based on psychological needs and emotional state
        psychological_avg = (autonomy + competence + relatedness) / 3
        physical_avg = (nutrition + physical_activity) / 2
        
        # Motivation is influenced by all factors
        target_motivation = (psychological_avg * 0.6 + physical_avg * 0.4)
        
        # Gradually adjust motivation towards target
        # if motivation < target_motivation:
        #     motivation = min(max_stat, motivation + 0.2)
        # elif motivation > target_motivation:
        #     motivation = max(0, motivation - 0.2)

        # Instantly adjust motivation
        motivation = target_motivation
        
        # Check for burnout
        if motivation <= 0 or (autonomy <= 10 and competence <= 10):
            renpy.jump("burnout")
        
        # Check for completion
        if thesis_progress >= 100:
            renpy.jump("thesis_complete")

# Label to start the game
label start:
    "Welcome to the Thesis Writing Simulator!"
    "You are a graduate student working on your thesis."
    "Manage your wellbeing, skills, and motivation to complete your thesis successfully!"
    "Click on interactive areas or the button to perform activities."

    # Show all screens
    show screen main_stats
    show screen detailed_stats_window
    show screen calendar_now
    show screen calendar_window
    
    call screen interactive_room

# Main gameplay loop
label main_gameplay:
    menu:
        "What would you like to do?"
        
        "Work on thesis (Requires motivation > 30)":
            if motivation > 30:
                $ thesis_progress = min(100, thesis_progress + 2)
                $ competence = min(max_stat, competence + 1)
                $ writing_xp += 10
                $ practical_xp += 5
                $ update_levels()
                $ arousal = max(0, arousal - 5)
                $ nutrition = max(0, nutrition - 3)
                $ update_motivation_and_progress()
                "You worked on your thesis. Progress made!"
            else:
                "You're too unmotivated to work effectively right now."
        
        "Eat a healthy meal":
            $ nutrition = min(max_stat, nutrition + 35)
            $ valence = min(max_stat, valence + 5)
            $ update_motivation_and_progress()
            "You ate a nutritious meal. You feel better!"
        
        "Exercise / Go for a walk":
            $ physical_activity = min(max_stat, physical_activity + 30)
            $ arousal = min(max_stat, arousal + 15)
            $ valence = min(max_stat, valence + 10)
            $ update_motivation_and_progress()
            "You exercised. You feel refreshed and energized!"
        
        "Meet with advisor":
            $ autonomy = min(max_stat, autonomy + 15)
            $ competence = min(max_stat, competence + 10)
            $ relatedness = min(max_stat, relatedness + 20)
            $ practical_xp += 5
            $ update_levels()
            $ update_motivation_and_progress()
            "You met with your advisor. You gained clarity and direction!"
        
        "Socialize with friends":
            $ relatedness = min(max_stat, relatedness + 30)
            $ valence = min(max_stat, valence + 20)
            $ update_motivation_and_progress()
            "You spent time with friends. You feel connected and happy!"
        
        "Take a nap":
            $ arousal = min(max_stat, arousal + 25)
            $ valence = min(max_stat, valence + 10)
            $ update_motivation_and_progress()
            "You took a nap. You feel more alert now!"
        
        "Attend a workshop / Learn new skills":
            $ practical_xp += 15
            $ writing_xp += 10
            $ update_levels()
            $ competence = min(max_stat, competence + 10)
            $ arousal = max(0, arousal - 10)
            $ update_motivation_and_progress()
            "You attended a workshop. Your skills improved!"
        
        "Practice self-directed learning":
            $ autonomy = min(max_stat, autonomy + 20)
            $ writing_xp += 8
            $ update_levels()
            $ update_motivation_and_progress()
            "You studied independently. You feel more in control!"
        
        "Just rest and do nothing":
            $ arousal = min(max_stat, arousal + 10)
            $ valence = min(max_stat, valence + 5)
            $ update_motivation_and_progress()
            "You took some time to rest."
        
        "Cancel":
            call screen interactive_room
    call screen interactive_room

# Burnout ending
label burnout:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen interactive_room
    hide screen calendar_now
    hide screen calendar_window
    
    scene black with dissolve
    
    centered "{color=#e74c3c}{size=40}BURNOUT{/size}{/color}\n\nYou've experienced burnout and need to take a break from your thesis."
    centered "Remember: Taking care of your wellbeing is essential for academic success!"
    
    menu:
        "Try again?"
        
        "Yes, restart":
            $ motivation = 100
            $ thesis_progress = 0
            $ autonomy = 100
            $ competence = 100
            $ relatedness = 100
            $ nutrition = 100
            $ physical_activity = 100
            $ valence = 100
            $ arousal = 100
            $ practical_xp = 0
            $ writing_xp = 0
            $ practical_level = 1
            $ writing_level = 1
            jump start
        
        "No, quit":
            "Thanks for playing!"
            return

# Thesis completion ending
label thesis_complete:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen interactive_room
    hide screen calendar_now
    hide screen calendar_window
    
    scene bg graduation with dissolve
    
    centered "{color=#2ecc71}{size=50}CONGRATULATIONS!{/size}{/color}\n\nYou've completed your thesis!"
    centered "Through managing your wellbeing and developing your skills,\nyou've achieved your academic goal!"
    
    "Final Stats:"
    "Practical Skill Level: [practical_level]"
    "Writing Skill Level: [writing_level]"
    "Final Motivation: [motivation]"
    
    menu:
        "Play again?"
        
        "Yes":
            $ motivation = 100
            $ thesis_progress = 0
            $ autonomy = 100
            $ competence = 100
            $ relatedness = 100
            $ nutrition = 100
            $ physical_activity = 100
            $ valence = 50
            $ arousal = 50
            $ practical_xp = 0
            $ writing_xp = 0
            $ practical_level = 1
            $ writing_level = 1
            jump start
        
        "No":
            "Thanks for playing!"
            return