default practical_xp = 0
default writing_xp = 0
default practical_level = 1
default writing_level = 1
default score = 0
default earned_score = 0
default max_stat = 100
default dapat_topik = False
default dosen_acc = False
default selected_bidang = None
default phase = 1 # 1 = proposal, 2 = proposal acced

# Level system and progression functions
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
    
    def get_thesis_progress_rate():
        """Returns per-minute thesis progress. Higher writing/practical level = faster progress."""
        level_mult = 1.0 + (writing_level - 1) * 0.10 + (practical_level - 1) * 0.05
        if phase == 1:
            return (1 / 60) * level_mult
        else:
            return (1 / 120) * level_mult

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
        base_score = 1
        
        # Calculate final score
        final_score = int((base_score + level_bonus + xp_bonus) * emotion_multiplier)
        
        # Ensure minimum score of 1
        final_score = max(1, final_score)
        
        # Add to total score
        score += final_score
        
        return final_score