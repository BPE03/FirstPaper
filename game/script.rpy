# Label to start the game

label start:
    "Jumat, 12 Desember 2025."
    scene kelas with fade
    p "Huft, akhirnya kelar juga EAS terakhir ini."
    p "Mana susah-susah lagi, moga lulus semua aja dah."
    p "Si Joko gimana tuh EAS-nya kira-kira?"
    show joko with fade
    p "Oi Jok!"
    j "Lah, Paijo. EAS lu gimana?"
    p "....."
    p "Kita balas di semester depan bos."
    j "Walah wkwkwk yang bener aja jo."
    p "Yaudah lah yah, moga nilai tugas-tugas yang lain bisa bantu angkat lah."
    p "Lu gimana?"
    j "Gua positif aman sih, cuma ada beberapa soal yang gua ragu-ragu, tapi ya semoga bisa dapet A lah."
    p "Amiin.. mantap-mantap."
    j "Lu habis ini ada rencana apa?"
    p "Ga ada sih, paling pulang terus tidur, capek banget."
    j "Wkwkwk, gua juga sih, paling pulang terus main game, capek banget."
    p "Wkwkwk, yaudah lah ya. Gua balik duluan yak."
    j "Oke oke, tiati di jalan Jo."
    p "Yoi."
    scene black with fade
    "Dengan hati yang lega, Paijo pun balik ke kosnya untuk mendapatkan hadiah dari kerja kerasnya."
    "Kerja keras?"
    "Hadiah?"
    "Paijo tidak memedulikan detail kecil yang tiba-tiba muncul di benaknya."
    "Yang ia tahu sekarang adalah, dia ingin menggunakan waktunya untuk bersenang-senang setelah menyelesaikan EAS."
    p "Hmm kayak ada sesuatu yang ngeganjel, tapi apa yak?"
    p "....."
    p "....."
    p "Ah ga tau lah, paling karena capek aja sih."
    scene kos with fade
    p "Hai istana, rajamu telah kembali."
    "Pause"
    p "Habis ngerjain EAS gini emang paling bener langsung tidur sih."
    "Paijo pun bergegas mengganti bajunya dan langsung melakukan aktivitas yang sangat ia dambakan yaitu rebahan."
    p "Hadeh tapi lagi kaga ngantuk gua."
    "Paijo mengambil handphone-nya dan mulai membuka media sosial untuk menghabiskan waktu."
    "Scrolling-scrolling...."
    scene kos with fade
    "Postingan demi postingan..."
    scene kos with fade
    "Reels demi reels..."
    scene kos with fade
    "Hal tersebut tanpa sadar sudah menghabiskan waktu selama 2 jam lamanya."
    p "Wkwkwk lah bisa gitu raut mukanya."
    "Notif.sfx"
    "Semua kesenangan itu berubah ketika ada notifikasi masuk di handphone Paijo."
    "Semua tawa yang ia keluarkan sebelumnya langsung menghilang seketika."
    "Di dalam benak Paijo, dia tahu telah melupakan sesuatu yang besar."
    "Namun dia tidak tahu apa itu."
    "Perasaan itu selalu mengganjal di Paijo tetapi dia tidak terlalu memikirkannya."
    "Namun notifikasi yang datang itu akhirnya menjelaskan sesuatu yang mengganjal tersebut."
    j "\"Jo, proposal lu gimana? udah sebulan lagi seminar proposal nih.\""
    p "....."
    p "....."
    "udah sebulan lagi seminar proposal nih."
    "Sebulan?"
    "Tentu saja."
    "Proposal merupakan mata kuliah di semester ini, sehingga deadline seminar proposal seharusnya tidak jauh dari setelah EAS."
    p "\"Ahh... proposal mah gampang, tinggal sat set diacc dosen kelar.\""
    j "\"Hah, seriusan lu?\""
    j "\"Lu tau kan ini udah tinggal sebulan lagi seminar proposal, berarti tinggal sebulan lagi buat ngerjain proposalnya?\""
    p "....."
    "Paijo tidak bisa berkata-kata."
    "Ia membayangkan dirinya yang harus mengerjakan proposal dalam waktu sebulan ke depan, dan itu membuatnya merasa sangat tertekan."
    j "\"Apalagi lu belum ada topik yang jelas, yakin ada topik langsung acc?\""
    j "\"Mending langsung lu kerjain dah.\""
    p "....."
    p "Ahh...."
    "Paijo memikirkan kembali momen-momen di mana dia menunda mengerjakan proposalnya."
    "\"Ah masih lama... ntar aja lah lagi banyak tugas juga.\""
    "\"Hmm lagi gak mood sih... paling besok atau kapan-kapan lah.\""
    "Bro berpikir dia karakter utama."
    "Tentu saja kemewahan itu tidak bisa berlangsung selamanya."
    p "\"Aman lah, masih lama kok.\""
    j "\"Lahh... serah lu dah.\""
    j "\"Awas aja lu sampe ga sempro bulan depan.\""
    j "\"Lama-lama dosen juga sungkem duluan sama lu.\""
    p "\"Iya dah gua kerjain nih.\""
    "Setelah itu juga Paijo tidak bisa menunda lagi."
    "Dia bergegas membuka laptopnya dan mulai mencari-cari referensi untuk digunakan sebagai topik proposalnya."
    "Namun, dia merasa sangat kesulitan untuk menemukan topik yang menarik dan sesuai dengan minatnya."
    "Dia merasa sangat tertekan karena deadline seminar proposal semakin dekat, tetapi dia belum menemukan topik yang tepat."
    "Ditambah dengan lelahnya setelah menyelesaikan EAS, dia merasa sangat kesulitan untuk mendapatkan ide."
    p "Duh, ga nemu-nemu topik yang menarik."
    p "Mana capek banget lagi."
    p "Mending lanjut cari referensi atau lanjut besok aja ya?"
    menu:
        "Lanjutkan cari referensi?"
        "Ayolah":
            call prologue_lanjut
        "Lanjut besok aja":
            call prologue_lanjut_besok

    scene kos with fade
    "...."
    "Eits, bentar dulu."
    "Apakah kamu sudah paham bagaimana cara memainkan game ini?"
    menu:
        "Apakah kamu sudah paham bagaimana cara memainkan game ini?"
        "Sudah":
            "Bersiaplah."
        "Belum":
            scene black with fade
            call tutorial_scene
            scene kos with fade
    "Sekarang."
    # Show all screens
    show screen main_stats
    show screen detailed_stats_window
    show screen calendar_now
    show screen calendar_window
    
    jump kos

