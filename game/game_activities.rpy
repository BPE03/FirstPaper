define interrupted = False

define activities = {
    "skripsi": {
        "name": "Kerjakan skripsi",
        "min_duration": 60,
        "default_duration_hours": 4,
        "default_duration_minutes": 0,
        "max_duration": 240
    },
    "cari_jurnal": {
        "name": "Cari dan baca jurnal",
        "min_duration": 60,
        "default_duration_hours": 4,
        "default_duration_minutes": 0,
        "max_duration": 240
    },
    "olahraga": {
        "name": "Olahraga",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 30,
        "max_duration": 240
    },
    "bimbingan": {
        "name": "Bimbingan dengan dosen",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 60
    },
    "sosialisasi": {
        "name": "Sosialisasi dengan teman",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 360
    },
    "nap": {
        "name": "Take a nap",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440
    },
    "tidur": {
        "name": "Tidur",
        "min_duration": 240,
        "default_duration_hours": 8,
        "default_duration_minutes": 0,
        "max_duration": 600
    },
    "workshop": {
        "name": "Attend a workshop",
        "min_duration": 120,
        "default_duration_hours": 2,
        "default_duration_minutes": 0,
        "max_duration": 120
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
    "chat_online": {
        "name": "Chat Online dengan Teman",
        "min_duration": 60,
        "default_duration_hours": 3,
        "default_duration_minutes": 0,
        "max_duration": 360
    },
    "main_game": {
        "name": "Main Game",
        "min_duration": 60,
        "default_duration_hours": 2,
        "default_duration_minutes": 0,
        "max_duration": 360
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
    def _activity_skripsi():
        store.autonomy = min(store.max_stat, store.autonomy - 10/60)
        store.competence = min(store.max_stat, store.competence - 10/60)
        relatedness_modifier = store.relatedness * 0.02
        store.relatedness = max(0, store.relatedness - relatedness_modifier/60)
        pa_modifier = store.physical_activity * 0.05
        store.physical_activity = max(0, store.physical_activity - pa_modifier/60)
        store.arousal = max(0, store.arousal - 6/60)
        store.valence = max(0, store.valence - 6/60)
        store.writing_xp += 20/60

    def _activity_makan_bergizi():
        store.nutrition = min(store.max_stat, store.nutrition + 70/20)
        store.autonomy = max(0, store.autonomy - 0.35/60)
        store.valence = max(0, store.valence - 6/20)

    def _activity_makan_enak():
        store.nutrition = min(store.max_stat, store.nutrition + 60/20)
        store.valence = min(store.max_stat, store.valence + 40/20)
        store.autonomy = min(store.max_stat, store.autonomy + 40/60)
        store.physical_activity = max(0, store.physical_activity - 2/20)
        store.sleep = max(0, store.sleep - 4/20)

    def _activity_minum_kopi():
        store.caffeine_level = min(100, store.caffeine_level + 20/15)
        store.arousal = min(store.max_stat, store.arousal + 25/15)

    def _activity_olahraga():
        store.physical_activity = min(store.max_stat, store.physical_activity + 30/60)
        store.competence = min(store.max_stat, store.competence + 2/60)

        nutrition_modifier = store.nutrition * 0.2
        store.nutrition = max(0, store.nutrition - nutrition_modifier / 60)
        store.arousal = min(store.max_stat, store.arousal + 15/60)

    def _activity_bimbingan():
        store.competence = min(store.max_stat, store.competence + 10/60)
        store.relatedness = min(store.max_stat, store.relatedness + 20/60)
        store.valence = min(store.max_stat, store.valence + 15/60)
        store.arousal = min(store.max_stat, store.arousal + 10/60)
        store.writing_xp += 10/60
        store.practical_xp += 5/60

    def _activity_sosialisasi():
        store.autonomy = min(store.max_stat, store.autonomy + 8/60)
        store.relatedness = min(store.max_stat, store.relatedness + 20/60)
        store.competence = min(store.max_stat, store.competence + 1/60)
        store.valence = min(store.max_stat, store.valence + 20/60)

    def _activity_nap():
        store.arousal = min(store.max_stat, store.arousal + 25/60)
        store.valence = min(store.max_stat, store.valence + 10/60)  # normalized from flat +10

    def _activity_workshop():
        store.practical_xp += 15/60
        store.writing_xp += 10/60
        store.competence = min(store.max_stat, store.competence + 60/60)
        store.arousal = max(0, store.arousal - 10/60)

    def _activity_selflearn():
        store.autonomy = min(store.max_stat, store.autonomy + 20/60)
        store.writing_xp += 8/60

    def _activity_cari_jurnal():
        store.writing_xp += 20/60
        store.autonomy = min(store.max_stat, store.autonomy - 10/60)
        store.competence = min(store.max_stat, store.competence - 10/60)
        relatedness_modifier = store.relatedness * 0.02
        store.relatedness = max(0, store.relatedness - relatedness_modifier/60)
        pa_modifier = store.physical_activity * 0.05
        store.physical_activity = max(0, store.physical_activity - pa_modifier/60)
        store.arousal = max(0, store.arousal - 6/60)
        store.valence = max(0, store.valence - 6/60)

    def _activity_rest():
        store.arousal = min(store.max_stat, store.arousal + 10/60)
        store.valence = min(store.max_stat, store.valence + 5/60)

    def _activity_chat_online():
        store.autonomy = min(store.max_stat, store.autonomy + 6.5/60)
        store.relatedness = min(store.max_stat, store.relatedness + 4/60)
        pa_modifier = store.physical_activity * 0.05
        store.physical_activity = max(0, store.physical_activity - pa_modifier/60)
        store.valence = min(store.max_stat, store.valence + 10/60)

    def _activity_main_game():
        store.autonomy = min(store.max_stat, store.autonomy + 5/60)
        store.competence = min(store.max_stat, store.competence + 10/60)
        store.relatedness = min(store.max_stat, store.relatedness + 10/60)
        store.physical_activity = max(0, store.physical_activity - 5/60)
        store.valence = min(store.max_stat, store.valence + 15/60)

    ACTIVITY_DISPATCH = {
        "skripsi":        _activity_skripsi,
        "makan_bergizi":  _activity_makan_bergizi,
        "makan_enak":     _activity_makan_enak,
        "minum_kopi":     _activity_minum_kopi,
        "olahraga":       _activity_olahraga,
        "bimbingan":      _activity_bimbingan,
        "sosialisasi":    _activity_sosialisasi,
        "nap":            _activity_nap,
        "workshop":       _activity_workshop,
        "selflearn":      _activity_selflearn,
        "rest":           _activity_rest,
        "cari_jurnal":    _activity_cari_jurnal,
        "chat_online":    _activity_chat_online,
        "main_game":      _activity_main_game,
    }