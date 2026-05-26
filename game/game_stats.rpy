# Define stats
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

# Sleep mechanic variables (based on circadian rhythm and adenosine buildup)
default sleep_debt = 0  # Hours of missed sleep, accumulates over time
default adenosine_level = 0  # Sleep pressure (0-100), increases during wakefulness
default last_sleep_time = 0  # Timestamp (in hours) of last sleep
default caffeine_level = 0  # Caffeine in system (0-100), blocks adenosine
default total_hours_awake = 0  # Track how long character has been awake

# Per activity motivation
default activity_last_done = {}
default current_motivation_value = 0.0
default current_motivation_label = "Butuh"

# Emotion system based on (valence, arousal) and stats
init python:
    # Emotion coordinates in (valence, arousal) space
    emotions_data = {
        "gembira": {"valence": 81.3, "arousal": 83.4, "color": "#ff6b9d", "description": "Energized and enthusiastic", "score_multiplier": 1.5}, # Excited
        "senang": {"valence": 90.1, "arousal": 68.6, "color": "#ffd93d", "description": "Content and joyful", "score_multiplier": 1.4}, # Happy
        "puas": {"valence": 86.8, "arousal": 49.3, "color": "#6bcf7f", "description": "Pleased and content", "score_multiplier": 1.3}, # Satisfied
        "santai": {"valence": 75.0, "arousal": 17.4, "color": "#4a90e2", "description": "Calm and peaceful", "score_multiplier": 1.2}, #Relaxed
        "tenang": {"valence": 78.7, "arousal": 42.5, "color": "#62bac0", "description": "Calm and composed", "score_multiplier": 1.1}, # Calm
        "bosan": {"valence": 24.4, "arousal": 22.9, "color": "#95a5a6", "description": "Unengaged and listless", "score_multiplier": 0.7}, # Bored
        "depresi": {"valence": 10.4, "arousal": 46.5, "color": "#34495e", "description": "Sad and fatigued", "score_multiplier": 0.4}, # Depressed
        "sedih": {"valence": 5.4, "arousal": 38.6, "color": "#2c3e50", "description": "Melancholic and withdrawn", "score_multiplier": 0.5}, # Sad
        "kacau": {"valence": 12.5, "arousal": 60.8, "color": "#e74c3c", "description": "Angry and agitated", "score_multiplier": 0.6}, # Upset
        "stres": {"valence": 12.5, "arousal": 80.9, "color": "#c0392b", "description": "Anxious and overwhelmed", "score_multiplier": 0.5}, #Stressed
        "grogi": {"valence": 28.6, "arousal": 69.9, "color": "#e67e22", "description": "Anxious and alert", "score_multiplier": 0.8}, # Nervous
        "tegang": {"valence": 32.0, "arousal": 69.1, "color": "#d35400", "description": "Tense and activated", "score_multiplier": 0.7}, # Tense
        "neutral": {"valence": 50.0, "arousal": 50.0, "color": "#7f8c8d", "description": "Neutral and balanced", "score_multiplier": 1.0} # Neutral
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

init python:
    # Per second decay function (called every in-game minute)
    def decrease_stats(time_minutes):
        """Decrease stats over time without going negative."""
        global autonomy, competence, relatedness, nutrition, physical_activity, sleep, valence, arousal
        global sleep_debt, adenosine_level

        autonomy_modifier = store.autonomy * 0.015
        if store.autonomy < 50:
            store.autonomy = min(max_stat, store.autonomy + autonomy_modifier/60 * time_minutes)
        else:
            store.autonomy = max(0, store.autonomy - autonomy_modifier/60 * time_minutes)

        competence_modifier = store.competence * 0.015
        store.competence = max(0, store.competence - (competence_modifier/60 * time_minutes))

        relatedness_modifier = store.relatedness * 0.015
        store.relatedness = max(0, store.relatedness - (relatedness_modifier/60 * time_minutes))

        store.nutrition = max(0, store.nutrition - (5/48 * time_minutes)) # 50% / 8 hours
        
        pa_modifier = store.physical_activity * 0.025
        store.physical_activity = max(0, store.physical_activity - (pa_modifier/60 * time_minutes))
        
        # Update sleep-wake cycle: adenosine builds up, decreasing sleep stat
        update_adenosine()
        
        # Sleep stat decreases faster based on adenosine level
        # If adenosine is high (high sleep pressure), sleep stat drops faster
        adenosine_effect = (adenosine_level / 100) * 0.05  # Max 0.05 extra per minute
        store.sleep = max(0, store.sleep - (0.0625 * time_minutes) - adenosine_effect)
        
        # Apply circadian rhythm effect: sleep stat decreases slower during optimal sleep times
        circadian_factor = get_circadian_rhythm_factor()
        if circadian_factor < 0.5:  # Daytime (poor sleep alignment)
            store.sleep = max(0, store.sleep - (0.02 * time_minutes))  # Extra penalty during day
        
        store.valence = max(0, store.valence - (6/60 * time_minutes))
        store.arousal = max(0, store.arousal - (6/60 * time_minutes))
        
        # Apply sleep deprivation penalties
        if store.sleep <= 30:  # Only when really tired
            sleep_debt += time_minutes / 60  # Accumulate sleep debt in hours
        
        #apply_sleep_deprivation_penalty()
        update_motivation_and_progress()  # Ensure motivation is updated based on current stats
        
        renpy.retain_after_load()

    # Python function to calculate motivation and progress
    def update_motivation_and_progress():
        global motivation, thesis_progress, autonomy, competence, relatedness
        global nutrition, physical_activity, sleep
        
        # Motivation is the lowest stat among psychological and physical needs
        # This reflects that if any basic need is not met, motivation suffers
        all_stats = [autonomy, competence, relatedness, nutrition, physical_activity, sleep]
        motivation = min(all_stats)
        
        # Check for burnout
        # if motivation <= 0:
        #     renpy.jump("burnout")
        
        # Check for completion
        # if thesis_progress >= 100:
        #     renpy.jump("thesis_complete")

init python:
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
        base_recovery = hours_slept * 12.5
        
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
            # Severe penalty for 4+ hours of debt
            else:
                severe_debt = sleep_debt - 4
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

init python:
    # Per activity motivation related functions
    _MOTIVATION_STATS_CAPPED = [
        "nutrition", "physical_activity", "autonomy", "competence",
        "relatedness", "valence", "arousal", "caffeine_level"
    ]
    _MOTIVATION_STATS_UNCAPPED = ["writing_xp", "practical_xp"]

    # Stats whose deficit drives motivation for each activity.
    # Low stat value = high deficit = high motivation to do that activity.
    _ACTIVITY_NEEDS = {
        # "skripsi":         ["autonomy", "competence"],
        # "cari_jurnal":     ["autonomy", "competence"],
        "olahraga":        ["physical_activity"],
        # "bimbingan":       ["competence", "relatedness"],
        "sosialisasi":     ["relatedness"],
        "nap":             ["sleep", "arousal"],
        # "tidur":           ["sleep", "arousal"],
        # "workshop":        ["competence"],
        # "belajar_mandiri": ["competence", "autonomy"],
        "rest":            ["arousal", "valence"],
        "chat_online":     ["relatedness", "valence"],
        "main_game":       ["autonomy", "valence", "arousal"],
        "makan_bergizi":   ["nutrition"],
        "makan_enak":      ["nutrition", "valence"],
        "minum_kopi":      ["arousal"],
    }

    def get_activity_motivation(activity_key):
        """
        Returns (value, label) where value is in [0, 1].
        value >=  0.6 : activity will be carried out
        value >= 0.3: 80% chance the activity is carried out this minute
        value <  0.3: activity stops (need already satisfied)
        """
        needs = _ACTIVITY_NEEDS.get(activity_key, [])
        if not needs:
            if motivation >= 70:
                return motivation, "Termotivasi"
            elif motivation >= 30:
                return motivation, "Ragu-ragu"
            else:
                return motivation, "Tidak Berminat"

        max_s = float(getattr(store, 'max_stat', 100))
        avg_deficit = sum((max_s - getattr(store, s, max_s)) / max_s for s in needs) / len(needs)
        #value = avg_deficit * 2.0 - 1.0

        # if value >= 0.5:
        #     label = "Sangat Termotivasi"
        # elif value >= 0.0:
        #     label = "Termotivasi"
        # elif value >= -0.5:
        #     label = "Ragu-ragu"
        # else:
        #     label = "Tidak Berminat"

        if avg_deficit >= 0.7:
            label = "Termotivasi"
        elif avg_deficit >= 0.3:
            label = "Ragu-ragu"
        else:
            label = "Tidak Berminat"

        return round(avg_deficit, 2), label

    # Returns True if the activity is carried
    def get_common_motivation():
        if motivation < 30:
            if renpy.random.randint(1, 2) < 2:
                store.interrupted = True
                return False
        elif motivation < 70:
            if renpy.random.randint(1, 10) > 9:
                store.interrupted = True
                return False
        return True