label prologue_lanjut:
    "Paijo pun memutuskan untuk terus mencari referensi untuk proposalnya."
    p "Cari terus lah, waktu tinggal dikit juga."
    p "Inget kata-kata seorang youtuber."
    p "Ngga dapet topik, ngga tidur."
    "Paijo terus mencari referensi topik yang dapat ia pahami."
    "Namun, semakin ia mencari, semakin ia merasa kelelahan dan kehilangan motivasi."
    scene kos with fade
    "Keesokan paginya, Paijo merasa sangat lelah dan tidak memiliki energi untuk melanjutkan pencarian referensi untuk proposalnya."
    "Sehingga dengan berat hati, dia memutuskan untuk berhenti dan tidur sebelum kondisi kesehatannya memburuk."
    scene black with fade
    show text "First Paper"
    $ renpy.pause(5.0, hard=True) # Matches the transition time
    show text "Dikembangkan oleh: Bimantara Putra Ernandra" with fade
    $ renpy.pause(5.0, hard=True) # Matches the transition time
    "Sabtu, 13 Desember 2025."
    p "...."
    p "Hahh...."
    p "Tidur berapa jam gua?"
    p "Cape banget rasanya, kaya ga tidur semaleman."
    "Kan emang begadang."
    p "Duh gua harus ngapain ya."
    p "Bener-bener ga kepikiran apa-apa buat skripsi nanti."
    "Paijo langsung menyalakan laptopnya kembali."
    p "Hmmm gimana ya."
    "Dia bergegas mencari jurnal lagi tanpa arah yang jelas."
    "Hal ini pun berlangsung selama beberapa menit."
    p "Udah baca ulang jurnal yang sama pun masih ga masuk."
    p "Ueueueueue..."
    p "...."
    p "...."
    p "Apa langkah gua salah ya?"
    p "...."
    p "...."
    "notif.sfx"
    p "Notif apalagi nih."
    j "\"Jo, gimana skripsi lu? udah ngerjain kah?\""
    p "\"Belum Jok, masih bingung cari topik euy.\""
    j "\"Bingung gimana? cari topik yang sesuai sama apa yang lu suka aja.\""
    j "\"Ga mungkin kalo ga ada. Banyak kok yang bisa lu jadikan topik riset.\""
    p "\"Nah itu masalahnya, gua ga tau apa yang gua suka.\""
    j "\"Yee elu sih kupu-kupu, jadi bingung kan.\""
    j "\"Hmmm... mungkin kalo gua jadi lu sih gua coba main-main di beberapa bidang ilmu dulu deh.\""
    j "\"Di Informatika kan topik skripsinya harus ngikut lab yang ada.\""
    j "\"Cobain satu-satu lu bikin program kek, atau belajar yang berhubungan sama lab itu dah.\""
    j "\"Sumpah lu ginian udah telat banget Jo, tapi kalo lu mau lulus ya cuma itu caranya.\""
    p "Hmmm... pelajari tiap bidang ilmu ya...."
    p "\"Oke Jok, saran yang mantap.\""
    j "\"Buruan jangan nunda-nunda lagi lu.\""

    p "Hmm, bidang ilmu ya."
    p "Okelah gua cari deh satu-satu."
    "......"
    scene kos with fade
    p "Okeh, gua dah nemu semua nih, sekarang bidang ilmu mana dulu yang pengen gua telusuri?"
    call pilih_bidang
    p "Oke, kayaknya Lab [selected_bidang] ini yang paling menarik deh buat gua."
    p "Berarti next step gua cari jurnal ama topik yang berhubungan sama bidang ilmu ini."
    p "Oke, gua dah tau apa yang harus gua lakuin, saatnya eksekusi!"

    $ valence = 20
    $ arousal = 80
    $ physical_activity = 20
    $ nutrition = 15
    $ autonomy = 20
    $ competence = 20
    $ sleep = 50
    $ current_hour = 12
    return

