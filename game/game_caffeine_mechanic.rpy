default caffeine_plasma_level   = 0.0   # current caffeine in system (0–1)
default caffeine_gut_level      = 0.0   # caffeine being absorbed
default caffeine_tolerance      = 0.0   # 0 = naive, 1 = fully tolerant
default caffeine_minutes_since_dose = 9999

init python:
    import math
    """
    Caffeine pharmacokinetics for Ren'Py life-sim.
    
    Based on: half-life ~5 hours, peak effect ~30-45 min after intake.
    Modeled as a two-compartment system: absorption + elimination.
    Time unit: minutes.
    """

    HALF_LIFE_MINUTES   = 300       # ~5 hours (literature range: 3–7 hrs)
    ABSORPTION_MINUTES  = 45        # time to peak effect
    MAX_EFFECT          = 0.45      # ceiling on alertness boost (0–1 scale)
    SLEEP_THRESHOLD     = 0.10      # caffeine level above which sleep quality degrades

    # Tolerance
    TOLERANCE_BUILD     = 0.08      # per dose
    TOLERANCE_DECAY     = 0.0003    # per minute without caffeine (slow reset)
    MAX_TOLERANCE       = 0.80      # hard ceiling

    # Elimination rate constant (derived from half-life)
    # k = ln(2) / half_life
    K_ELIM = math.log(2) / HALF_LIFE_MINUTES      # per minute

    # --------------------------------------------------
    # Call this every in-game minute
    # --------------------------------------------------
    def caffeine_advance_minute():
        global caffeine_minutes_since_dose
        caffeine_absorb()
        caffeine_eliminate()
        caffeine_update_tolerance()
        caffeine_minutes_since_dose += 1

    def caffeine_absorb():
        global caffeine_gut_level, caffeine_plasma_level
        """Gut → plasma: first-order absorption."""
        if caffeine_gut_level > 0:
            absorbed = caffeine_gut_level * (1.0 / ABSORPTION_MINUTES)
            caffeine_gut_level    = max(0.0, caffeine_gut_level - absorbed)
            caffeine_plasma_level = min(1.0, caffeine_plasma_level + absorbed)

    def caffeine_eliminate():
        """Plasma → eliminated: exponential decay by half-life."""
        global caffeine_plasma_level
        caffeine_plasma_level *= (1.0 - K_ELIM)
        caffeine_plasma_level  = max(0.0, caffeine_plasma_level)

    def caffeine_update_tolerance():
        global caffeine_tolerance
        if caffeine_plasma_level > 0.05:
            # Tolerance builds while caffeine is active
            pass  # handled at dose time
        else:
            # Tolerance slowly decays without caffeine
            caffeine_tolerance = max(0.0, caffeine_tolerance - TOLERANCE_DECAY)

    # --------------------------------------------------
    # Player drinks coffee
    # dose_strength: 0.2 = weak tea, 0.4 = coffee, 0.7 = espresso shot
    # --------------------------------------------------
    def caffeine_consume(dose_strength=0.4):
        global caffeine_gut_level, caffeine_tolerance, caffeine_minutes_since_dose
        caffeine_gut_level = min(1.0, caffeine_gut_level + dose_strength)
        caffeine_tolerance = min(
            MAX_TOLERANCE,
            caffeine_tolerance + TOLERANCE_BUILD * dose_strength
        )
        caffeine_minutes_since_dose = 0

    # --------------------------------------------------
    # The alertness boost — what gets added to the main formula
    # Tolerance reduces the effective boost
    # --------------------------------------------------
    def caffeine_get_effect():
        global caffeine_plasma_level, caffeine_tolerance
        effective = caffeine_plasma_level * (1.0 - caffeine_tolerance)
        return min(MAX_EFFECT, effective)

    # --------------------------------------------------
    # Sleep disruption — how much caffeine degrades sleep quality
    # Pass this into TwoProcessSleep to slow S_FALL_RATE during sleep
    # --------------------------------------------------
    def caffeine_sleep_disruption():
        global caffeine_plasma_level
        if caffeine_plasma_level < SLEEP_THRESHOLD:
            return 0.0
        # Scales from 0 → 1 as plasma_level goes from threshold → 1.0
        return (caffeine_plasma_level - SLEEP_THRESHOLD) / (1.0 - SLEEP_THRESHOLD)

    # --------------------------------------------------
    # State labels for UI / narrative triggers
    # --------------------------------------------------
    def caffeine_get_state():
        effect = caffeine_get_effect()
        if effect >= 0.30:
            return "caffeinated"
        elif effect >= 0.10:
            return "mild_buzz"
        elif caffeine_plasma_level > 0.05 and effect < 0.08:
            return "tolerant"   # caffeine present but not working
        else:
            return "none"

    def caffeine_is_crashing():
        """
        True when caffeine just wore off AND underlying fatigue is high.
        This is the 'caffeine crash' — suddenly feeling the accumulated S.
        """
        return (
            caffeine_plasma_level < 0.10 and
            caffeine_minutes_since_dose < 120 and
            process_s > 0.65
        )