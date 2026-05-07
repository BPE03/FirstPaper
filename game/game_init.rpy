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

# Sleep mechanic variables (based on circadian rhythm and adenosine buildup)
default sleep_debt = 0  # Hours of missed sleep, accumulates over time
default adenosine_level = 0  # Sleep pressure (0-100), increases during wakefulness
default last_sleep_time = 0  # Timestamp (in hours) of last sleep
default caffeine_level = 0  # Caffeine in system (0-100), blocks adenosine
default total_hours_awake = 0  # Track how long character has been awake

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
        global sleep_debt, adenosine_level

        #store.autonomy = max(0, store.autonomy - 0.3)
        competence = max(0, competence - (0.1 * time_minutes))
        relatedness = max(0, relatedness - (0.1 * time_minutes))
        nutrition = max(0, nutrition - (0.104 * time_minutes))
        physical_activity = max(0, physical_activity - (0.1 * time_minutes))
        
        # Update sleep-wake cycle: adenosine builds up, decreasing sleep stat
        update_adenosine()
        
        # Sleep stat decreases faster based on adenosine level
        # If adenosine is high (high sleep pressure), sleep stat drops faster
        adenosine_effect = (adenosine_level / 100) * 0.05  # Max 0.05 extra per minute
        sleep = max(0, sleep - (0.0625 * time_minutes) - adenosine_effect)
        
        # Apply circadian rhythm effect: sleep stat decreases slower during optimal sleep times
        circadian_factor = get_circadian_rhythm_factor()
        if circadian_factor < 0.5:  # Daytime (poor sleep alignment)
            sleep = max(0, sleep - (0.02 * time_minutes))  # Extra penalty during day
        
        valence = max(0, valence - (0.1 * time_minutes))
        arousal = max(0, arousal - (0.1 * time_minutes))
        
        # Apply sleep deprivation penalties
        if sleep <= 30:  # Only when really tired
            sleep_debt += time_minutes / 60  # Accumulate sleep debt in hours
        
        apply_sleep_deprivation_penalty()
        
        renpy.retain_after_load()

    # Sleep Mechanic Functions (based on NHLBI Sleep-Wake Cycle research)
    # https://www.nhlbi.nih.gov/health/sleep/sleep-wake-cycle
    
    def get_circadian_rhythm_factor():
        """
        Returns a factor (0.0-1.0) representing how aligned the current time is 
        with natural sleep patterns. Based on melatonin release and cortisol patterns.
        
        Peak sleep time: 2-4 AM (factor ~1.0 - best sleep)
        Wake time: 6-8 AM (cortisol rises)
        Afternoon dip: 2-3 PM (factor ~0.6)
        Evening: 10 PM - midnight (factor ~0.9)
        """
        hour = current_hour
        
        # Night time: 10 PM - 8 AM is prime sleep time
        if 22 <= hour or hour < 8:
            # Peak at 2-4 AM (hour 2-4)
            if 2 <= hour < 4:
                return 1.0
            # Good sleep time 10 PM - 8 AM
            elif 22 <= hour or hour < 6:
                return 0.9
            # Morning transition 6-8 AM (waking up with cortisol)
            else:  # 6-8
                return 0.7
        # Morning: 8 AM - noon (awake time, low sleep quality)
        elif 8 <= hour < 12:
            return 0.2
        # Afternoon: noon - 6 PM (very low, afternoon energy dip 2-3 PM is ~0.6)
        elif 12 <= hour < 15:
            return 0.4
        elif 15 <= hour < 18:
            return 0.3
        # Evening: 6 PM - 10 PM (gradually increasing melatonin)
        else:  # 18-22
            return 0.5
    
    def update_adenosine():
        """
        Updates adenosine level based on time awake.
        Adenosine is a compound that builds up during wakefulness and signals
        the need for sleep. Caffeine blocks adenosine.
        """
        global adenosine_level, total_hours_awake, caffeine_level
        
        # Adenosine increases ~10 points per hour awake
        adenosine_increase = 0.167  # 10 per hour = 0.167 per minute
        
        # Caffeine fades over time (~25% per hour)
        caffeine_level = max(0, caffeine_level - 0.417)  # 25% per hour = 0.417 per minute
        
        # Caffeine blocks adenosine (reduces perceived sleep pressure)
        if caffeine_level > 0:
            caffeine_blocking = (caffeine_level / 100) * 0.5  # Max 50% reduction
            adenosine_level = max(0, adenosine_level - (adenosine_increase * caffeine_blocking))
        else:
            adenosine_level = min(100, adenosine_level + adenosine_increase)
        
        total_hours_awake += 1/60  # Convert minutes to hours
    
    def get_sleep_quality_factor():
        """
        Returns a factor (0.0-2.0) for how effectively sleep restores the character.
        Based on:
        - Time of day (circadian alignment)
        - Hours slept (more is better, diminishing returns after 8 hours)
        - Sleep debt (recovering from debt reduces quality slightly)
        """
        circadian_factor = get_circadian_rhythm_factor()
        
        # More circadian alignment = better sleep quality
        return 0.5 + (circadian_factor * 1.5)
    
    def calculate_sleep_recovery(hours_slept):
        """
        Calculates how much sleep stat recovery occurs for sleeping N hours.
        Takes into account circadian rhythm and sleep debt.
        
        Returns: (sleep_stat_gained, adenosine_reduction)
        """
        # Base recovery: ~20 points per hour of sleep
        base_recovery = hours_slept * 20
        
        # Apply circadian factor for quality
        quality_factor = get_sleep_quality_factor()
        recovery_with_quality = base_recovery * (quality_factor / 2.0)
        
        # Diminishing returns after 8 hours
        if hours_slept > 8:
            excess = hours_slept - 8
            recovery_with_quality = recovery_with_quality - (excess * 5)
        
        # Cap at max sleep stat
        sleep_recovery = min(100, recovery_with_quality)
        
        # Adenosine reduction: almost complete reset with good sleep
        adenosine_reduction = hours_slept * 15  # 100 adenosine cleared per ~6.7 hours
        
        return (sleep_recovery, adenosine_reduction)
    
    def apply_sleep_deprivation_penalty():
        """
        Applies penalties to stats when sleep debt is high.
        Based on research showing sleep deprivation affects cognitive function,
        emotional regulation, and immune system.
        """
        global autonomy, competence, relatedness, valence, arousal, sleep_debt
        
        if sleep_debt > 0:
            # Mild penalty for 1-4 hours of debt
            if sleep_debt <= 4:
                penalty = sleep_debt * 2
                competence = max(0, competence - penalty)
            # Severe penalty for 4+ hours of debt
            else:
                severe_debt = sleep_debt - 4
                competence = max(0, competence - (8 + severe_debt * 5))
                arousal = max(0, arousal - (severe_debt * 3))
                valence = max(0, valence - (severe_debt * 2))
    
    def perform_sleep(hours_to_sleep):
        """
        Main sleep function that handles sleeping for N hours.
        Updates all relevant stats and time.
        """
        global sleep, adenosine_level, total_hours_awake, sleep_debt
        global valence, arousal, current_hour, current_minute, current_day
        global current_month, current_year
        
        # Validate input
        hours_to_sleep = max(1, min(12, hours_to_sleep))  # Clamp 1-12 hours
        
        # Calculate sleep recovery
        sleep_gained, adenosine_cleared = calculate_sleep_recovery(hours_to_sleep)
        
        # Update stats
        sleep = min(100, sleep + sleep_gained)
        adenosine_level = max(0, adenosine_level - adenosine_cleared)
        
        # Clear part of sleep debt
        debt_cleared = min(sleep_debt, hours_to_sleep)
        sleep_debt = max(0, sleep_debt - debt_cleared)
        
        # Reset time awake counter
        total_hours_awake = 0
        
        # Emotional effects of sleep (rested feeling)
        # Good sleep improves mood and arousal
        circadian_quality = get_sleep_quality_factor()
        valence = min(100, valence + (circadian_quality * 10))
        arousal = min(100, arousal + (circadian_quality * 8))
        
        # Advance time
        advance_time(int(hours_to_sleep * 60))
        
        renpy.retain_after_load()