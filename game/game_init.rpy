# Define characters
define p = Character("Paijo", color="#77ff77")
define j = Character("Joko", color="#c9982f")

# Define your stats
default motivation = 30
default thesis_progress = 0
default autonomy = 50
default competence = 50
default relatedness = 50
default nutrition = 30
default physical_activity = 50
default sleep = 100
default valence = 50  # Emotional positivity
default arousal = 50  # Energy/alertness
default practical_xp = 0
default writing_xp = 0
default practical_level = 1
default writing_level = 1
default score = 0
default max_stat = 100

# Variable to track if detailed stats window is shown
default show_detailed_stats = False
# Variable to track if activity menu is shown
default show_activity_menu = False
# Variable to track if calendar window is shown
default show_calendar = False
# Variable to track if it's a cutscene or interactive gameplay
default in_cutscene = False

# Date and time variables
default current_day = 13
default current_month = 12
default current_year = 2025
default current_hour = 9
default current_minute = 0

# Calendar display variables
default display_month = current_month
default display_year = current_year

# Calendar event data
default calendar_events = [
    {
        "day": 9,
        "month": 1,
        "year": 2026,
        "title": "Thesis Deadline",
        "description": "Final thesis submission is due today. Prepare your final draft, supporting documents, and submit before the deadline."
    }
]
default selected_calendar_event = None
default show_event_details = False

# Python function to calculate motivation and progress
init python:
    def update_motivation_and_progress():
        global motivation, thesis_progress, autonomy, competence, relatedness
        global nutrition, physical_activity, valence, arousal
        global practical_level, writing_level
        
        # Motivation is the lowest stat among psychological and physical needs
        # This reflects that if any basic need is not met, motivation suffers
        all_stats = [autonomy, competence, relatedness, nutrition, physical_activity, sleep]
        motivation = min(all_stats)
        
        # Check for burnout
        # if motivation <= 0:
        #     renpy.jump("burnout")
        
        # Check for completion
        if thesis_progress >= 100:
            renpy.jump("thesis_complete")

    # Hide all screens during cutscenes, show during interactive gameplay
    def set_cutscene_mode(is_cutscene):
        global in_cutscene, show_calendar, show_detailed_stats
        in_cutscene = is_cutscene
        show_calendar = False  # Ensure calendar is hidden during cutscenes
        show_detailed_stats = False  # Ensure detailed stats are hidden during cutscenes
        renpy.retain_after_load()  # Ensure this state persists after loading

# Dictionary for month names
init python:
    import datetime
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
    
    def calculate_thesis_score():
        """Calculate score gained when writing thesis based on emotion, levels, and XP."""
        global score, valence, arousal, practical_level, writing_level, practical_xp, writing_xp
        
        # Get current emotion and its multiplier from emotions_data
        current_emotion = get_current_emotion()
        emotion_data = emotions_data[current_emotion]
        emotion_multiplier = emotion_data.get("score_multiplier", 1.0)
        
        # Level bonuses
        level_bonus = (practical_level * 0.5) + (writing_level * 0.5)
        
        # XP experience bonus (more XP = more experienced = better score)
        xp_bonus = (practical_xp / 1000.0) + (writing_xp / 1000.0)
        
        # Base score per thesis work session
        base_score = 10
        
        # Calculate final score
        final_score = int((base_score + level_bonus + xp_bonus) * emotion_multiplier)
        
        # Ensure minimum score of 1
        final_score = max(1, final_score)
        
        # Add to total score
        score += final_score
        
        return final_score

# Emotion system based on (valence, arousal)
init python:
    # Emotion coordinates in (valence, arousal) space
    emotions_data = {
        "excited": {"valence": 81.3, "arousal": 83.4, "color": "#ff6b9d", "description": "Energized and enthusiastic", "score_multiplier": 1.5},
        "happy": {"valence": 90.1, "arousal": 68.6, "color": "#ffd93d", "description": "Content and joyful", "score_multiplier": 1.4},
        "satisfied": {"valence": 86.8, "arousal": 49.3, "color": "#6bcf7f", "description": "Pleased and content", "score_multiplier": 1.3},
        "relaxed": {"valence": 75.0, "arousal": 17.4, "color": "#4a90e2", "description": "Calm and peaceful", "score_multiplier": 1.2},
        "bored": {"valence": 24.4, "arousal": 22.9, "color": "#95a5a6", "description": "Unengaged and listless", "score_multiplier": 0.7},
        "depressed": {"valence": 10.4, "arousal": 46.5, "color": "#34495e", "description": "Sad and fatigued", "score_multiplier": 0.4},
        "sad": {"valence": 5.4, "arousal": 38.6, "color": "#2c3e50", "description": "Melancholic and withdrawn", "score_multiplier": 0.5},
        "upset": {"valence": 12.5, "arousal": 60.8, "color": "#e74c3c", "description": "Angry and agitated", "score_multiplier": 0.6},
        "stressed": {"valence": 12.5, "arousal": 80.9, "color": "#c0392b", "description": "Anxious and overwhelmed", "score_multiplier": 0.5},
        "nervous": {"valence": 28.6, "arousal": 69.9, "color": "#e67e22", "description": "Anxious and alert", "score_multiplier": 0.8},
        "tense": {"valence": 32.0, "arousal": 69.1, "color": "#d35400", "description": "Tense and activated", "score_multiplier": 0.7},
        "neutral": {"valence": 50.0, "arousal": 50.0, "color": "#7f8c8d", "description": "Neutral and balanced", "score_multiplier": 1.0}
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
    
    def decrease_stats(time_minutes):
        """Decrease stats over time without going negative."""
        global autonomy, competence, relatedness, nutrition, physical_activity, sleep, valence, arousal

        #store.autonomy = max(0, store.autonomy - 0.3)
        competence = max(0, competence - (0.1 * time_minutes))
        relatedness = max(0, relatedness - (0.1 * time_minutes))
        nutrition = max(0, nutrition - (0.104 * time_minutes))
        physical_activity = max(0, physical_activity - (0.1 * time_minutes))
        sleep = max(0, sleep - (0.0625 * time_minutes))
        valence = max(0, valence - (0.1 * time_minutes))
        arousal = max(0, arousal - (0.1 * time_minutes))
        renpy.retain_after_load()