label prologue_lanjut_besok:
    "Paijo memutuskan untuk istirahat dan melanjutkan pencarian referensi untuk proposalnya besok."
    "Tentu saja hal ini tidak membuatnya merasa lebih baik, karena dia tahu bahwa deadline seminar proposal semakin dekat."
    "Namun, dia merasa bahwa dia tidak bisa memaksakan dirinya untuk terus mencari referensi ketika dia sudah sangat lelah."
    scene black with fade
    show text "First Paper"
    $ renpy.pause(5.0, hard=True) # Matches the transition time
    show text "Dikembangkan oleh: Bimantara Putra Ernandra" with fade
    $ renpy.pause(5.0, hard=True) # Matches the transition time
    "Sabtu, 13 Desember 2025."
    p "....."
    p "Bangun pagi, ku terus...."
    p "Ngerjain skripsi."
    p "...."
    p "Oalah pantes aja."
    p "Gua ga nemu-nemu topik yang pas itu bukan karena gua ga nyari di tempat yang bener."
    p "Tapi emang gua aja yang ga tau kemampuan ama minat gua."
    p "Kalo gua ga minat apa-apa dapet topik gimana coba."
    p "Hmm terus gimana dah."
    p "...."
    p "Bentar."
    p "...."
    p "Di Informatika kan ada beberapa bidang ilmu yak."
    p "Mungkin gua bisa riset dari situ dulu, baru gua cari topik yang lebih spesifik lagi."
    "......"
    scene kos with fade
    p "Okeh, gua dah nemu semua nih, sekarang bidang ilmu mana dulu yang pengen gua telusuri?"
    call pilih_bidang
    p "Oke, kayaknya Lab [selected_bidang] ini yang paling menarik deh buat gua."
    p "Berarti next step gua cari jurnal ama topik yang berhubungan sama bidang ilmu ini."
    p "Oke, gua dah tau apa yang harus gua lakuin, saatnya eksekusi!"
    return

