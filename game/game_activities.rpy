default interrupted = False
default pending_jump = None
default appt_bimbingan_state = "unscheduled"
default appt_bimbingan_day   = 0
default appt_bimbingan_month = 0
default appt_bimbingan_year  = 0
default appt_workshop_state  = "unscheduled"
default appt_workshop_day    = 0
default appt_workshop_month  = 0
default appt_workshop_year   = 0
default bimbingan_last_thesis_progress = 0
default bimbingan_count = 0
default bimbingan_bonus_active = False
default bimbingan_bonus_start_progress = 0

define activities = {
    "skripsi": {
        "name": "Kerjakan skripsi",
        "min_duration": 60,
        "default_duration_hours": 4,
        "default_duration_minutes": 0,
        "max_duration": 240,
        "stats_affected_message": "Efek: Progress Skripsi {color=#4caf50}↑{/color}, XP Menulis {color=#4caf50}↑{/color}, Arousal {color=#4caf50}↑{/color}  |  Valence {color=#f44336}↓{/color}, Otonomi {color=#f44336}↓{/color}, Kompetensi {color=#f44336}↓{/color}"
    },
    "cari_jurnal": {
        "name": "Cari dan baca jurnal",
        "min_duration": 60,
        "default_duration_hours": 4,
        "default_duration_minutes": 0,
        "max_duration": 240,
        "stats_affected_message": "Efek: XP Menulis {color=#4caf50}↑{/color}, Arousal {color=#4caf50}↑{/color}  |  Valence {color=#f44336}↓{/color}, Otonomi {color=#f44336}↓{/color}, Kompetensi {color=#f44336}↓{/color}  |  (Peluang menemukan topik)"
    },
    "olahraga_ringan": {
        "name": "Olahraga ringan",
        "min_duration": 60,
        "default_duration_hours": 2,
        "default_duration_minutes": 0,
        "max_duration": 120,
        "completion_message": "Kamu olahraga ringan selama {minutes} menit. Kamu merasa lebih segar!",
        "stats_affected_message": "Efek: Aktivitas Fisik {color=#4caf50}↑{/color}, Otonomi {color=#4caf50}↑{/color}  |  Nutrisi {color=#f44336}↓{/color}"
    },
    "olahraga_sedang": {
        "name": "Olahraga Sedang",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 30,
        "max_duration": 120,
        "completion_message": "Kamu olahraga sedang selama {minutes} menit. Kamu merasa lebih segar!",
        "stats_affected_message": "Efek: Aktivitas Fisik {color=#4caf50}↑↑{/color}, Valence {color=#4caf50}↑{/color}, Arousal {color=#4caf50}↑{/color}, Kompetensi {color=#4caf50}↑{/color}  |  Nutrisi {color=#f44336}↓{/color}"
    },
    "olahraga_berat": {
        "name": "Olahraga Berat",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 120,
        "completion_message": "Kamu olahraga berat selama {minutes} menit. Kamu merasa lebih segar!",
        "stats_affected_message": "Efek: Aktivitas Fisik {color=#4caf50}↑↑↑{/color}, Valence {color=#4caf50}↑↑{/color}, Arousal {color=#4caf50}↑↑{/color}  |  Otonomi {color=#f44336}↓{/color}, Kompetensi {color=#f44336}↓{/color}, Nutrisi {color=#f44336}↓↓{/color}"
    },
    "bimbingan": {
        "name": "Bimbingan dengan dosen",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 60,
        "stats_affected_message": "Efek: Kompetensi {color=#4caf50}↑{/color}, Keterhubungan {color=#4caf50}↑{/color}, Valence {color=#4caf50}↑{/color}, Arousal {color=#4caf50}↑{/color}, XP Menulis {color=#4caf50}↑{/color}, XP Praktis {color=#4caf50}↑{/color}"
    },
    "sosialisasi": {
        "name": "Sosialisasi dengan teman",
        "min_duration": 60,
        "default_duration_hours": 3,
        "default_duration_minutes": 0,
        "max_duration": 360,
        "completion_message": "Kamu menghabiskan waktu dengan teman-teman untuk {minutes} menit. Kamu merasa terhubung dan bahagia!",
        "stats_affected_message": "Efek: Keterhubungan {color=#4caf50}↑↑{/color}, Valence {color=#4caf50}↑↑{/color}, Arousal {color=#4caf50}↑↑{/color}, Otonomi {color=#4caf50}↑{/color}, Kompetensi {color=#4caf50}↑{/color}"
    },
    "nap": {
        "name": "Take a nap",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440,
        "completion_message": "Kamu tidur siang selama {minutes} menit. Kamu merasa lebih waspada sekarang!",
        "stats_affected_message": "Efek: Arousal {color=#4caf50}↑{/color}, Valence {color=#4caf50}↑{/color}"
    },
    "tidur": {
        "name": "Tidur",
        "min_duration": 60,
        "default_duration_hours": 8,
        "default_duration_minutes": 0,
        "max_duration": 720,
        "completion_message": "Kamu tidur selama {minutes} menit.",
        "stats_affected_message": "Efek: Tidur {color=#4caf50}↑↑{/color}  |  memulihkan stamina harian"
    },
    "workshop": {
        "name": "Attend a workshop",
        "min_duration": 120,
        "default_duration_hours": 2,
        "default_duration_minutes": 0,
        "max_duration": 120,
        "completion_message": "Kamu menghadiri sebuah workshop selama {minutes} menit. Kemampuanmu meningkat!",
        "stats_affected_message": "Efek: XP Praktis {color=#4caf50}↑↑{/color}, XP Menulis {color=#4caf50}↑{/color}, Kompetensi {color=#4caf50}↑{/color}  |  Arousal {color=#f44336}↓{/color}"
    },
    "belajar_mandiri": {
        "name": "Belajar dan Praktek secara mandiri",
        "min_duration": 60,
        "default_duration_hours": 4,
        "default_duration_minutes": 0,
        "max_duration": 240,
        "completion_message": "Kamu belajar secara mandiri selama {minutes} menit. Kamu merasa lebih punya kendali!",
        "stats_affected_message": "Efek: XP Praktis {color=#4caf50}↑{/color}, Otonomi {color=#4caf50}↑{/color}, Kompetensi {color=#4caf50}↑{/color}  |  Valence {color=#f44336}↓{/color}"
    },
    "rest": {
        "name": "Just rest and do nothing",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 1440,
        "completion_message": "Kamu beristirahat selama {minutes} menit.",
        "stats_affected_message": "Efek: Arousal {color=#4caf50}↑{/color}, Valence {color=#4caf50}↑{/color}"
    },
    "prokrastinasi": {
        "name": "Skip time",
        "min_duration": 60,
        "default_duration_hours": 1,
        "default_duration_minutes": 0,
        "max_duration": 144000,
        "completion_message": "Kamu prokrastinasi selama {minutes} menit.",
        "stats_affected_message": "Efek: Otonomi {color=#4caf50}↑{/color}, Valence {color=#4caf50}↑{/color}, Arousal {color=#4caf50}↑{/color}"
    },
    "chat_online": {
        "name": "Chat Online dengan Teman",
        "min_duration": 60,
        "default_duration_hours": 3,
        "default_duration_minutes": 0,
        "max_duration": 360,
        "completion_message": "Kamu mengobrol dengan teman-teman secara online selama {minutes} menit. Kamu merasa lebih terhubung!",
        "stats_affected_message": "Efek: Keterhubungan {color=#4caf50}↑{/color}, Valence {color=#4caf50}↑{/color}, Arousal {color=#4caf50}↑{/color}, Otonomi {color=#4caf50}↑{/color}"
    },
    "main_game": {
        "name": "Main Game",
        "min_duration": 60,
        "default_duration_hours": 2,
        "default_duration_minutes": 0,
        "max_duration": 360,
        "completion_message": "Kamu bermain game selama {minutes} menit. Kamu merasa lebih santai dan terhibur!",
        "stats_affected_message": "Efek: Valence {color=#4caf50}↑↑{/color}, Arousal {color=#4caf50}↑↑{/color}, Otonomi {color=#4caf50}↑{/color}, Kompetensi {color=#4caf50}↑{/color}"
    },

    "makan_bergizi": {
        "name": "Makan Bergizi",
        "min_duration": 20,
        "default_duration_hours": 0,
        "default_duration_minutes": 20,
        "max_duration": 20,
        "completion_message": "Kamu makan makanan bergizi selama {minutes} menit. Nutrisimu meningkat!",
        "stats_affected_message": "Efek: Nutrisi {color=#4caf50}↑↑{/color}, Arousal {color=#4caf50}↑{/color}  |  Otonomi {color=#f44336}↓{/color}"
    },
    "makan_enak": {
        "name": "Makan Enak Sembarangan",
        "min_duration": 20,
        "default_duration_hours": 0,
        "default_duration_minutes": 20,
        "max_duration": 20,
        "completion_message": "Kamu menikmati makanan enak selama {minutes} menit. Mood kamu meningkat, namun kamu mendapatkan kalori lebih banyak.",
        "stats_affected_message": "Efek: Nutrisi {color=#4caf50}↑{/color}, Valence {color=#4caf50}↑{/color}, Otonomi {color=#4caf50}↑{/color}  |  Aktivitas Fisik {color=#f44336}↓{/color}"
    },
    "minum_kopi": {
        "name": "Minum Kopi",
        "min_duration": 15,
        "default_duration_hours": 0,
        "default_duration_minutes": 15,
        "max_duration": 15,
        "completion_message": "Kamu menikmati kopi selama {minutes} menit. Tingkat kafein dan kewaspadaan kamu meningkat!",
        "stats_affected_message": "Efek: Kafein {color=#4caf50}↑{/color}, Arousal {color=#4caf50}↑{/color}"
    },
    "meditasi": {
        "name": "Meditasi",
        "min_duration": 10,
        "default_duration_hours": 0,
        "default_duration_minutes": 10,
        "max_duration": 60,
        "completion_message": "Kamu bermeditasi selama {minutes} menit. Kamu merasa lebih tenang dan fokus!",
        "stats_affected_message": "Efek: Arousal {color=#f44336}↓↓{/color}"
    }
}

