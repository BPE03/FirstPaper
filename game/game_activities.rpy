define interrupted = False

define activities = {
    "thesis": {
        "name": "Work on thesis",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "cari_jurnal": {
        "name": "Search for academic papers",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 240
    },
    "olahraga": {
        "name": "Olahraga",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "advisor": {
        "name": "Meet with advisor",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "socialize": {
        "name": "Socialize with friends",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "nap": {
        "name": "Take a nap",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "sleep": {
        "name": "Sleep",
        "min_duration": 240,
        "default_duration_hours": 8,
        "default_duration_minutes": 0,
        "max_duration": 600
    },
    "workshop": {
        "name": "Attend a workshop",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "selflearn": {
        "name": "Practice self-directed learning",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "rest": {
        "name": "Just rest and do nothing",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "skip": {
        "name": "Skip time",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 144000
    },
    "makan_bergizi": {
        "name": "Makan Bergizi",
        "min_duration": 20,
        "default_duration_hours": 0,
        "default_duration_minutes": 20,
        "max_duration": 20
    },
    "makan_enak": {
        "name": "Makan Enak Sembarangan",
        "min_duration": 20,
        "default_duration_hours": 0,
        "default_duration_minutes": 20,
        "max_duration": 20
    },
    "minum_kopi": {
        "name": "Minum Kopi",
        "min_duration": 15,
        "default_duration_hours": 0,
        "default_duration_minutes": 15,
        "max_duration": 15
    }
}

init python:
    def _activity_makan_bergizi():
        store.nutrition = min(store.max_stat, store.nutrition + 50/20)
        store.valence = max(0, store.valence - 6/60)

    def _activity_makan_enak():
        store.nutrition = min(store.max_stat, store.nutrition + 50/20)
        store.valence = min(store.max_stat, store.valence + 40/20)
        store.autonomy = min(store.max_stat, store.autonomy + 10/20)
        store.physical_activity = max(0, store.physical_activity - 6/60)

    def _activity_minum_kopi():
        store.caffeine_level = min(100, store.caffeine_level + 20/15)
        store.arousal = min(store.max_stat, store.arousal + 25/15)

    def _activity_olahraga():
        store.physical_activity = min(store.max_stat, store.physical_activity + 30/60)
        store.arousal = min(store.max_stat, store.arousal + 15/60)

    def _activity_advisor():
        store.competence = min(store.max_stat, store.competence + 10/60)
        store.relatedness = min(store.max_stat, store.relatedness + 20/60)
        store.valence = min(store.max_stat, store.valence + 15/60)
        store.arousal = min(store.max_stat, store.arousal + 10/60)
        store.writing_xp += 10
        store.practical_xp += 5

    def _activity_socialize():
        store.relatedness = min(store.max_stat, store.relatedness + 30/60)
        store.valence = min(store.max_stat, store.valence + 20/60)

    def _activity_nap():
        store.arousal = min(store.max_stat, store.arousal + 25/60)
        store.valence = min(store.max_stat, store.valence + 10/60)  # normalized from flat +10

    def _activity_workshop():
        store.practical_xp += 15/20
        store.writing_xp += 10/20
        store.competence = min(store.max_stat, store.competence + 60/60)
        store.arousal = max(0, store.arousal - 10/60)

    def _activity_selflearn():
        store.autonomy = min(store.max_stat, store.autonomy + 20/60)
        store.writing_xp += 8/20

    def _activity_cari_jurnal():
        store.writing_xp += 20/60
        store.competence = min(store.max_stat, store.competence + 15/60)
        store.nutrition = max(0, store.nutrition - 5/60)

    def _activity_rest():
        store.arousal = min(store.max_stat, store.arousal + 10/60)
        store.valence = min(store.max_stat, store.valence + 5/60)

    ACTIVITY_DISPATCH = {
        "makan_bergizi":  _activity_makan_bergizi,
        "makan_enak":     _activity_makan_enak,
        "minum_kopi":     _activity_minum_kopi,
        "olahraga":       _activity_olahraga,
        "advisor":        _activity_advisor,
        "socialize":      _activity_socialize,
        "nap":            _activity_nap,
        "workshop":       _activity_workshop,
        "selflearn":      _activity_selflearn,
        "rest":           _activity_rest,
        "cari_jurnal":    _activity_cari_jurnal,
    }