label pilih_bidang:
    menu:
        "Bidang ilmu mana yang mau kamu jelajahi duluan?"
        "KCV":
            $ selected_bidang = "KCV"
        "AlPro":
            $ selected_bidang = "AlPro"
        "GIGA":
            $ selected_bidang = "GIGA"
        "RPL":
            $ selected_bidang = "RPL"
        "Selanjutnya":
            menu:
                "Bidang ilmu mana yang mau kamu jelajahi duluan?"
                "KBJ":
                    $ selected_bidang = "KBJ"
                "Netics":
                    $ selected_bidang = "Netics"
                "MCI":
                    $ selected_bidang = "MCI"
                "PKT":
                    $ selected_bidang = "PKT"
                "Kembali":
                    call pilih_bidang
                    return
    $ renpy.scene()
    $ renpy.show(selected_bidang.lower())
    with fade
    n "[bidang_ilmu[selected_bidang]['nama']]"
    n "Laboratorium ini menawarkan bidang keahlian yang ditekankan pada kemampuan lulusan dalam [bidang_ilmu[selected_bidang]['deskripsi']]"
    n "Mata kuliah pada bidang ilmu ini adalah [bidang_ilmu[selected_bidang]['mata_kuliah']]."
    n "Yakin ingin fokus ke bidang ilmu ini? (Memilih bidang ilmu hanya mengubah siapa dosen pembimbingmu dan peristiwa saat sidang nanti.)"
    nvl clear
    menu:
        "Yakin ingin fokus ke bidang ilmu ini? (Memilih bidang ilmu hanya mengubah siapa dosen pembimbingmu dan peristiwa saat sidang nanti.)"
        "Ya":
            scene kos with fade
            return
        "Tidak":
            scene kos with fade
            call pilih_bidang
            return
    return

label tutorial_scene:
    n "Game ini mensimulasikan kehidupan seorang mahasiswa yang sedang mengerjakan skripsi."
    n "Ada beberapa aspek yang disimulasikan dalam game ini, namun secara utama hal yang perlu diperhatikan adalah motivasi dan emosi karakter."
    n "Motivasi akan mempengaruhi seberapa besar keinginan karakter untuk mengerjakan skripsi."
    n "Emosi akan mempengaruhi seberapa baik karakter dapat mengerjakan skripsinya."
    n "Kamu akan diberikan pilihan aktivitas setiap harinya, dan setiap aktivitas akan mempengaruhi motivasi dan emosi karakter dengan cara yang berbeda-beda."
    nvl clear

    n "Motivasi"
    n "Untuk meningkatkan motivasi, pemain perlu memenuhi kebutuhan psikologis dan kebutuhan fisiknya."
    n "Kebutuhan psikologis terdiri dari kebutuhan akan otonomi, kompetensi, dan keterhubungan."
    n "Kebutuhan fisik terdiri dari kebutuhan akan nutrisi, aktivitas fisik, dan tidur."
    nvl clear
    n "Otonomi adalah kebutuhan untuk merasa memiliki kontrol atas hidup kita sendiri."
    n "Otonomi dapat dipenuhi dengan melakukan aktivitas yang kita sukai, atau dengan membuat keputusan sendiri tentang apa yang akan kita lakukan."
    n "Kompetensi adalah kebutuhan untuk merasa mampu dan efektif dalam melakukan sesuatu."
    n "Kompetensi dapat dipenuhi dengan melakukan aktivitas yang menantang tetapi masih bisa kita lakukan, atau dengan belajar sesuatu yang baru."
    n "Keterhubungan adalah kebutuhan untuk merasa terhubung dengan orang lain."
    n "Keterhubungan dapat dipenuhi dengan menghabiskan waktu dengan teman-teman, atau dengan berbicara dengan orang lain tentang apa yang kita rasakan."
    nvl clear
    n "Nutrisi adalah kebutuhan untuk mendapatkan asupan nutrisi melalui makanan atau minuman."
    n "Nutrisi tentu saja dapat dipenuhi dengan mengonsumsi makanan atau minuman."
    n "Aktivitas fisik adalah kebutuhan untuk melakukan aktivitas fisik yang cukup."
    n "Aktivitas fisik dapat dipenuhi dengan berolahraga."
    n "Tidur adalah kebutuhan untuk mendapatkan tidur yang cukup."
    n "Namun, mekanik tidur di dalam game ini tidak hanya sekadar mendapatkan tidur yang cukup, tetapi juga mendapatkan tidur yang berkualitas dengan memperhatikan faktor-faktor seperti siklus sirkadian dan utang tidur."
    n "Secara umum, pemain hanya perlu untuk melakukan tidur dan bangun pada jam yang konsisten."
    nvl clear

    n "Emosi"
    n "Emosi dalam game ini terdiri dari dua dimensi yaitu {i}valence{/i} dan {i}arousal{/i}."
    n "{i}Valence{/i} adalah dimensi yang menunjukkan seberapa positif atau negatif suatu emosi."
    n "{i}Valence{/i} akan meningkat ketika karakter melakukan aktivitas yang menyenangkan atau memuaskan, dan akan menurun ketika karakter melakukan aktivitas yang tidak menyenangkan atau membuat stres."
    n "{i}Arousal{/i} adalah dimensi yang menunjukkan seberapa intens suatu emosi."
    n "{i}Arousal{/i} akan meningkat ketika karakter melakukan aktivitas yang menstimulasi atau membuatnya merasa lebih hidup, dan akan menurun ketika karakter melakukan aktivitas yang menenangkan atau membuatnya merasa lebih santai."
    nvl clear

    n "Untuk mendapatkan topik proposal, kamu dapat mendapatkannya dari aktivitas mencari jurnal."
    n "Namun faktor keberhasilanmu untuk mendapatkan topik proposal yang dapat kamu pahami dipengaruhi oleh kemampuan praktismu."
    n "Semakin tinggi kemampuan praktismu, semakin besar peluangmu untuk mendapatkan topik proposal yang dapat kamu pahami."
    n "Kamu bisa mulai mengerjakan skripsimu ketika kamu sudah mendapatkan topik."

    "Apakah kamu ingin mengulang penjelasan tadi?"
    menu:
        "Apakah kamu ingin mengulang penjelasan tadi?"
        "Ya":
            call tutorial_scene
            return
        "Tidak":
            return
    return