init python:
    def _activity_skripsi():
        global autonomy, competence, relatedness, physical_activity, arousal, valence
        autonomy = min(max_stat, autonomy - 10/60)
        competence = min(max_stat, competence - 10/60)
        relatedness_modifier = relatedness * 0.02
        relatedness = max(0, relatedness - relatedness_modifier/60)
        pa_modifier = physical_activity * 0.05
        physical_activity = max(0, physical_activity - pa_modifier/60)
        arousal = max(0, arousal + 6/60)
        valence = max(0, valence - 6/60)
        calculate_writing_xp(20/60)

    def _activity_makan_bergizi():
        global autonomy, nutrition, arousal
        nutrition = min(max_stat, nutrition + 70/20)
        autonomy = max(0, autonomy - 35/60)
        arousal = min(max_stat, arousal + 5/20)

    def _activity_makan_enak():
        global nutrition, valence, autonomy, physical_activity, process_s
        nutrition = min(max_stat, nutrition + 60/20)
        valence = min(max_stat, valence + 20/20)
        autonomy = min(max_stat, autonomy + 40/60)
        physical_activity = max(0, physical_activity - 4/20)
        process_s = min(S_MAX, process_s + 0.02/20)

    def _activity_minum_kopi():
        global arousal
        caffeine_consume(0.4/15)
        arousal = min(max_stat, arousal + 10/15)

    def _activity_olahraga_ringan():
        global autonomy, physical_activity, nutrition
        autonomy = min(max_stat, autonomy + 3/60)
        physical_activity = min(max_stat, physical_activity + 8/60)
        nutrition_modifier = nutrition * 0.18
        nutrition = max(0, nutrition - nutrition_modifier / 60)

    def _activity_olahraga_sedang():
        global physical_activity, competence, nutrition, valence, arousal
        physical_activity = min(max_stat, physical_activity + 30/60)
        competence = min(max_stat, competence + 2/60)

        nutrition_modifier = nutrition * 0.2
        nutrition = max(0, nutrition - nutrition_modifier / 60)
        valence = min(max_stat, valence + 20/60)
        arousal = min(max_stat, arousal + 15/60)

    def _activity_olahraga_berat():
        global autonomy, physical_activity, competence, nutrition, valence, arousal
        autonomy = max(0, autonomy - 6/60)
        physical_activity = min(max_stat, physical_activity + 50/60)
        competence = max(0, competence - 1/60)
        nutrition_modifier = nutrition * 0.27
        nutrition = max(0, nutrition - nutrition_modifier / 60)
        valence = min(max_stat, valence + 35/60)
        arousal = min(max_stat, arousal + 25/60)

    def _activity_bimbingan():
        global competence, relatedness, valence, arousal
        competence = min(max_stat, competence + 10/60)
        relatedness = min(max_stat, relatedness + 20/60)
        valence = min(max_stat, valence + 15/60)
        arousal = min(max_stat, arousal + 10/60)
        calculate_writing_xp(40/60)
        calculate_practical_xp(20/60)

    # def _activity_nap():
    #     global arousal, valence
    #     arousal = min(max_stat, arousal + 25/60)
    #     valence = min(max_stat, valence + 10/60)

    def _activity_workshop():
        global competence, arousal
        calculate_practical_xp(40/60)
        calculate_writing_xp(10/60)
        competence = min(max_stat, competence + 20/60)
        arousal = max(0, arousal - 10/60)

    def _activity_belajar_mandiri():
        global autonomy, competence, relatedness, physical_activity, arousal, valence
        autonomy = min(max_stat, autonomy + 10/60)
        competence = min(max_stat, competence + 5/60)
        relatedness_modifier = relatedness * 0.02
        relatedness = max(0, relatedness - relatedness_modifier/60)
        pa_modifier = physical_activity * 0.05
        physical_activity = max(0, physical_activity - pa_modifier/60)
        #arousal = max(0, arousal + 6/60)
        valence = max(0, valence - 6/60)
        calculate_practical_xp(20/60)

    def _activity_cari_jurnal():
        global autonomy, competence, relatedness, physical_activity, arousal, valence
        calculate_writing_xp(20/60)
        autonomy = min(max_stat, autonomy - 10/60)
        competence = min(max_stat, competence - 10/60)
        relatedness_modifier = relatedness * 0.02
        relatedness = max(0, relatedness - relatedness_modifier/60)
        pa_modifier = physical_activity * 0.05
        physical_activity = max(0, physical_activity - pa_modifier/60)
        arousal = max(0, arousal + 6/60)
        valence = max(0, valence - 6/60)

    # def _activity_rest():
    #     global arousal, valence
    #     arousal = min(max_stat, arousal + 10/60)
    #     valence = min(max_stat, valence + 5/60)

    def _activity_chat_online():
        global autonomy, relatedness, physical_activity, valence, arousal
        autonomy = min(max_stat, autonomy + 6.5/60)
        relatedness = min(max_stat, relatedness + 4/60)
        pa_modifier = physical_activity * 0.05
        physical_activity = max(0, physical_activity - pa_modifier/60)
        valence = min(max_stat, valence + 10/60)
        arousal = min(max_stat, arousal + 5/60)

    def _activity_sosialisasi():
        global autonomy, relatedness, competence, valence, arousal
        autonomy = min(max_stat, autonomy + 8/60)
        relatedness = min(max_stat, relatedness + 20/60)
        competence = min(max_stat, competence + 1/60)
        valence = min(max_stat, valence + 20/60)
        arousal = min(max_stat, arousal + 15/60)

    def _activity_main_game():
        global autonomy, competence, relatedness, physical_activity, arousal, valence
        autonomy = min(max_stat, autonomy + 5/60)
        competence = min(max_stat, competence + 10/60)
        relatedness = min(max_stat, relatedness + 1/60)
        physical_activity = max(0, physical_activity - 5/60)
        valence = min(max_stat, valence + 15/60)
        arousal = min(max_stat, arousal + 10/60)

    def _activity_meditasi():
        global arousal
        arousal = max(0, arousal - 15/10)

    def _activity_prokrastinasi():
        global valence, arousal, autonomy
        autonomy = min(max_stat, autonomy + 5/60)
        valence = min(max_stat, valence + 10/60)
        arousal = min(max_stat, arousal + 10/60)

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
        # "nap":            _activity_nap,
        "workshop":       _activity_workshop,
        "belajar_mandiri":      _activity_belajar_mandiri,
        # "rest":           _activity_rest,
        "cari_jurnal":    _activity_cari_jurnal,
        "chat_online":    _activity_chat_online,
        "main_game":      _activity_main_game,
        "meditasi":      _activity_meditasi,
        "prokrastinasi":  _activity_prokrastinasi
    }

    ACTIVITY_MOTIVATION_CURVES = {
        "skripsi": {
            "autonomy":    [(0.0, -0.4), (75, 0.0)],
            "competence":  [(0.0, -0.4), (75, 0.0)],
            "relatedness": [(0.0, -0.4), (75, 0.0)],
            "physical_activity":          [(0.0, -0.4), (75, 0.0)],
            "nutrition":   [(20, -1.0), (50,  0.0)],
            "sleep":       [(0, -1.0), (30,  0.0)],
        },
        "belajar_mandiri": {
            "autonomy":    [(0.0, 0.4), (75, 0.0)],
            "competence":  [(0.0, 0.4), (75, 0.0)],
            "relatedness": [(0.0, -0.4), (75, 0.0)],
            "physical_activity":          [(0.0, -0.4), (75, 0.0)],
            "nutrition":   [(0, -1.0), (50,  0.0)],
            "sleep":       [(0, -1.0), (30,  0.0)],
        },
        "cari_jurnal": {
            "autonomy":    [(0.0, -0.4), (75, 0.0)],
            "competence":  [(0.0, -0.4), (75, 0.0)],
            "relatedness": [(0.0, -0.4), (75, 0.0)],
            "physical_activity":          [(0.0, -0.4), (75, 0.0)],
            "nutrition":   [(0, -1.0), (50,  0.0)],
            "sleep":       [(0, -1.0), (30,  0.0)],
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
            "caffeine_plasma_level": [(0.2, 1), (1.0, 0.0)],
        },
        "olahraga_ringan": {
            "physical_activity":          [(0.0, 0.8), (50, 0.0), (80, 0), (100, -0.5)],
        },
        "olahraga_sedang": {
            "physical_activity":          [(0.0, -0.2), (50, 0.0), (80, 0), (100, -0.5)],
        },
        "olahraga_berat": {
            "physical_activity":          [(0.0, -0.7), (50, 0.0), (80, 0), (100, -0.7)],
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
        "tidur": {
            "autonomy":    [(0.0, -0.1), (30, 0.0)],
            "competence":  [(0.0, -0.1), (30, 0.0)],
            "relatedness": [(0.0, -0.1), (30, 0.0)],
            "nutrition":   [(0.0, -2.0), (40, 0.0)],
            "physical_activity": [(0.0, -0.2), (50, 0.0)],
            "sleep":       [(30, 1.0), (70, -1.0)]
        },
        "meditasi": {
            "arousal": [(0, -1.0), (50, 1.0)]
        },
        "prokrastinasi": {
            "autonomy":    [(0.0, 0.5), (100, -0.05)],
            "competence":  [(0.0, 0.5), (100, -0.05)],
            "relatedness": [(0.0, 0.5), (100, -0.05)],
            "nutrition":   [(0, -2), (35, 0.5), (100, -0.05)],
            "physical_activity":  [(0.0, 0.5), (100, -0.05)],
            "sleep":       [(0, -1), (35, 0.5), (100, -0.05)]
        }
    }

    def get_activity_motivation(activity_name):
        stats = {
            "autonomy":    store.autonomy,
            "competence":  store.competence,
            "relatedness": store.relatedness,
            "nutrition":   store.nutrition,
            "physical_activity": store.physical_activity,
            "sleep":       store.sleep,
            "caffeine_plasma_level": store.caffeine_plasma_level,
            "arousal":     store.arousal,
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

    def get_activity_motivation_label(activity_name):
        value = get_activity_motivation(activity_name)
        if value <= 20:
            return "tidak termotivasi"
        elif value <= 60:
            return "parsial"
        else:
            return "termotivasi"

default activity_fsm_state = "idle"

init python:
    ACTIVITY_IDLE = "idle"

    # ── On-enter hooks ────────────────────────────────────────────────
    def _on_enter_tidur():
        go_to_sleep()

    def _on_enter_skripsi():
        store.earned_score = 0

    def _on_enter_bimbingan():
        in_writing_phase = store.thesis_fsm_state in (
            THESIS_SUPERVISED, THESIS_PROPOSAL_WRITING, THESIS_POST_SEMPRO, THESIS_WRITING
        )
        if store.bimbingan_count > 0 and in_writing_phase:
            progress_diff = store.thesis_progress - store.bimbingan_last_thesis_progress
            if progress_diff <= 5:
                store.competence = max(0, store.competence - 20)
                store.valence    = max(0, store.valence - 10)
                store.arousal    = min(store.max_stat, store.arousal + 10)
                renpy.say(None, "Dosen pembimbing melihat bahwa kamu masih belum ada kemajuan di skripsimu.")
                renpy.say(None, "Kamu merasa tertekan atas ketidak adanya kemajuan dalam skripsimu.")
                renpy.say(None, "Dosen pembimbingmu perlahan menjelaskan kembali apa yang harus kamu revisi.")

    ACTIVITY_ON_ENTER = {
        "tidur":     _on_enter_tidur,
        "skripsi":   _on_enter_skripsi,
        "bimbingan": _on_enter_bimbingan,
    }

    # ── On-exit hooks ─────────────────────────────────────────────────
    def _on_exit_tidur():
        wake_up(current_hour, current_minute)
        store.sleep = get_sleep_need()

    def _on_exit_skill_activity():
        update_levels()

    def _on_exit_bimbingan():
        update_levels()
        if not thesis_advisor_approved():
            return
        store.bimbingan_last_thesis_progress = store.thesis_progress
        store.bimbingan_count += 1
        store.bimbingan_bonus_active = True
        store.bimbingan_bonus_start_progress = store.thesis_progress

    ACTIVITY_ON_EXIT = {
        "tidur":           _on_exit_tidur,
        "skripsi":         _on_exit_skill_activity,
        "bimbingan":       _on_exit_bimbingan,
        "workshop":        _on_exit_skill_activity,
        "belajar_mandiri": _on_exit_skill_activity,
    }

    # ── Enhanced per-minute tick functions ────────────────────────────
    def _activity_tick_skripsi():
        if store.bimbingan_bonus_active:
            if (store.thesis_progress - store.bimbingan_bonus_start_progress) > 10:
                store.bimbingan_bonus_active = False
        rate = get_thesis_progress_rate()

        store.thesis_progress = min(100, store.thesis_progress + rate)
        _activity_skripsi()
        store.earned_score += calculate_thesis_score()

        _thesis_on_writing_tick()

        if thesis_check_completion():
            store.interrupted = True

    def _activity_tick_cari_jurnal():
        if thesis_fsm_state == THESIS_EXPLORING:
            chance = min(0.9, (store.practical_level) * 0.15) / 60
            if renpy.random.random() < chance:
                thesis_advance_to(THESIS_TOPIC_FOUND)
                renpy.say(None, "Kamu berhasil mendapatkan topik proposal yang kamu pahami!")
                renpy.say(None, "Segera bimbingan dengan dosen untuk memastikan apakah topik ini layak untuk dilanjutkan.")
        _activity_cari_jurnal()

    def _activity_tick_bimbingan():
        if thesis_fsm_state == THESIS_TOPIC_FOUND:
            practical_skill_factor = (store.practical_level) * 0.15
            competence_factor      = store.competence / store.max_stat * 0.05
            relatedness_factor     = store.relatedness / store.max_stat * 0.05
            total_chance = 0.05 + practical_skill_factor + competence_factor + relatedness_factor
            total_chance = min(0.9, total_chance) / 10
            if renpy.random.random() < total_chance:
                thesis_advance_to(THESIS_SUPERVISED)
                renpy.say(d_bim, "Mas, setelah saya pelajari, topik ini menarik dan layak untuk dilanjutkan.")
                renpy.say(d_bim, "Fondasi teorinya ada, dan ada celah penelitian yang bisa Mas isi di sini.")
                renpy.say(d_bim, "Saya setuju untuk membimbing proposal ini. Silakan mulai mengerjakan drafnya.")
                renpy.say(p, "Serius, Pak? Alhamdulillah...")
                renpy.say(p, "Terima kasih banyak, Pak. Saya akan langsung mulai.")
                renpy.say(d_bim, "Yang terpenting mengerjakan BAB 3 Metodologi Penelitian dahulu.")
                renpy.say(d_bim, "Karena BAB 3 ini menjelaskan apa yang mau kamu lakukan, apa yang mau kamu riset.")
                renpy.say(d_bim, "Kalau BAB 3 udah bagus, nanti BAB 1 dan BAB 2 nya juga jadi jelas mau ditulis apa.")
                renpy.say(d_bim, "Ingat, bimbingan rutin itu penting. Jangan menunggu drafnya sempurna dulu baru ke saya.")
                renpy.say(p, "Baik, Pak. Terima kasih banyak.")
        _activity_bimbingan()

    # ACTIVITY_TICK extends ACTIVITY_DISPATCH with special-case overrides
    ACTIVITY_TICK = dict(ACTIVITY_DISPATCH)
    ACTIVITY_TICK["skripsi"]     = _activity_tick_skripsi
    ACTIVITY_TICK["cari_jurnal"] = _activity_tick_cari_jurnal
    ACTIVITY_TICK["bimbingan"]   = _activity_tick_bimbingan

    # ── FSM lifecycle ─────────────────────────────────────────────────
    def activity_fsm_start(activity_name):
        global activity_fsm_state
        activity_fsm_state = activity_name
        enter_fn = ACTIVITY_ON_ENTER.get(activity_name)
        if enter_fn:
            enter_fn()

    def activity_fsm_tick():
        advance_time(1)
        decrease_stats(1)
        tick_fn = ACTIVITY_TICK.get(activity_fsm_state)
        if tick_fn:
            tick_fn()

    def activity_fsm_stop():
        global activity_fsm_state
        exit_fn = ACTIVITY_ON_EXIT.get(activity_fsm_state)
        if exit_fn:
            exit_fn()
        update_motivation_and_progress()
        activity_fsm_state = ACTIVITY_IDLE