default interrupted = False
default booked_bimbingan = False
default bimbingan_day = 0
default bimbingan_month = 0
default bimbingan_year = 0

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
    "olahraga_ringan": {
        "name": "Olahraga ringan",
        "min_duration": 60,
        "default_duration_hours": 2,
        "default_duration_minutes": 0,
        "max_duration": 240
    },
    "olahraga_sedang": {
        "name": "Olahraga Sedang",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 30,
        "max_duration": 240
    },
    "olahraga_berat": {
        "name": "Olahraga Berat",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
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
    "belajar_mandiri": {
        "name": "Belajar dan Praktek secara mandiri",
        "min_duration": 60,
        "default_duration_hours": 4,
        "default_duration_minutes": 0,
        "max_duration": 240
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
        calculate_writing_xp(20/60)

    def _activity_makan_bergizi():
        store.nutrition = min(store.max_stat, store.nutrition + 70/20)
        store.autonomy = max(0, store.autonomy - 35/60)
        store.valence = max(0, store.valence - 6/20)

    def _activity_makan_enak():
        store.nutrition = min(store.max_stat, store.nutrition + 60/20)
        store.valence = min(store.max_stat, store.valence + 40/20)
        store.autonomy = min(store.max_stat, store.autonomy + 40/60)
        store.physical_activity = max(0, store.physical_activity - 4/20)
        store.sleep = max(0, store.sleep - 4/20)

    def _activity_minum_kopi():
        store.caffeine_level = min(100, store.caffeine_level + 20/15)
        store.arousal = min(store.max_stat, store.arousal + 25/15)

    def _activity_olahraga_ringan():
        store.autonomy = min(store.max_stat, store.autonomy + 3/60)
        store.physical_activity = min(store.max_stat, store.physical_activity + 8/60)
        nutrition_modifier = store.nutrition * 0.18
        store.nutrition = max(0, store.nutrition - nutrition_modifier / 60)

    def _activity_olahraga_sedang():
        store.physical_activity = min(store.max_stat, store.physical_activity + 30/60)
        store.competence = min(store.max_stat, store.competence + 2/60)

        nutrition_modifier = store.nutrition * 0.2
        store.nutrition = max(0, store.nutrition - nutrition_modifier / 60)
        store.arousal = min(store.max_stat, store.arousal + 15/60)

    def _activity_olahraga_berat():
        store.autonomy = max(0, store.autonomy - 6/60)
        store.physical_activity = min(store.max_stat, store.physical_activity + 50/60)
        store.competence = max(0, store.competence - 1/60)
        nutrition_modifier = store.nutrition * 0.27
        store.nutrition = max(0, store.nutrition - nutrition_modifier / 60)
        store.arousal = min(store.max_stat, store.arousal + 25/60)

    def _activity_bimbingan():
        store.competence = min(store.max_stat, store.competence + 10/60)
        store.relatedness = min(store.max_stat, store.relatedness + 20/60)
        store.valence = min(store.max_stat, store.valence + 15/60)
        store.arousal = min(store.max_stat, store.arousal + 10/60)
        calculate_writing_xp(10/60)
        calculate_practical_xp(5/60)

    def _activity_sosialisasi():
        store.autonomy = min(store.max_stat, store.autonomy + 8/60)
        store.relatedness = min(store.max_stat, store.relatedness + 20/60)
        store.competence = min(store.max_stat, store.competence + 1/60)
        store.valence = min(store.max_stat, store.valence + 20/60)

    def _activity_nap():
        store.arousal = min(store.max_stat, store.arousal + 25/60)
        store.valence = min(store.max_stat, store.valence + 10/60)  # normalized from flat +10

    def _activity_workshop():
        calculate_practical_xp(15/60)
        calculate_writing_xp(10/60)
        store.competence = min(store.max_stat, store.competence + 60/60)
        store.arousal = max(0, store.arousal - 10/60)

    def _activity_belajar_mandiri():
        store.autonomy = min(store.max_stat, store.autonomy - 10/60)
        store.competence = min(store.max_stat, store.competence + 5/60)
        relatedness_modifier = store.relatedness * 0.02
        store.relatedness = max(0, store.relatedness - relatedness_modifier/60)
        pa_modifier = store.physical_activity * 0.05
        store.physical_activity = max(0, store.physical_activity - pa_modifier/60)
        store.arousal = max(0, store.arousal - 6/60)
        store.valence = max(0, store.valence - 6/60)
        calculate_practical_xp(20/60)

    def _activity_cari_jurnal():
        calculate_writing_xp(20/60)
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
        store.arousal = min(store.max_stat, store.arousal + 5/60)

    def _activity_main_game():
        store.autonomy = min(store.max_stat, store.autonomy + 5/60)
        store.competence = min(store.max_stat, store.competence + 10/60)
        store.relatedness = min(store.max_stat, store.relatedness + 10/60)
        store.physical_activity = max(0, store.physical_activity - 5/60)
        store.valence = min(store.max_stat, store.valence + 15/60)
        store.arousal = min(store.max_stat, store.arousal + 15/60)

    ACTIVITY_DISPATCH = {
        "skripsi":        _activity_skripsi,
        "makan_bergizi":  _activity_makan_bergizi,
        "makan_enak":     _activity_makan_enak,
        "minum_kopi":     _activity_minum_kopi,
        "olahraga_ringan":  _activity_olahraga_ringan,
        "olahraga_sedang":  _activity_olahraga_sedang,
        "olahraga_berat":   _activity_olahraga_berat,
        "bimbingan":      _activity_bimbingan,
        "sosialisasi":    _activity_sosialisasi,
        "nap":            _activity_nap,
        "workshop":       _activity_workshop,
        "belajar_mandiri":      _activity_belajar_mandiri,
        "rest":           _activity_rest,
        "cari_jurnal":    _activity_cari_jurnal,
        "chat_online":    _activity_chat_online,
        "main_game":      _activity_main_game,
    }

    ACTIVITY_MOTIVATION_CURVES = {
        "skripsi": {
            "autonomy":    [(0.0, -0.4), (75, 0.0)],
            "competence":  [(0.0, -0.4), (75, 0.0)],
            "relatedness": [(0.0, -0.4), (75, 0.0)],
            "physical_activity":          [(0.0, -0.4), (75, 0.0)],
            "nutrition":   [(30, -1.0), (60,  0.0)],
            "sleep":       [(30, -1.0), (60,  0.0)],
        },
        "sosialisasi": {
            "relatedness": [(0.0, 0.5), (100, -0.2)],
        },
        "makan_bergizi": {
            "autonomy":    [(0.0, 0.1), (50, 0.0)],
            "competence":   [(0.0, 0.1), (50, 0.0)],
            "relatedness":  [(0.0, 0.1), (50, 0.0)],
            "nutrition":    [(50, 1), (60, 0.0), (80, -1)],
            "physical_activity":          [(0.0, 0.1), (50, 0.0)],
            "sleep":       [(0.0, 0.2), (30, 0.0)],
        },
        "makan_enak": {
            "autonomy":    [(0.0, 0.2), (50, 0.0)],
            "competence":   [(0.0, 0.2), (50, 0.0)],
            "relatedness":  [(0.0, 0.2), (50, 0.0)],
            "nutrition":    [(50, 1), (60, 0.0), (100, -0.6)],
            "physical_activity":          [(0.0, 0.2), (50, 0.0)],
            "sleep":       [(0.0, 0.4), (30, 0.0)],
        },
        "minum_kopi": {
            "caffeine_level": [(0, 1), (100, 0.0)],
        },
        "olahraga_ringan": {
            "physical_activity":          [(0.0, 0.5), (50, 0.0), (80, 0), (100, -0.5)],
        },
        "olahraga_sedang": {
            "physical_activity":          [(0.0, -0.35), (50, 0.0), (80, 0), (100, -0.5)],
        },
        "olahraga_berat": {
            "physical_activity":          [(0.0, -0.7), (50, 0.0), (80, 0), (100, -0.7)],
        },
        # "bimbingan":      _activity_bimbingan,
        # "nap":            _activity_nap,
        # "workshop":       _activity_workshop,
        "belajar_mandiri": {
            "autonomy":    [(0.0, -0.4), (75, 0.0)],
            "competence":  [(0.0, -0.4), (75, 0.0)],
            "relatedness": [(0.0, -0.4), (75, 0.0)],
            "physical_activity":          [(0.0, -0.4), (75, 0.0)],
            "nutrition":   [(30, -1.0), (60,  0.0)],
            "sleep":       [(30, -1.0), (60,  0.0)],
        },
        #"rest":           _activity_rest,
        "cari_jurnal": {
            "autonomy":    [(0.0, -0.4), (75, 0.0)],
            "competence":  [(0.0, -0.4), (75, 0.0)],
            "relatedness": [(0.0, -0.4), (75, 0.0)],
            "physical_activity":          [(0.0, -0.4), (75, 0.0)],
            "nutrition":   [(30, -1.0), (60,  0.0)],
            "sleep":       [(30, -1.0), (60,  0.0)],
        },
        "chat_online": {
            "autonomy":    [(0.0, 1), (70, 0.0)],
            "relatedness": [(0.0, 1), (70, 0.0)],
            "nutrition":   [(0, -0.5), (40,  0.0)],
            "sleep":       [(0, -0.5), (40,  0.0)],
        },
        "main_game": {
            "autonomy":    [(0.0, 0.7), (70, 0.0)],
            "competence":  [(0.0, 0.7), (70, 0.0)],
            "relatedness": [(0.0, 0.5), (30, 0.3)],
            "nutrition":   [(0, -2), (40,  0.0)],
            "sleep":       [(0, -1), (40,  0.0)],
        },
    }

    def get_activity_motivation(activity_name):
        stats = {
            "autonomy":    store.autonomy,
            "competence":  store.competence,
            "relatedness": store.relatedness,
            "nutrition":   store.nutrition,
            "physical_activity": store.physical_activity,
            "sleep":       store.sleep,
            "caffeine_level": store.caffeine_level,
        }
        base_motivation = store.motivation
        curves = ACTIVITY_MOTIVATION_CURVES.get(activity_name, {})
        if not curves:
            return 100
        total_modifier = 0.0
        for stat_name, points in curves.items():
            total_modifier += sample_curve(points, stats[stat_name])
        result = base_motivation + total_modifier
        return round(max(0.0, min(100, result)), 2)