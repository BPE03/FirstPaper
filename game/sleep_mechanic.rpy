default process_s           = 0.15
default wake_time_in_minute = current_hour * 60 + current_minute
default total_daily_time    = current_hour * 60 + current_minute
default is_sleeping         = False

init python:
    import math
    S_RISE_RATE = 0.022 / 60    # per minute, awake
    S_FALL_RATE = 0.045 / 60    # per minute, asleep
    S_MIN       = 0.05
    S_MAX       = 1.0

    C_AMPLITUDE = 0.45
    C_OFFSET    = 0.50

    def sleep_advance_minute(minutes=1):
        for _ in range(minutes):
            if is_sleeping:
                sleep_decay_s()
            else:
                sleep_build_s()
            total_daily_time = (total_daily_time + 1) % 1440

    def sleep_build_s():
        process_s += S_RISE_RATE * (S_MAX - process_s)
        process_s = min(process_s, S_MAX)

    def sleep_decay_s():
        process_s -= S_FALL_RATE * (process_s - S_MIN)
        process_s = max(process_s, S_MIN)

    def sleep_get_process_c():
        wake_time_in_minute = (total_daily_time - wake_time_in_minute) % 1440
        phase = (wake_time_in_minute / 1440.0) * 2 * math.pi
        c = C_OFFSET + C_AMPLITUDE * math.sin(phase - math.pi * 0.25)
        return max(0.0, min(1.0, c))

    def sleep_get_alertness():
        return max(-1.0, min(1.0, sleep_get_process_c() - process_s))

    def go_to_sleep():
        is_sleeping = True

    def wake_up(new_wake_hour=None, new_wake_minute=None):
        is_sleeping = False
        if new_wake_hour is not None and new_wake_minute is not None:
            wake_time_in_minute = new_wake_hour * 60 + new_wake_minute

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
        }[get_state()]

    # def mood_modifier():
    #     """Per-minute valence delta, stat-scale (0–100)."""
    #     return {
    #         "peak":      +0.03,
    #         "normal":     0.00,
    #         "fatigued":  -0.02,
    #         "exhausted": -0.05,
    #         "crashed":   -0.10,
    #     }[get_state()]

    # def action_penalty():
    #     """Flat penalty to effective stat on skill checks (0–100 scale)."""
    #     return {
    #         "peak":       0,
    #         "normal":     0,
    #         "fatigued":  -5,
    #         "exhausted": -15,
    #         "crashed":   -30,
    #     }[get_state()]