label sempro:
    "Hari seminar proposal pun tiba."
    "Paijo merasa sangat gugup dan tidak percaya diri karena dia belum menyelesaikan proposalnya."
    "Namun, dia tahu bahwa dia harus menghadapi kenyataan dan melakukan yang terbaik dalam seminar proposalnya."
    scene black with fade
    return

label post_sempro:
    "Setelah seminar proposal, Paijo merasa sangat lega dan senang karena dia berhasil melalui seminar proposal dengan baik."

    jump kos

label sidang_akhir:
    "Hari sidang akhir pun tiba."

label post_sidang_akhir:
    "Setelah sidang akhir, Paijo merasa sangat lega dan senang karena dia berhasil menyelesaikan sidang akhir dengan baik."

label kos:
    $ current_location = "kos"
    scene kos with fade
    call screen interactive_kos

label dapur:
    $ current_location = "dapur"
    scene dapur with fade
    call screen interactive_dapur

label activity_kos_kasur:
    $ activity = None
    menu:
        "Mau Ngapain?"
        
        "Tidur":
            $ activity = "tidur"

        "Batal":
            jump kos
    call process_activity
    jump kos

label activity_kos_laptop:
    $ activity = None
    $ _m_thesis     = get_activity_motivation("skripsi")[1]
    $ _m_workshop   = get_activity_motivation("workshop")[1]
    $ _m_selflearn  = get_activity_motivation("selflearn")[1]
    $ _m_jurnal     = get_activity_motivation("cari_jurnal")[1]
    $ _m_chat_online = get_activity_motivation("chat_online")[1]
    $ _m_main_game = get_activity_motivation("main_game")[1]
    menu:
        "Mau Ngapain?"

        "Kerjakan Skripsi ([_m_thesis]) (Membutuhkan motivation > 30)":
            if not dapat_topik:
                "Kamu belum mendapatkan topik untuk skripsimu, jadi kamu belum bisa mulai mengerjakan skripsimu."
                jump kos
            if motivation <= 30:
                "Motivasi kamu terlalu rendah untuk mengerjakan skripsi. Coba lakukan aktivitas lain untuk meningkatkan motivasimu."
                jump kos
            $ activity = "skripsi"

        "Attend a workshop / Learn new skills ([_m_workshop])":
            $ activity = "workshop"

        "Practice self-directed learning ([_m_selflearn])":
            $ activity = "selflearn"

        "Cari Jurnal ([_m_jurnal])":
            $ activity = "cari_jurnal"

        "Chat Online ([_m_chat_online])":
            $ activity = "chat_online"

        "Main Game ([_m_main_game])":
            $ activity = "main_game"

        "Batal":
            jump kos

    call process_activity
    jump kos

# Main gameplay loop
label activity_kos:
    $ activity = None
    $ _m_olahraga   = get_activity_motivation("olahraga")[1]
    $ _m_bimbingan  = get_activity_motivation("bimbingan")[1]
    $ _m_sosialisasi  = get_activity_motivation("sosialisasi")[1]
    menu:
        "Mau Ngapain?"

        "Olahraga ([_m_olahraga])":
            $ activity = "olahraga"

        "Bimbingan dengan dosen ([_m_bimbingan])":
            if not dapat_topik:
                "Kamu belum mendapatkan topik untuk skripsimu, jadi kamu belum bisa bimbingan."
                jump kos
            $ activity = "bimbingan"

        "Sosialisasi dengan teman ([_m_sosialisasi])":
            $ activity = "sosialisasi"

        # "Just rest and do nothing":
        #     $ activity = "rest"

        "Skip time":
            $ activity = "skip"

        "Batal":
            jump kos
    
    call process_activity
    jump kos

