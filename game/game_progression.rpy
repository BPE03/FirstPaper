default practical_xp = 0
default writing_xp = 0
default practical_level = 1
default writing_level = 1
default thesis_progress = 0
default score = 0
default earned_score = 0
default selected_bidang = None
default thesis_fsm_state = "exploring"

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

    # ── Thesis FSM states ─────────────────────────────────────────────
    THESIS_EXPLORING    = "exploring"
    THESIS_TOPIC_FOUND  = "topic_found"
    THESIS_SUPERVISED   = "supervised"
    THESIS_PROPOSAL_WRITING      = "proposal_writing"
    THESIS_SEMPRO_READY = "sempro_ready"
    THESIS_SEMPRO_FAILED = "sempro_failed"
    THESIS_POST_SEMPRO  = "post_sempro"
    THESIS_WRITING      = "writing"
    THESIS_DONE         = "done"
    THESIS_FAILED       = "failed"

    def thesis_advance_to(new_state):
        global thesis_fsm_state
        thesis_fsm_state = new_state

    def thesis_can_write():
        """True when player has a topic and can work on the thesis."""
        return thesis_fsm_state not in (THESIS_EXPLORING, THESIS_DONE)

    def thesis_has_topic():
        """True when player has found a topic candidate."""
        return thesis_fsm_state != THESIS_EXPLORING

    def thesis_advisor_approved():
        """True when advisor has approved the topic."""
        return thesis_fsm_state in (
            THESIS_SUPERVISED, THESIS_PROPOSAL_WRITING, THESIS_SEMPRO_READY,
            THESIS_POST_SEMPRO, THESIS_WRITING, THESIS_DONE,
        )

    def thesis_get_phase():
        """Returns 1 (proposal) or 2 (full thesis) for progress-rate calculation."""
        return 2 if thesis_fsm_state in (THESIS_POST_SEMPRO, THESIS_DONE) else 1

    def _thesis_on_writing_tick():
        """Auto-advance writing sub-states; called each skripsi tick."""
        if thesis_fsm_state == THESIS_SUPERVISED and store.thesis_progress > 0:
            thesis_advance_to(THESIS_PROPOSAL_WRITING)
        elif thesis_fsm_state == THESIS_PROPOSAL_WRITING and store.thesis_progress >= 100:
            thesis_advance_to(THESIS_SEMPRO_READY)
        elif thesis_fsm_state == THESIS_POST_SEMPRO and store.thesis_progress > 0:
            thesis_advance_to(THESIS_WRITING)
        elif thesis_fsm_state == THESIS_WRITING and store.thesis_progress >= 100:
            thesis_advance_to(THESIS_DONE)

    BIMBINGAN_BONUS_MULT = 1.5

    def get_thesis_progress_rate():
        global bimbingan_bonus_active, writing_level, practical_level
        """Returns per-minute thesis progress. Depends on levels, sleep, emotion, and bimbingan bonus."""

        # Get current emotion and its multiplier from emotions_data
        current_emotion = get_current_emotion()
        emotion_data = emotions_data[current_emotion]
        emotion_multiplier = emotion_data.get("score_multiplier", 1.0)

        level_mult = 1.0 + (writing_level - 1) * 0.20 + (practical_level - 1) * 0.1
        base_progress_per_hour = 1
        # Minimum progress rate = 1 * 1 * 0.4 * 0.4 = 0.16 progress/hour, or 0.0027 progress/minute
        progress_rate = base_progress_per_hour * level_mult * sleep_stat_multiplier() * emotion_multiplier

        if bimbingan_bonus_active:
            progress_rate *= BIMBINGAN_BONUS_MULT

        if thesis_get_phase() == 1:
            return progress_rate / 60
        else:
            return progress_rate / 120

    def calculate_thesis_score():
        """Calculate score gained when writing thesis based on emotion, progress done, levels, and bimbingan bonus."""
        global score, valence, arousal, practical_level, writing_level
        
        # Level bonuses
        level_bonus = (practical_level * 1) + (writing_level * 0.5)
        
        # Base score per minute of work
        base_score = 1

        # Per progress rate bonus
        progress_rate_bonus = get_thesis_progress_rate() * 60
        
        # Calculate final score
        # Minimum score = (1 + 1.5) * 0.16 = 0.256, or about 1 point every 4 minutes at the very start, scaling up with levels, emotion, and alertness
        # 0.256 * 625 * 60
        final_score = (base_score + level_bonus) * progress_rate_bonus
        
        # Ensure minimum score of 1
        #final_score = max(1, final_score)
        
        # Add to total score
        score += final_score
        
        return final_score

    def calculate_writing_xp(xp):
        # Get current emotion and its multiplier from emotions_data
        current_emotion = get_current_emotion()
        emotion_data = emotions_data[current_emotion]
        emotion_multiplier = emotion_data.get("score_multiplier", 1.0)

        store.writing_xp += xp * emotion_multiplier * sleep_stat_multiplier()

    def calculate_practical_xp(xp):
        # Get current emotion and its multiplier from emotions_data
        current_emotion = get_current_emotion()
        emotion_data = emotions_data[current_emotion]
        emotion_multiplier = emotion_data.get("score_multiplier", 1.0)

        store.practical_xp += xp * emotion_multiplier * sleep_stat_multiplier()