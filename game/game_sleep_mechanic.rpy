default process_s           = 0.15
default wake_time_in_minute = current_hour * 60 + current_minute
default total_daily_time    = current_hour * 60 + current_minute
default is_sleeping         = False
default circadian_phase      = 0.0
default habitual_wake       = wake_time_in_minute 

init python:
    import math
    S_RISE_RATE = 0.044 / 60    # per minute, awake
    S_FALL_RATE = 0.3 / 60    # per minute, asleep
    S_MIN       = 0.05
    S_MAX       = 1.0

    C_AMPLITUDE = 0.45
    C_OFFSET    = 0.50

    def sleep_advance_minute(minutes=1):
        global is_sleeping, process_s, total_daily_time
        for _ in range(minutes):
            if is_sleeping:
                sleep_decay_s()
            else:
                sleep_build_s()
            total_daily_time = current_hour * 60 + current_minute

    def sleep_build_s():
        global process_s
        process_s += S_RISE_RATE * (S_MAX - process_s)
        process_s = min(process_s, S_MAX)

    def sleep_decay_s():
        global process_s
        disruption = caffeine_sleep_disruption()
        # Base quality from circadian phase
        circadian_quality = 1.0 - sleep_get_process_c()

        # High homeostatic pressure partially overrides circadian resistance
        # Only kicks in at extreme fatigue (process_s > 0.75)
        # Reflects the biology: severe sleep deprivation forces sleep quality up slightly
        homeostatic_override = max(0.0, (process_s - 0.75) / 0.25) * 0.25
        # At process_s = 0.75 → override = 0.0
        # At process_s = 1.00 → override = 0.25 (adds up to 0.25 quality back)
        sleep_quality  = min(1.0, circadian_quality + homeostatic_override)
        effective_rate = S_FALL_RATE * (1.0 - disruption * 0.7) * sleep_quality

        process_s -= effective_rate * (process_s - S_MIN)
        process_s = max(process_s, S_MIN)

    def sleep_get_process_c():
        global total_daily_time, wake_time_in_minute, current_hour, circadian_phase
        """
        Circadian alertness signal anchored to absolute clock time.
        
        Uses a two-harmonic model to capture:
        - Primary peak: ~10:00-12:00
        - Post-lunch dip: ~14:00-16:00  
        - Evening rise: ~18:00-20:00
        - Trough: ~04:00-06:00
        
        Phase offset is fixed biologically, with slow entrainment adjustment.
        """

        # Convert to radians — full cycle over 24 hours
        # Phase shift so trough lands near 04:00
        # Without shift: sine peaks at 6hr (06:00), troughs at 18hr (18:00)
        # We want trough at ~05:00, so shift by +13 hours
        primary_phase = ((total_daily_time/60 - 5.0) / 24.0) * 2 * math.pi

        # Primary 24hr component
        primary = math.sin(primary_phase)

        # Secondary 12hr component — adds the post-lunch dip
        # Peaks again in early afternoon, creating a slight suppression
        secondary_phase = ((total_daily_time/60 - 2.0) / 12.0) * 2 * math.pi
        secondary = 0.20 * math.sin(secondary_phase)

        # Combine and normalize to 0–1
        raw = primary - secondary
        #print("DEBUG: primary={:.3f}, secondary={:.3f}, raw={:.3f}".format(primary, secondary, raw))
        #print("DEBUG: total_daily_time={}, primary_phase={:.2f} rad, secondary_phase={:.2f} rad".format(total_daily_time, primary_phase, secondary_phase))
        c = (raw + 1.20) / 2.40  # empirically scaled so range stays ~0–1

        # Apply phase shift from entrainment (slow drift over days)
        # circadian_phase is in minutes, modified by wake habits
        if circadian_phase != 0.0:
            phase_correction = circadian_phase / 24.0*60 * 2 * math.pi
            c_shifted = math.sin(primary_phase + phase_correction) - \
                        0.20 * math.sin(secondary_phase + phase_correction)
            c = (c_shifted + 1.20) / 2.40
        print("DEBUG: process c={:.3f}".format(c))
        return max(0.0, min(1.0, c))

    def sleep_get_alertness():
        global process_s
        base = sleep_get_process_c() - process_s
        caff_boost = caffeine_get_effect()
        alertness = base + caff_boost
        return max(-1.0, min(1.0, alertness))

    def get_sleep_need():
        global process_s
        """
        Sleep need on 0-100 scale.
        Combines homeostatic pressure (process_s) and 
        circadian pressure (inverted process_c).
        
        Caffeine masks the felt urgency without reducing actual need —
        so the displayed value is partially suppressed by caffeine effect,
        but the underlying variables are unchanged.
        """
        S_WEIGHT = 0.80
        C_WEIGHT = 0.20

        circadian_pressure = 1.0 - sleep_get_process_c()
        effective_s = process_s * 10/8 * S_WEIGHT  # above 0.8 is sleep deprivation
        raw = 1 - (effective_s + circadian_pressure * C_WEIGHT)

        # Caffeine partially masks felt sleep need — cosmetic only
        # The actual process_s is still accumulating underneath
        if caffeine_plasma_level > 0.0:
            mask = caffeine_get_effect() * 0.4  # max 40% suppression
            raw = max(0.0, raw + mask)

        return round(min(100.0, max(0.0, raw * 100)), 2)

    def go_to_sleep():
        global is_sleeping
        is_sleeping = True

    def wake_up(new_wake_hour=None, new_wake_minute=None):
        global is_sleeping, wake_time_in_minute, habitual_wake, circadian_phase
        is_sleeping = False
        # if new_wake_hour is not None and new_wake_minute is not None:
        #     # Entrainment: actual wake time pulls habitual wake slowly
        #     # ~15 min of phase shift per day maximum (realistic limit)
        #     wake_time_in_minute = new_wake_hour * 60 + new_wake_minute
        #     delta = wake_time_in_minute - habitual_wake
        #     delta = max(-15, min(15, delta))   # clamp to ±15 min
        #     habitual_wake   += delta * 0.3
        #     circadian_phase  = habitual_wake - 7.0*60  # offset from "standard" 7am

    def sleep_get_state():
        a = sleep_get_alertness()
        if   a >= 0.6:  return "peak"
        elif a >= 0.3:  return "normal"
        elif a >= 0.0:  return "fatigued"
        elif a >= -0.3: return "exhausted"
        else:           return "crashed"

    def sleep_stat_multiplier():
        return {
            "peak":      1.25,
            "normal":    1.00,
            "fatigued":  0.70,
            "exhausted": 0.40,
            "crashed":   0.15,
        }[sleep_get_state()]

    # def mood_modifier():
    #     """Per-minute valence delta, stat-scale (0–100)."""
    #     return {
    #         "peak":      +0.03,
    #         "normal":     0.00,
    #         "fatigued":  -0.02,
    #         "exhausted": -0.05,
    #         "crashed":   -0.10,
    #     }[sleep_get_state()]

    # def action_penalty():
    #     """Flat penalty to effective stat on skill checks (0–100 scale)."""
    #     return {
    #         "peak":       0,
    #         "normal":     0,
    #         "fatigued":  -5,
    #         "exhausted": -15,
    #         "crashed":   -30,
    #     }[sleep_get_state()]