label activity_dapur:
    $ activity = None
    $ _m_bergizi = get_activity_motivation("makan_bergizi")[1]
    $ _m_enak    = get_activity_motivation("makan_enak")[1]
    $ _m_kopi    = get_activity_motivation("minum_kopi")[1]
    menu:
        "Mau ngapain?"

        "Makan Bergizi ([_m_bergizi])":
            $ activity = "makan_bergizi"

        "Makan Enak Sembarangan ([_m_enak])":
            $ activity = "makan_enak"

        "Minum Kopi ([_m_kopi])":
            $ activity = "minum_kopi"

        "Ga jadi":
            jump dapur

    call process_activity
    jump dapur

label process_activity:
    # Ask for time in hours and minutes
    $ activity_data = activities[activity]
    $ min_dur = activity_data["min_duration"]
    $ max_dur = activity_data["max_duration"]
    $ def_h = activity_data["default_duration_hours"]
    $ def_m = activity_data["default_duration_minutes"]
        
    if min_dur == max_dur:
        $ time_minutes = min_dur
    else:
        if activity == "tidur":
            $ hours_input = renpy.input("Kamu akan tidur berapa jam? (Min: {} - Max: {})".format(format_duration(min_dur), format_duration(max_dur)), default=str(def_h))
            $ hours = int(hours_input) if hours_input.isdigit() else def_h
            $ hours = max(min_dur//60, min(max_dur//60, hours))
            $ time_minutes = hours * 60
        else:
            $ hours_input = renpy.input("Kamu mau aktivitas selama berapa jam? (Min: {} - Max: {})".format(format_duration(min_dur), format_duration(max_dur)), default=str(def_h))
            $ minutes_input = renpy.input("Berapa menit?", default=str(def_m))
            $ hours = int(hours_input) if hours_input.isdigit() else def_h
            $ minutes = int(minutes_input) if minutes_input.isdigit() else def_m
            if hours < 0:
                $ hours = 0
            if minutes < 0:
                $ minutes = 0
            elif minutes >= 60:
                $ hours += minutes // 60
                $ minutes = minutes % 60
            $ time_minutes = hours * 60 + minutes
            $ time_minutes = max(min_dur, min(max_dur, time_minutes))
    "Yakin mau melakukan aktivitas ini?"
    menu:
        "Yakin mau melakukan aktivitas ini?"
        "Yakin":
            #Continue to next line
            pass
        "Tidak":
            return
    $ minutes_activity = 1
    $ delay_batch = time_minutes // 60  # For activities longer than 1 hour, we can batch the time advancement
    if delay_batch < 1:
        $ delay_batch = 1  # Minimum batch of 1 minute to ensure UI updates
    $ current_motivation_mult, current_motivation_label = get_activity_motivation(activity)
    if activity not in ("skip", "tidur"):
        "Motivasimu untuk aktivitas ini: [current_motivation_label] (x[current_motivation_mult])"
    # Special handling for sleep activity - uses dedicated sleep mechanic
    if activity == "tidur":
        $ sleep_hours = time_minutes // 60
        "You head to bed for the night..."
        "Zzzzzzz... [sleep_hours] hours of sleep..."
        $ perform_sleep(sleep_hours)
        scene black with fade
    # Loop through each minute for other activities
    else:
        python:
            for minutes_activity in range(time_minutes+1):
                advance_time(1)
                decrease_stats(1)
                
                if activity == "skripsi":
                    if motivation > 30:
                        mult = store.current_motivation_mult
                        store.thesis_progress = min(100, store.thesis_progress + (1/60) * mult)
                        ACTIVITY_DISPATCH["skripsi"]()  # Apply thesis-specific effects
                        earned_score += calculate_thesis_score() * mult
                    else:
                        break
                elif activity == "cari_jurnal":
                    if not dapat_topik:
                        xp_in_level = get_xp_in_level(store.practical_xp, store.practical_level)
                        required = get_required_for_level(store.practical_level)
                        xp_ratio = xp_in_level / required
                        # Each level above 1 adds 15% base; XP within the level adds up to 15% more
                        chance = min(0.9, (store.practical_level - 1 + xp_ratio) * 0.15)
                        if renpy.random.random() < chance:
                            dapat_topik = True
                            renpy.say(narrator, "Kamu berhasil mendapatkan topik proposal yang kamu pahami!")
                            renpy.say(narrator, "Segera bimbingan dengan dosen untuk memastikan apakah topik ini layak untuk dilanjutkan.")
                    apply_with_motivation(ACTIVITY_DISPATCH.get(activity, lambda: None), store.current_motivation_mult)
                elif activity == "bimbingan":
                    if not dosen_acc:
                        # 5% chance per minute to get acc, increased by competence and relatedness
                        base_chance = 0.05
                        competence_factor = store.competence / store.max_stat * 0.1  # up to +10%
                        relatedness_factor = store.relatedness / store.max_stat * 0.1  # up to +10%
                        total_chance = base_chance + competence_factor + relatedness_factor
                        if renpy.random.random() < total_chance:
                            dosen_acc = True
                            renpy.say(narrator, "Dosen menyetujui topik proposalmu! Kamu bisa mulai mengerjakan skripsimu sekarang.")
                    apply_with_motivation(ACTIVITY_DISPATCH.get(activity, lambda: None), store.current_motivation_mult)
                else:
                    fn = ACTIVITY_DISPATCH.get(activity)
                    if fn:
                        apply_with_motivation(fn, store.current_motivation_mult)
                if (minutes_activity % delay_batch == 0):
                    renpy.pause(delay=delay)  # Small pause to allow UI to update each minute
                if interrupted:
                    break
            
            # For skip, no effects
    
    # Record when this activity was last done (for motivation tracking)
    if activity not in ("skip", "tidur"):
        $ activity_last_done[activity] = get_total_game_minutes()

    # Update levels and motivation after loop
    if activity in ["skripsi", "bimbingan", "workshop", "selflearn"]:
        $ update_levels()
    
    $ update_motivation_and_progress()
    
    # Show messages
    if activity == "skripsi":
        "Kamu mengerjakan skripsi selama [minutes_activity] menit."
        "Kamu mendapatkan [earned_score] poin!"
        $ earned_score = 0  # Reset earned score after showing message
    
    elif activity == "olahraga":
        "Kamu olahraga selama [minutes_activity] menit. Kamu merasa lebih segar!"
    
    elif activity == "bimbingan":
        if not dosen_acc:
            "Kamu bimbingan dengan dosen selama [minutes_activity] menit, namun topikmu belum disetujui."
            "Dosen menyarankan untuk memperdalam pemahamanmu tentang topik yang kamu pilih dan kembali lagi nanti."
            $ dapat_topik = False  # Ensure you don't get the benefits of having a topic until you actually get it
        else:
            "Kamu bimbingan dengan dosen selama [minutes_activity] menit. Kamu memperoleh kejelasan dan arah!"
    
    elif activity == "sosialisasi":
        "Kamu menghabiskan waktu dengan teman-teman untuk [minutes_activity] menit. Kamu merasa terhubung dan bahagia!"
    
    elif activity == "nap":
        "Kamu tidur siang selama [minutes_activity] menit. Kamu merasa lebih waspada sekarang!"

    elif activity == "makan_bergizi":
        "Kamu makan makanan bergizi selama [minutes_activity] menit. Nutrisimu meningkat!"
    elif activity == "makan_enak":
        "Kamu menikmati makanan enak selama [minutes_activity] menit. Mood kamu meningkat, namun kamu mendapatkan kalori lebih banyak."

    elif activity == "minum_kopi":
        "Kamu menikmati kopi selama [minutes_activity] menit. Tingkat kafein dan kewaspadaan kamu meningkat!"
    
    elif activity == "tidur":
        $ sleep_hours = time_minutes // 60
        $ circadian_quality = get_sleep_quality_factor()
        if circadian_quality >= 1.3:
            "Kamu tidur nyenyak! Kamu merasa benar-benar segar!"
        else:
            "Kamu bangun merasa cukup istirahat."
        "Tingkat Adenosine: [int(adenosine_level)], Utang Tidur: [int(sleep_debt)] jam"
    
    elif activity == "workshop":
        "Kamu menghadiri sebuah workshop selama [minutes_activity] menit. Kemampuanmu meningkat!"
    
    elif activity == "selflearn":
        "Kamu belajar secara mandiri selama [minutes_activity] menit. Kamu merasa lebih punya kendali!"
    
    elif activity == "rest":
        "Kamu beristirahat selama [minutes_activity] menit."
    
    elif activity == "skip":
        "Kamu melewatkan [minutes_activity] menit."

    elif activity == "cari_jurnal":
        if not dapat_topik:
            "Kamu belum berhasil menemukan topik proposal yang kamu pahami."
        "Kamu mencari dan membaca jurnal selama [minutes_activity] menit. Kamu mendapatkan ilmu baru."

    elif activity == "chat_online":
        "Kamu mengobrol dengan teman-teman secara online selama [minutes_activity] menit. Kamu merasa lebih terhubung!"

    elif activity == "main_game":
        "Kamu bermain game selama [minutes_activity] menit. Kamu merasa lebih santai dan terhibur!"
    
    # Check for random event (1% chance)
    #call check_random_event
    
    return

# Random event system - 1% chance after any activity
label check_random_event:
    $ random_chance = renpy.random.randint(1, 100)
    if random_chance > 1:
        call random_event
    return

label random_event:
    $ set_cutscene_mode(True)  # Enter cutscene mode to hide UI
    $ event_type = renpy.random.choice(["lucky_find", "unexpected_visitors", "inspiration", "small_accident"])
    
    if event_type == "lucky_find":
        "While going about your day, you find a useful reference article on the ground!"
        "It turns out to be exactly what you needed for your thesis."
        $ thesis_progress = min(100, thesis_progress + 3)
        $ competence = min(max_stat, competence + 5)
        "You gained 3 thesis progress and 5 competence!"
    
    elif event_type == "unexpected_visitors":
        "Someone knocks on your door - it's an old friend you haven't seen in a while!"
        "They came to surprise you with a visit."
        $ relatedness = min(max_stat, relatedness + 15)
        $ valence = min(max_stat, valence + 10)
        "You gained 15 relatedness and 10 valence!"
    
    elif event_type == "inspiration":
        "A sudden flash of inspiration hits you!"
        "You feel motivated to work on your thesis right now."
        $ motivation = min(100, motivation + 20)
        $ competence = min(max_stat, competence + 5)
        "You gained 20 motivation and 5 competence!"
    
    elif event_type == "small_accident":
        "Oh no! You accidentally spilled water on your notes."
        "You'll need to redo some of your work."
        $ thesis_progress = max(0, thesis_progress - 2)
        $ valence = max(0, valence - 10)
        "You lost 2 thesis progress and 10 valence!"
    
    $ set_cutscene_mode(False)  # Exit cutscene mode after event
    return

# Burnout ending
label burnout:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen interactive_kos
    hide screen calendar_now
    hide screen calendar_window
    
    scene black with dissolve
    
    centered "{color=#e74c3c}{size=40}BURNOUT{/size}{/color}\n\nYou've experienced burnout and need to take a break from your thesis."
    centered "Remember: Taking care of your wellbeing is essential for academic success!"
    
    menu:
        "Try again?"
        
        "Yes, restart":
            $ motivation = 100
            $ thesis_progress = 0
            $ autonomy = 100
            $ competence = 100
            $ relatedness = 100
            $ nutrition = 100
            $ physical_activity = 100
            $ valence = 100
            $ arousal = 100
            $ practical_xp = 0
            $ writing_xp = 0
            $ practical_level = 1
            $ writing_level = 1
            $ score = 0
            jump start
        
        "No, quit":
            "Thanks for playing!"
            return

# Thesis completion ending
label thesis_complete:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen interactive_kos
    hide screen calendar_now
    hide screen calendar_window
    
    scene bg graduation with dissolve
    
    centered "{color=#2ecc71}{size=50}CONGRATULATIONS!{/size}{/color}\n\nYou've completed your thesis!"
    centered "Through managing your wellbeing and developing your skills,\nyou've achieved your academic goal!"
    
    "Final Stats:"
    "Practical Skill Level: [practical_level]"
    "Writing Skill Level: [writing_level]"
    "Final Motivation: [motivation]"
    "Final Score: [score]"
    
    menu:
        "Play again?"
        
        "Yes":
            $ motivation = 100
            $ thesis_progress = 0
            $ autonomy = 100
            $ competence = 100
            $ relatedness = 100
            $ nutrition = 100
            $ physical_activity = 100
            $ valence = 50
            $ arousal = 50
            $ practical_xp = 0
            $ writing_xp = 0
            $ practical_level = 1
            $ writing_level = 1
            $ score = 0
            jump start
        
        "No":
            "Thanks for playing!"
            return