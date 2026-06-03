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
    K_ELIM = math.log(2) / 300      # per minute

    # --------------------------------------------------
    # Call this every in-game minute
    # --------------------------------------------------
    def caffeine_advance_minute():
        global caffeine_minutes_since_dose
        _absorb()
        _eliminate()
        _update_tolerance()
        caffeine_minutes_since_dose += 1

    def _absorb():
        global caffeine_gut_level, caffeine_plasma_level
        """Gut → plasma: first-order absorption."""
        if caffeine_gut_level > 0:
            absorbed = caffeine_gut_level * (1.0 / ABSORPTION_MINUTES)
            caffeine_gut_level    = max(0.0, caffeine_gut_level - absorbed)
            caffeine_plasma_level = min(1.0, caffeine_plasma_level + absorbed)

    def _eliminate():
        """Plasma → eliminated: exponential decay by half-life."""
        global caffeine_plasma_level
        caffeine_plasma_level *= (1.0 - K_ELIM)
        caffeine_plasma_level  = max(0.0, caffeine_plasma_level)

    def _update_tolerance():
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
    def consume(self, dose_strength=0.4):
        self.gut_level = min(1.0, self.gut_level + dose_strength)
        self.tolerance = min(
            self.MAX_TOLERANCE,
            self.tolerance + self.TOLERANCE_BUILD * dose_strength
        )
        self.minutes_since_dose = 0

    # --------------------------------------------------
    # The alertness boost — what gets added to the main formula
    # Tolerance reduces the effective boost
    # --------------------------------------------------
    def get_effect(self):
        effective = self.plasma_level * (1.0 - self.tolerance)
        return min(self.MAX_EFFECT, effective)

    # --------------------------------------------------
    # Sleep disruption — how much caffeine degrades sleep quality
    # Pass this into TwoProcessSleep to slow S_FALL_RATE during sleep
    # --------------------------------------------------
    def sleep_disruption(self):
        if self.plasma_level < self.SLEEP_THRESHOLD:
            return 0.0
        # Scales from 0 → 1 as plasma_level goes from threshold → 1.0
        return (self.plasma_level - self.SLEEP_THRESHOLD) / (1.0 - self.SLEEP_THRESHOLD)

    # --------------------------------------------------
    # State labels for UI / narrative triggers
    # --------------------------------------------------
    def get_state(self):
        effect = self.get_effect()
        if effect >= 0.30:
            return "caffeinated"
        elif effect >= 0.10:
            return "mild_buzz"
        elif self.plasma_level > 0.05 and effect < 0.08:
            return "tolerant"   # caffeine present but not working
        else:
            return "none"

    def is_crashing(self, sleep_system):
        """
        True when caffeine just wore off AND underlying fatigue is high.
        This is the 'caffeine crash' — suddenly feeling the accumulated S.
        """
        return (
            self.plasma_level < 0.10 and
            self.minutes_since_dose < 120 and
            sleep_system.process_s > 0.65
        )