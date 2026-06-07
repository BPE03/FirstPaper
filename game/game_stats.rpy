# Define stats
default motivation = 30
default autonomy = 80
default competence = 80
default relatedness = 80
default nutrition = 30
default physical_activity = 80
default sleep = 80
default valence = 50  # Emotional positivity
default arousal = 50  # Energy/alertness
default current_emotion_state = "kosong"
default max_stat = 100

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
        "kosong": {"valence": 50.0, "arousal": 50.0, "color": "#7f8c8d", "description": "Neutral and balanced", "score_multiplier": 1.0} # Neutral
    }
    
    def get_emotion_distance(v1, a1, v2, a2):
        """Calculate Euclidean distance between two (valence, arousal) points."""
        return ((v1 - v2) ** 2 + (a1 - a2) ** 2) ** 0.5

    EMOTION_HYSTERESIS = 2.0  # min distance-improvement needed to leave current state

    # EMOTION_ON_ENTER = {
    #     # Populated with narrative triggers as story content is added.
    #     # e.g. "stres": lambda: renpy.notify("Kamu mulai merasa stres...")
    # }

    def _emotion_find_nearest():
        """Scan all centroids; return (name, distance) of the nearest to current (v, a)."""
        best_name = "kosong"
        best_dist = float('inf')
        for name, data in emotions_data.items():
            d = get_emotion_distance(valence, arousal, data["valence"], data["arousal"])
            if d < best_dist:
                best_dist = d
                best_name = name
        return best_name, best_dist

    def emotion_step():
        """Advance the Emotion one step with hysteresis. Called once per game-minute."""
        global current_emotion_state
        nearest, d_nearest = _emotion_find_nearest()
        if nearest == current_emotion_state:
            return
        d_current = get_emotion_distance(
            valence, arousal,
            emotions_data[current_emotion_state]["valence"],
            emotions_data[current_emotion_state]["arousal"],
        )
        if d_current - d_nearest < EMOTION_HYSTERESIS:
            return
        current_emotion_state = nearest
        # trigger = EMOTION_ON_ENTER.get(nearest)
        # if trigger:
        #     trigger()

    def get_current_emotion():
        """Return the current stable emotion state (hysteresis-filtered)."""
        return current_emotion_state
    
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
        """Set valence and arousal to match a specific emotion and sync FSM state immediately."""
        global valence, arousal, current_emotion_state
        if emotion_name in emotions_data:
            emotion = emotions_data[emotion_name]
            valence = emotion["valence"]
            arousal = emotion["arousal"]
            current_emotion_state = emotion_name
            return True
        return False

init python:
    # Per second decay function (called every in-game minute)
    def decrease_stats(time_minutes):
        """Decrease stats over time without going negative."""
        global autonomy, competence, relatedness, nutrition, physical_activity, sleep, valence, arousal
        #global sleep_debt, adenosine_level

        autonomy_modifier = autonomy * 0.015
        if autonomy < 50:
            autonomy = min(max_stat, autonomy + autonomy_modifier/60 * time_minutes)
        else:
            autonomy = max(0, autonomy - autonomy_modifier/60 * time_minutes)

        competence_modifier = competence * 0.015
        competence = max(0, competence - (competence_modifier/60 * time_minutes))

        relatedness_modifier = relatedness * 0.015
        relatedness = max(0, relatedness - (relatedness_modifier/60 * time_minutes))

        nutrition_modifier = nutrition * 0.12
        nutrition = max(0, nutrition - (nutrition_modifier/60 * time_minutes))
        
        pa_modifier = physical_activity * 0.025
        physical_activity = max(0, physical_activity - (pa_modifier/60 * time_minutes))
        
        #sleep_modifier = sleep * 0.08
        #sleep = max(0, sleep - (sleep_modifier/60 * time_minutes))
        caffeine_advance_minute()
        sleep_advance_minute()
        sleep = get_sleep_need()  # Sleep stat is directly tied to alertness from sleep mechanic, converted from -1..1 to 0..100
        
        valence = max(0, valence - (6/60 * time_minutes))
        arousal = max(0, arousal - (6/60 * time_minutes))

        emotion_step()

        update_motivation_and_progress()  # Ensure motivation is updated based on current stats
        
        renpy.retain_after_load()

    # Python function to calculate motivation and progress
    def update_motivation_and_progress():
        global motivation, autonomy, competence, relatedness
        global nutrition, physical_activity, sleep
        
        min_stat_for_max_motivation = 72
        min_stat_for_no_motivation = 12
        # Motivation is the lowest stat among psychological and physical needs
        # This reflects that if any basic need is not met, motivation suffers
        all_stats = [autonomy, competence, relatedness, nutrition, physical_activity, sleep]
        min_stats = min(all_stats)
        motivation = (min_stats - min_stat_for_no_motivation) / (min_stat_for_max_motivation - min_stat_for_no_motivation) * 100
        motivation = max(0, min(100, motivation))  # Ensure motivation is between 0 and 100