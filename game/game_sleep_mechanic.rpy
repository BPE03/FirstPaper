default process_s           = 0.15
default wake_time_in_minute = current_hour * 60 + current_minute
default total_daily_time    = current_hour * 60 + current_minute
default circadian_phase     = 0.0
default habitual_wake       = wake_time_in_minute
default sleep_fsm_state     = "awake_normal"

init python:
    import math

    S_RISE_RATE = 0.044 / 60
    S_FALL_RATE = 0.3   / 60
    S_MIN       = 0.05
    S_MAX       = 1.0

    C_AMPLITUDE = 0.45
    C_OFFSET    = 0.50

    # ── Sleep FSM states ─────────────────────────────────────────────
    SLEEP_SLEEPING  = "sleeping"
    SLEEP_PEAK      = "awake_peak"
    SLEEP_NORMAL    = "awake_normal"
    SLEEP_FATIGUED  = "awake_fatigued"
    SLEEP_EXHAUSTED = "awake_exhausted"
    SLEEP_CRASHED   = "awake_crashed"

    # ── Process-S update ─────────────────────────────────────────────
    def sleep_build_s():
        global process_s
        process_s += S_RISE_RATE * (S_MAX - process_s)
        process_s  = min(process_s, S_MAX)

    def sleep_decay_s():
        global process_s
        disruption           = caffeine_sleep_disruption()
        circadian_quality    = 1.0 - sleep_get_process_c()
        homeostatic_override = max(0.0, (process_s - 0.75) / 0.25) * 0.25
        # At process_s = 0.75 → override = 0.0
        # At process_s = 1.00 → override = 0.25 (adds up to 0.25 quality back)
        sleep_quality  = min(1.0, circadian_quality + homeostatic_override)
        effective_rate = S_FALL_RATE * (1.0 - disruption * 0.7) * sleep_quality
        process_s     -= effective_rate * (process_s - S_MIN)
        process_s      = max(process_s, S_MIN)

    # ── Circadian signal ─────────────────────────────────────────────
    def sleep_get_process_c():
        global total_daily_time, circadian_phase
        """
        Two-harmonic circadian alertness signal anchored to clock time.
        Primary peak ~10:00-12:00, post-lunch dip ~14:00-16:00, trough ~04:00-06:00.
        """
        primary_phase   = ((total_daily_time / 60.0 - 5.0) / 24.0) * 2 * math.pi
        primary         = math.sin(primary_phase)
        secondary_phase = ((total_daily_time / 60.0 - 2.0) / 12.0) * 2 * math.pi
        secondary       = 0.20 * math.sin(secondary_phase)
        raw             = primary - secondary
        c               = (raw + 1.20) / 2.40
        if circadian_phase != 0.0:
            phase_correction = circadian_phase / 24.0 * 60 * 2 * math.pi
            c_shifted = (math.sin(primary_phase + phase_correction)
                        - 0.20 * math.sin(secondary_phase + phase_correction))
            c = (c_shifted + 1.20) / 2.40
        #print("DEBUG: process c={:.3f}".format(c))
        return max(0.0, min(1.0, c))

    # ── Alertness & derived quantities ───────────────────────────────
    def sleep_get_alertness():
        base       = sleep_get_process_c() - process_s
        caff_boost = caffeine_get_effect()
        return max(-1.0, min(1.0, base + caff_boost))

    def get_sleep_need():
        """
        Sleep need on 0-100 scale from homeostatic + circadian pressure.
        Caffeine partially masks felt urgency without changing underlying variables.
        """
        S_WEIGHT           = 0.80
        C_WEIGHT           = 0.20
        circadian_pressure = 1.0 - sleep_get_process_c()
        # effective_s is around 0.1 - 1.0
        effective_s        = (process_s - 0.1) / (1.0 - 0.1)
        effective_s        = max(0.0, min(1.0, effective_s))
        weighted_s         = effective_s * S_WEIGHT
        raw                = 1 - (effective_s + circadian_pressure * C_WEIGHT)
        if caffeine_plasma_level > 0.0:
            mask = caffeine_get_effect() * 0.4  # max 40% suppression
            raw  = max(0.0, raw + mask)
        return round(min(100.0, max(0.0, raw * 100)), 2)

    # ── FSM internals ────────────────────────────────────────────────
    def _sleep_alertness_to_state(a):
        if   a >= 0.5:  return SLEEP_PEAK
        elif a >= 0.0:  return SLEEP_NORMAL
        elif a >= -0.3:  return SLEEP_FATIGUED
        elif a >= -0.6: return SLEEP_EXHAUSTED
        else:           return SLEEP_CRASHED

    def _sleep_fsm_step():
        """Advance the Sleep FSM one minute: update process_s, then evaluate awake transitions."""
        global sleep_fsm_state, total_daily_time
        total_daily_time = current_hour * 60 + current_minute
        if sleep_fsm_state == SLEEP_SLEEPING:
            sleep_decay_s()
        else:
            sleep_build_s()
            new_state = _sleep_alertness_to_state(sleep_get_alertness())
            if new_state != sleep_fsm_state:
                sleep_fsm_state = new_state

    # ── Public API ───────────────────────────────────────────────────
    def sleep_advance_minute(minutes=1):
        for _ in range(minutes):
            _sleep_fsm_step()

    def go_to_sleep():
        global sleep_fsm_state
        sleep_fsm_state = SLEEP_SLEEPING

    def wake_up(new_wake_hour=None, new_wake_minute=None):
        global sleep_fsm_state
        sleep_fsm_state = _sleep_alertness_to_state(sleep_get_alertness())

    def sleep_get_state():
        """Returns alertness tier label. Returns 'sleeping' when asleep."""
        if sleep_fsm_state == SLEEP_SLEEPING:
            return "sleeping"
        _label = {
            SLEEP_PEAK:      "peak",
            SLEEP_NORMAL:    "normal",
            SLEEP_FATIGUED:  "fatigued",
            SLEEP_EXHAUSTED: "exhausted",
            SLEEP_CRASHED:   "crashed",
        }
        return _label.get(sleep_fsm_state, "normal")

    def sleep_stat_multiplier():
        return {
            "sleeping":  1.00,
            "peak":      1.25,
            "normal":    1.00,
            "fatigued":  0.70,
            "exhausted": 0.40,
            "crashed":   0.15,
        }[sleep_get_state()]
