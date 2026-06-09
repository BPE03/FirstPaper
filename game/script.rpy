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
    scene kos_afternoon with fade
    p "Hai istana, rajamu telah kembali."
    "Pause"
    p "Habis ngerjain EAS gini emang paling bener langsung tidur sih."
    "Paijo pun bergegas mengganti bajunya dan langsung melakukan aktivitas yang sangat ia dambakan yaitu rebahan."
    p "Hadeh tapi lagi kaga ngantuk gua."
    "Paijo mengambil handphone-nya dan mulai membuka media sosial untuk menghabiskan waktu."
    "Scrolling-scrolling...."
    scene kos_afternoon with fade
    "Postingan demi postingan..."
    scene kos_afternoon with fade
    "Reels demi reels..."
    scene kos_night with fade
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

    scene kos_morning with fade
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
            scene kos_morning with fade
    "Sekarang."
    # Show all screens
    show screen main_stats
    show screen detailed_stats_window
    show screen calendar_now
    show screen calendar_window
    show screen game_maps
    
    jump kos

label prologue_lanjut:
    "Paijo pun memutuskan untuk terus mencari referensi untuk proposalnya."
    p "Cari terus lah, waktu tinggal dikit juga."
    p "Inget kata-kata seorang youtuber."
    p "Ngga dapet topik, ngga tidur."
    "Paijo terus mencari referensi topik yang dapat ia pahami."
    "Namun, semakin ia mencari, semakin ia merasa kelelahan dan kehilangan motivasi."
    scene kos_morning with fade
    "Keesokan paginya, Paijo merasa sangat lelah dan tidak memiliki energi untuk melanjutkan pencarian referensi untuk proposalnya."
    "Sehingga dengan berat hati, dia memutuskan untuk berhenti dan tidur sebelum kondisi kesehatannya memburuk."
    scene black with fade
    show text "First Paper"
    $ renpy.pause(5.0, hard=True) # Matches the transition time
    show text "Dikembangkan oleh: Bimantara Putra Ernandra" with fade
    $ renpy.pause(5.0, hard=True) # Matches the transition time
    scene black with fade
    "Sabtu, 13 Desember 2025."
    scene kos_morning with fade
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
    scene kos_morning with fade
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
    $ current_hour = 12
    $ process_s = 0.5
    $ wake_time_in_minute = current_hour * 60 + current_minute
    $ total_daily_time    = current_hour * 60 + current_minute
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
    scene black with fade
    "Sabtu, 13 Desember 2025."
    scene kos_morning with fade
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
    scene kos_morning with fade
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
            scene kos_morning with fade
            return
        "Tidak":
            scene kos_morning with fade
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
    n "Namun, mekanik tidur di dalam game ini tidak hanya sekadar mendapatkan tidur yang cukup, tetapi juga mendapatkan tidur yang berkualitas dengan memperhatikan ritme sirkadian."
    n "Secara umum, untuk mendapatkan tidur yang berkualitas, pemain perlu tidur di malam hari."
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
    nvl clear

    n "Kemampuan"
    n "Game ini memiliki 2 tipe kemampuan, yaitu praktis dan menulis."
    n "Kemampuan praktis adalah pengetahuanmu terhadap bidang ilmu."
    n "Meningkatkan kemampuan ini dapat meningkatkan skor yang didapatkan dalam satu sesi menulis skripsi."
    n "Kemampuan menulis adalah pengetahuanmu terhadap cara menulis skripsi."
    n "Meningkatkan kemampuan ini dapat memperbanyak progress yang dihasilkan dalam satu sesi menulis skripsi."
    nvl clear

    n "Bonus progress skripsi, skor, dan xp yang didapatkan."
    n "Emosi dan tingkat kesadaran karakter dapat mempengaruhi progress skripsi, skor, dan xp yang didapatkan."
    n "Emosi yang positif dapat memberikan dampak yang positif, sedangkan emosi negatif akan memberikan dampak yang negatif pula."
    n "Selanjutnya tingkat kesadaran karakter dipengaruhi oleh beberapa hal."
    n "Pemenuhan kebutuhan tidur, dan ritme sirkadian."
    n "Secara umum, karakter akan lebih berenergi di pagi dan siang hari."
    n "Pemain juga bisa memberikan kesadaran lebih dengan minum kopi."
    n "Namun semakin sering minum kopi, karakter akan semakin toleran dan efek kesadaran dari kopi akan semakin lemah."
    n "Selain itu, minum kopi sebelum tidur juga akan mengganggu kualitas tidur."
    nvl clear

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
    scene black with fade
    "Deadline mengumpulkan proposal pun tiba."
    if thesis_fsm_state not in (THESIS_PROPOSAL_WRITING, THESIS_SEMPRO_READY):
        jump sempro_tidak_mengerjakan
    "Paijo mengumpulkan proposalnya dan kini menunggu hari yang dijadwalkan untuk sidang proposalnya."
    "Rabu, 21 Januari 2026."
    "Hari sidang proposal pun tiba."
    scene kos_morning with fade
    p "....."
    p "Udah waktunya sidang proposal."
    p "Bisa lah ya, lulus lah ya."
    if thesis_progress >= 100 or score > 40000:
        call sempro_a
    else:
        if score >= 36000:
            call sempro_ab
        elif score >= 32000:
            call sempro_b
        elif score >= 28000:
            call sempro_bc
        elif score >= 24000:
            call sempro_c
        elif score >= 20000:
            call sempro_d
        else:
            call sempro_e
    if thesis_fsm_state == THESIS_SEMPRO_FAILED:
        jump sempro_gagal
    $ thesis_advance_to(THESIS_POST_SEMPRO)
    jump post_sempro

label sempro_tidak_mengerjakan:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen calendar_now
    hide screen calendar_window
    hide screen game_maps
    scene kos_morning with fade
    "Hari sidang proposal."
    "Paijo duduk di tepi kasurnya, menatap layar laptop yang menyala."
    "Dokumen proposalnya terbuka."
    "Kosong."
    p "..."
    "Bukan kosong sepenuhnya, hanya ada nama dan NRP yang dia ketik tiga minggu lalu."
    "Tapi itu saja."
    "Tidak ada latar belakang. Tidak ada tinjauan pustaka. Tidak ada metodologi."
    "Hanya dua baris teks di atas halaman putih yang membentang panjang."
    p "..."
    p "Gua ga bisa ikut sempro hari ini."
    "Bukan pertanyaan. Bukan kepanikan."
    "Hanya sebuah kenyataan yang diucapkan dengan tenang, karena Paijo sudah tahu jawabannya sejak berminggu-minggu lalu."
    "Dia hanya tidak mau mengakuinya."
    "Notif.sfx"
    j "\"Jo, lo udah di jalan belum? Sempro lo kan jam 9.\""
    p "..."
    j "\"Jo?\""
    p "\"Jok, gua ga bisa ikut.\""
    j "\"Hah? Kenapa? Lo sakit?\""
    p "\"Bukan.\""
    p "\"Proposalnya... belum ada apa-apa.\""
    "Hening panjang di sisi lain."
    j "\"...serius?\""
    p "\"Iya.\""
    j "\"Jo...\""
    p "\"Gua tau.\""
    "Paijo menutup laptopnya."
    "Di luar, matahari sudah naik. Hari berjalan seperti biasa."
    "Hanya untuk Paijo, hari ini terasa seperti sebuah pintu yang menutup."
    scene kos_night with fade
    "Sore itu, koordinator mata kuliah mengirim pesan."
    "Paijo tidak menghadiri sempro. Nilainya E."
    "Proposal harus diulang di semester depan."
    p "..."
    p "Satu semester."
    p "Gua buang satu semester."
    "Tidak ada tangisan. Tidak ada amarah."
    "Hanya sunyi yang berat, dan kesadaran penuh bahwa semua ini adalah hasil dari pilihan-pilihannya sendiri."
    "Pilihan untuk menunda."
    "Pilihan untuk 'nanti'."
    "Pilihan untuk percaya bahwa masih ada waktu, sampai tiba-tiba tidak ada lagi."
    scene black with fade
    centered "{size=48}AKHIR{/size}\n\n{size=24}Paijo tidak mengumpulkan proposal.\nIa harus mengulang di semester berikutnya.{/size}"
    $ renpy.pause(3.0, hard=True)
    centered "{size=20}{i}Waktu yang terbuang tidak bisa dikembalikan.\nTapi hari esok masih bisa diisi dengan lebih baik.{/i}{/size}"
    $ renpy.pause(3.0, hard=True)
    scene black with fade
    return

label sempro_e:
    $ thesis_advance_to(THESIS_SEMPRO_FAILED)
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Ruangan seminar proposal terasa sangat sunyi."
    "Paijo berdiri di depan layar presentasinya, sebuah slide yang bahkan tidak bisa dia jelaskan sendiri."
    "Ketiga dosen penguji di hadapannya menatap dengan ekspresi yang sulit dibaca."
    d_uji "Silakan mulai, Mas."
    p "Ba... baik."
    p "Selamat pagi, perkenalkan saya Paijo dengan topik..."
    p "...topik..."
    "Paijo menelan ludah."
    d_uji "Lanjutkan, Mas."
    p "Topik penelitian saya adalah... tentang... sistem yang..."
    "Lima belas menit kemudian, sesi presentasi yang terlalu singkat selesai."
    "Kemudian datang sesi tanya jawab."
    d_uji "Apa problem statement dari penelitian Anda?"
    p "Problem statement-nya adalah... ehm..."
    d_uji "Apa kebaruan dari penelitian Anda dibanding paper yang sudah ada?"
    p "..."
    d_uji "Metode apa yang Anda rencanakan?"
    p "..."
    "Dosen ketua penguji akhirnya menutup kertas revisinya."
    d_uji "Mas, kami mohon Anda menunggu di luar sebentar."
    "Paijo keluar dengan kaki yang terasa berat."
    "Dari balik pintu, dia bisa mendengar bisikan dan suara ketukan pena."
    "Sepuluh menit berlalu."
    d_uji "Silakan masuk, Mas."
    d_uji "Dengan berat hati, kami tidak bisa meluluskan proposal ini."
    d_uji "Proposal Anda masih memerlukan perbaikan yang sangat mendasar, dari problem statement, tinjauan pustaka, hingga metodologi."
    d_uji "Kami harap Mas bisa berkonsultasi lebih intensif dengan dosen pembimbing dan mempersiapkan diri lebih baik untuk sempro berikutnya."
    p "..."
    p "Baik, Bu. Terima kasih atas masukannya."
    "Paijo keluar dari ruang seminar."
    "Langit di luar tetap biru seperti biasa."
    "Tapi rasanya hari ini jauh lebih berat dari seharusnya."
    return

label sempro_d:
    $ thesis_advance_to(THESIS_SEMPRO_FAILED)
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Paijo masuk ke ruang seminar dengan napas yang tidak karuan."
    "Proposalnya ada. Slidenya ada. Tapi entah mengapa, semuanya terasa tidak cukup."
    "Dan memang tidak cukup."
    "Presentasi berjalan cukup lancar di awal, tapi saat sesi tanya jawab dimulai, retakan mulai terlihat."
    d_uji "Kalau menggunakan metode ini, bagaimana cara Anda memvalidasi hasilnya?"
    p "Validasinya... ehm... menggunakan dataset yang tersedia?"
    d_uji "Dataset apa? Dari mana? Berapa besar?"
    p "..."
    d_uji "Apa kontribusi spesifik penelitian ini terhadap literatur yang sudah ada?"
    p "Kontribusinya adalah... penelitian ini belum pernah dilakukan sebelumnya?"
    d_uji "Sudah ada setidaknya tiga paper dengan topik serupa yang kami tahu. Anda sudah membaca ketiganya?"
    p "..."
    p "Belum, Bu."
    "Dosen kedua mencatat sesuatu."
    "Banyak sekali sesuatu."
    d_uji "Proposalnya masih perlu banyak perbaikan. Tinjauan pustakanya kurang mendalam, metodologinya masih kabur, dan justifikasinya belum kuat."
    d_uji "Kami tidak bisa meluluskan dalam kondisi ini."
    p "Baik, Pak. Terima kasih atas masukannya."
    "Paijo keluar dari ruangan."
    "Jantungnya masih berdegup kencang."
    "Setidaknya sekarang dia tahu dengan pasti apa yang harus diperbaiki."
    return

label sempro_c:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Paijo mendapatkan nilai C untuk seminar proposalnya."
    "Sesi tanya jawab tadi cukup berat."
    "Tapi Paijo berhasil menjawab sebagian pertanyaan, meskipun beberapa jawabannya masih tidak memuaskan."
    d_uji "Kami memutuskan meluluskan proposal ini dengan beberapa catatan revisi yang signifikan."
    d_uji "Tinjauan pustakanya perlu diperluas. Metodologinya perlu diperinci. Dan latar belakang masalahnya perlu diperkuat."
    d_uji "Kami harap revisi ini diselesaikan sebelum Mas mulai mengerjakan penelitiannya."
    p "Baik, Bu. Terima kasih atas masukannya."
    "Paijo keluar dengan formulir revisi setebal hampir sepuluh halaman di tangannya."
    p "..."
    p "Setidaknya lulus."
    return

label sempro_bc:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Paijo mendapatkan nilai BC untuk seminar proposalnya."
    "Presentasi berjalan cukup baik."
    "Paijo bisa menjawab sebagian besar pertanyaan dengan cukup memuaskan, meskipun beberapa masih kurang tajam."
    d_uji "Proposalnya sudah cukup baik. Ada beberapa hal yang perlu direvisi, terutama di bagian metodologi dan kerangka teori."
    d_uji "Tapi secara keseluruhan, arahnya sudah jelas."
    p "Terima kasih, Pak. Akan saya revisi sesuai catatan."
    "Paijo keluar dengan senyum tipis."
    "Tidak sempurna, tapi cukup."
    return

label sempro_b:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Paijo mendapatkan nilai B untuk seminar proposalnya."
    "Presentasi berjalan dengan baik."
    "Paijo menjawab semua pertanyaan dengan lancar, hanya ada satu atau dua yang perlu elaborasi tambahan."
    d_uji "Proposalnya sudah bagus. Ada beberapa catatan minor, penulisan di bagian metodologi bisa lebih sistematis, dan referensinya bisa ditambah yang lebih baru."
    d_uji "Tapi secara keseluruhan, kami puas dengan kesiapan Mas."
    p "Terima kasih banyak, Bu. Akan saya perbaiki."
    "Paijo keluar dengan langkah yang lebih ringan dari saat dia masuk."
    return

label sempro_ab:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Paijo mendapatkan nilai AB untuk seminar proposalnya."
    "Presentasi berjalan dengan sangat baik."
    "Paijo tampak percaya diri dan bisa menjawab semua pertanyaan dengan detail dan meyakinkan."
    d_uji "Proposalnya sangat baik. Tinjauan pustakanya komprehensif, metodologinya terstruktur, dan problem statement-nya jelas."
    d_uji "Hanya ada beberapa catatan kecil yang lebih bersifat penyempurnaan."
    p "Terima kasih, Pak. Saya akan segera memperbaikinya."
    d_uji "Kami nantikan hasil penelitiannya."
    "Paijo keluar ruangan dengan kepala tegak."
    "Kerja kerasnya terbayar."
    return

label sempro_a:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Paijo mendapatkan nilai A untuk seminar proposalnya."
    "Dia merasa sangat senang dan bangga karena dia berhasil mendapatkan nilai yang sangat baik untuk seminar proposalnya."
    "Presentasi tadi... berjalan luar biasa."
    "Paijo menjawab setiap pertanyaan dengan tepat dan percaya diri."
    "Bahkan dosen penguji yang biasanya paling kritis pun terlihat mengangguk-angguk puas."
    d_uji "Ini proposal yang sangat matang. Tinjauan pustakanya mendalam, metodologinya solid, dan kontribusi penelitiannya jelas."
    d_uji "Hampir tidak ada yang perlu direvisi. Kami sangat terkesan."
    p "..."
    p "Terima kasih banyak, Bu. Pak."
    d_uji "Kami tunggu hasil penelitiannya."
    "Paijo keluar ruangan."
    "Dia berdiri sejenak di depan pintu, memastikan bahwa semua ini nyata."
    p "..."
    p "Gua... lulus sempro dengan nilai A."
    "Senyum pelan-pelan merekah di wajahnya."
    return

label sempro_gagal:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen calendar_now
    hide screen calendar_window
    hide screen game_maps
    scene kos_afternoon with fade
    p "..."
    "Paijo duduk di tepi kasurnya, menatap lantai."
    "Formulir evaluasi sempro tergeletak di mejanya."
    "Di situ, dengan tulisan yang sangat jelas, tertera: TIDAK LULUS."
    p "..."
    p "Gua gagal sempro."
    "Kata-kata itu terasa berat di benaknya."
    "Selama ini dia sudah menunda, dan sekarang dia harus membayar harganya."
    "Notif.sfx"
    j "\"Jo, gimana sempro-nya?\""
    p "..."
    j "\"Jo?\""
    p "\"Ga lulus Jok.\""
    "Hening sejenak di sisi lain."
    j "\"Lu serius?\""
    p "\"Iya.\""
    j "\"Aduh Jo... Sori gua denger itu.\""
    j "\"Tapi... ya udah. Bukan akhir dari segalanya.\""
    p "\"Gampang ngomongnya lu.\""
    j "\"Iya gua tau. Tapi serius, ini bukan akhir. Banyak yang pernah di posisi lu dan akhirnya lulus juga.\""
    j "\"Yang penting sekarang, lu tau apa yang harus diperbaiki kan?\""
    p "..."
    p "\"Iya, dosen udah kasih banyak catatan.\""
    j "\"Nah, itu modal lu. Sekarang tinggal lu kerjain.\""
    j "\"Lu bukan ga bisa, Jo. Lu cuma kurang waktu dan persiapan kemarin.\""
    p "\"Hmmm.\""
    j "\"Ayo, jangan mager. Semester depan lu pasti bisa.\""
    "Paijo menaruh handphone-nya."
    "Dia menatap langit-langit kamarnya dalam keheningan yang panjang."
    scene kos_night with fade
    "Malam itu, Paijo tidak membuka laptopnya."
    "Bukan karena menyerah."
    "Tapi karena dia tahu, semester ini sudah selesai."
    "Seminar proposal yang gagal berarti satu hal: dia harus mengulang di semester depan."
    "Satu semester yang terbuang bukan karena tidak mampu, tapi karena menunda."
    p "..."
    p "Semester depan."
    p "Gua harus mulai dari awal lagi."
    "Paijo menutup mata."
    "Di balik kegelapan, dia sudah mulai menyusun rencana."
    scene black with fade
    centered "{size=48}AKHIR{/size}\n\n{size=24}Paijo gagal seminar proposal.\nIa harus mengulang di semester berikutnya.{/size}"
    $ renpy.pause(3.0, hard=True)
    centered "{size=20}{i}Terkadang, pelajaran terbesar datang dari kegagalan yang bisa kita hindari.{/i}{/size}"
    $ renpy.pause(3.0, hard=True)
    scene black with fade
    return

label post_sempro:
    "Setelah seminar proposal, Paijo merasa sangat lega dan senang karena dia berhasil melalui seminar proposal dengan baik."
    scene kos_afternoon with fade
    "Formulir revisi di tangannya tidak seberat yang dia bayangkan."
    "Yang penting, dia sudah melewati gerbang pertama."
    p "Akhirnya..."
    "Notif.sfx"
    j "\"Jo! Gimana sempro-nya?\""
    p "\"Lulus Jok.\""
    j "\"SERIUSAN?! Mantap kali lu Jo!\""
    p "\"Hehehe. Masih ada revisi sih.\""
    j "\"Ya iyalah, sempro mana yang ga ada revisi. Yang penting lulus dulu!\""
    j "\"Selamat ya Jo! Lu emang bisa kalo mau.\""
    p "\"Thanks Jok. Gua juga ga nyangka sih.\""
    j "\"Udah, sekarang istirahatin diri lu dulu. Besok baru lanjut revisi.\""
    p "\"Oke-oke.\""
    "Paijo menaruh handphone-nya dan merebahkan diri di kasur."
    "Langit-langit kamarnya terlihat sama seperti biasa."
    "Tapi entah mengapa, terasa lebih menyenangkan dari sebelumnya."
    p "..."
    p "Sekarang, tinggal skripsinya."
    "Masih panjang. Tapi setidaknya kini Paijo tahu dia bisa."

    $ score = 0
    $ thesis_progress = 0
    $ valence = 50
    $ arousal = 50
    $ physical_activity = 80
    $ nutrition = 30
    $ autonomy = 80
    $ process_s = 0.05
    $ competence = 80
    $ relatedness = 80
    $ current_day = 22
    $ current_month = 5
    $ current_hour = 9
    $ current_minute = 0
    $ wake_time_in_minute = current_hour * 60 + current_minute
    $ total_daily_time    = current_hour * 60 + current_minute
    $ set_cutscene_mode(False)
    jump kos

label sidang_akhir:
    scene black with fade
    "Deadline mengumpulkan skripsi pun tiba."
    "Paijo mengumpulkan skripsinya dan kini menunggu hari yang dijadwalkan untuk sidang akhirnya."
    "Rabu, 10 Juli 2026."
    "Hari sidang akhir pun tiba."
    scene kos_morning with fade
    p "....."
    p "Udah waktunya sidang akhir."
    p "....."
    if thesis_progress >= 100 or score > 40000:
        call sidang_akhir_a
    else:
        if score >= 36000:
            call sidang_akhir_ab
        elif score >= 32000:
            call sidang_akhir_b
        elif score >= 28000:
            call sidang_akhir_bc
        elif score >= 24000:
            call sidang_akhir_c
        elif score >= 20000:
            call sidang_akhir_d
        else:
            call sidang_akhir_e
    if thesis_fsm_state == THESIS_FAILED:
        jump sidang_akhir_gagal
    jump post_sidang_akhir

label sidang_akhir_a:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Presentasi tadi berjalan sempurna."
    "Paijo menjawab setiap pertanyaan dengan percaya diri, tepat, dan terstruktur."
    "Dosen pembimbing tersenyum tipis dari kursinya."
    "Para penguji terlihat terkesan, bukan hanya dengan hasilnya, tapi dengan cara Paijo memahami penelitiannya sendiri."
    d_uji "Penelitiannya solid. Kontribusinya jelas. Dan Anda bisa menjelaskannya dengan sangat baik."
    d_uji "Hampir tidak ada yang perlu kami tanyakan lebih lanjut."
    d_bim "Saya bangga dengan perkembangan Mas Paijo. Ini hasil yang luar biasa."
    d_uji "Kami sepakat memberikan nilai A."
    d_uji "Selamat, Sarjana."
    p "..."
    p "Terima kasih banyak, Pak. Bu."
    "Paijo keluar ruangan."
    "Tangannya masih sedikit gemetar."
    "Bukan karena gugup, tapi karena baru saja menyadari bahwa semuanya sudah selesai."
    return

label sidang_akhir_ab:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Presentasi berjalan sangat baik."
    "Paijo menjawab semua pertanyaan dengan lancar dan menunjukkan pemahaman yang mendalam terhadap topiknya."
    d_uji "Skripsinya sangat baik. Metodologinya kuat, analisisnya tajam."
    d_uji "Ada beberapa hal kecil yang bisa diperkuat di versi finalnya, terutama di bagian diskusi dan kesimpulan."
    d_uji "Tapi secara keseluruhan, kami sangat puas."
    d_bim "Kerja bagus, Mas. Saya yakin revisi minornya bisa diselesaikan cepat."
    p "Terima kasih, Pak. Bu. Akan saya perbaiki segera."
    d_uji "Selamat, Sarjana."
    "Paijo keluar dengan dada yang terasa lapang."
    return

label sidang_akhir_b:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Presentasi berjalan dengan baik."
    "Ada beberapa pertanyaan yang membuat Paijo berpikir lebih keras, tapi semuanya berhasil dijawab."
    d_uji "Skripsinya bagus. Beberapa bagian perlu diperkuat, analisisnya bisa lebih dalam, dan ada inkonsistensi kecil di bab tiga."
    d_uji "Kami juga ingin Anda memperluas pembahasan limitasi penelitian."
    p "Baik, Pak. Saya catat semuanya."
    d_bim "Revisinya tidak banyak, Mas. Fokus ke poin-poin yang disebutkan, selesaikan dalam dua minggu."
    d_uji "Setuju. Kami meluluskan dengan nilai B. Selamat, Sarjana."
    p "Terima kasih banyak."
    "Paijo keluar dengan formulir revisi yang tidak terlalu tebal."
    "Cukup untuk dikerjakan. Cukup untuk diselesaikan."
    return

label sidang_akhir_bc:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Presentasi berjalan cukup baik, tapi ada momen-momen di sesi tanya jawab yang membuat Paijo terpaksa menjawab lebih hati-hati."
    d_uji "Secara keseluruhan, skripsinya cukup. Tapi ada beberapa revisi yang cukup signifikan."
    d_uji "Bab dua perlu direstrukturisasi. Validasi hasilnya perlu diperkuat dengan data tambahan. Dan kesimpulannya terlalu umum."
    p "Baik, saya pahami. Akan saya perbaiki."
    d_bim "Mas Paijo, revisinya memang cukup banyak. Tapi saya yakin Anda bisa. Hubungi saya jika butuh arahan."
    d_uji "Kami meluluskan dengan nilai BC. Selamat, Sarjana. Selesaikan revisinya dengan baik."
    "Paijo keluar dengan catatan revisi yang cukup panjang di tangannya."
    "Tapi dia lulus."
    "Itu yang penting sekarang."
    return

label sidang_akhir_c:
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Sesi tanya jawab tadi berat."
    "Beberapa pertanyaan membuat Paijo terdiam cukup lama sebelum akhirnya menjawab, sebagian memuaskan, sebagian tidak."
    d_uji "Kami berdiskusi cukup lama untuk kasus ini."
    d_uji "Skripsinya memenuhi syarat minimal kelulusan, tapi masih banyak yang harus diperbaiki."
    d_uji "Metodologinya perlu direvisi ulang. Analisis datanya kurang mendalam. Dan tinjauan pustakanya sudah usang."
    d_uji "Kami memutuskan meluluskan dengan nilai C, dengan catatan revisi yang harus diselesaikan sebelum yudisium."
    d_bim "Mas Paijo, ini menjadi pelajaran berharga. Mari kita jadwalkan bimbingan intensif untuk menyelesaikan revisinya."
    p "Baik, Bu. Pak. Terima kasih atas kesempatannya."
    "Paijo keluar dengan tangan penuh catatan."
    "Lulus, tapi dengan banyak pekerjaan rumah yang masih menunggu."
    return

label sidang_akhir_d:
    $ thesis_advance_to(THESIS_FAILED)
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Sesi tanya jawab berjalan sangat sulit."
    "Paijo tidak bisa menjawab beberapa pertanyaan fundamental tentang penelitiannya."
    d_uji "Saya ingin memahami logika di balik metode yang Anda pilih. Bisa dijelaskan?"
    p "Metodenya... dipilih karena paling umum digunakan untuk kasus seperti ini."
    d_uji "Apa kriteria 'paling umum' itu? Anda sudah membandingkan dengan alternatif lainnya?"
    p "..."
    d_uji "Bagaimana Anda memvalidasi bahwa hasil Anda tidak bias?"
    p "..."
    "Para penguji saling bertukar pandang."
    "Dosen pembimbing menunduk."
    d_uji "Mas, kami mohon Anda menunggu di luar."
    "Lima belas menit berlalu dengan sangat panjang."
    d_uji "Kami tidak bisa meluluskan skripsi ini dalam kondisi saat ini."
    d_uji "Fondasi metodologisnya terlalu lemah. Ini bukan soal perbaikan minor, ini membutuhkan revisi substansial."
    d_bim "Mas Paijo, saya minta maaf. Kita harus bimbingan lebih intensif lagi. Saya akan bantu Anda melalui ini."
    p "..."
    p "Baik. Terima kasih."
    "Paijo keluar dari ruangan."
    return

label sidang_akhir_e:
    $ thesis_advance_to(THESIS_FAILED)
    scene expression selected_bidang.lower() + "_sidang" with fade
    "Dari menit pertama, semuanya sudah terasa tidak berjalan dengan baik."
    "Paijo tidak bisa menjawab pertanyaan pertama dari penguji."
    d_uji "Apa research gap yang Anda isi dengan penelitian ini?"
    p "Research gap-nya adalah... bahwa penelitian ini belum pernah dilakukan sebelumnya."
    d_uji "Berdasarkan apa? Anda sudah melakukan systematic literature review?"
    p "..."
    d_uji "Di halaman empat puluh dua, Anda menyebutkan metode X menghasilkan akurasi 87\%. Dari mana angka ini?"
    p "Dari... eksperimen yang saya jalankan."
    d_uji "Dataset-nya apa? Bagaimana Anda memastikan tidak ada data leakage?"
    p "..."
    "Dosen penguji kedua meletakkan skripsinya di meja."
    d_uji "Mas, jujur, apakah Anda benar-benar memahami apa yang Anda tulis di sini?"
    p "..."
    "Hening."
    "Hening yang sangat panjang."
    d_bim "..."
    d_uji "Kami sudahi sesi ini. Harap menunggu di luar."
    "Sepuluh menit kemudian."
    d_uji "Kami tidak bisa meluluskan. Skripsi ini membutuhkan perbaikan menyeluruh, bukan hanya revisi, tapi hampir penulisan ulang."
    d_uji "Kami harap Mas bisa memulai ulang dengan bimbingan yang lebih intensif."
    p "Baik. Terima kasih."
    "Paijo keluar."
    "Kakinya terasa sangat berat."
    return

label sidang_akhir_gagal:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen calendar_now
    hide screen calendar_window
    hide screen game_maps
    scene kos_afternoon with fade
    "Paijo duduk di kosnya, menatap layar laptop yang menyala."
    "Skripsinya terbuka di sana, ratusan halaman hasil kerja berbulan-bulan."
    "Dan hari ini, semuanya dinyatakan tidak cukup."
    p "..."
    p "Gua gagal sidang."
    "Bukan proposal. Bukan ujian tengah semester."
    "Sidang akhir."
    "Notif.sfx"
    j "\"Jo, gimana sidangnya?!\""
    p "..."
    j "\"Jo? Kok diem?\""
    p "\"Ga lulus Jok.\""
    "Hening cukup lama."
    j "\"...serius?\""
    p "\"Iya.\""
    j "\"Jo, gua minta maaf banget denger itu.\""
    j "\"Lu udah kerja keras banget selama ini.\""
    p "\"Kayaknya emang kurang keras.\""
    j "\"Bukan gitu. Lu udah jauh banget dari awal. Inget waktu lu ga tau mau ngapain sama skripsi lu?\""
    p "\"Iya.\""
    j "\"Sekarang lu udah punya ratusan halaman. Itu bukan hal kecil.\""
    j "\"Revisinya pasti berat. Tapi lu bukan orang yang ga bisa nyelesain ini.\""
    p "..."
    p "\"Iya Jok. Makasih.\""
    "Paijo menutup handphone-nya."
    "Dia membuka skripsinya lagi."
    "Bukan untuk dibaca."
    "Hanya untuk mengingatkan dirinya bahwa ini bisa diselesaikan."
    scene kos_night with fade
    "Malam itu, Paijo tidak tidur lebih awal."
    "Dia membaca catatan revisi dari para penguji, satu per satu."
    "Panjang. Berat. Tapi ada logikanya."
    p "Oke."
    p "Gua tau harus mulai dari mana."
    scene black with fade
    centered "{size=48}AKHIR{/size}\n\n{size=24}Paijo gagal sidang akhir.\nRevisi menanti. Wisuda harus ditunda.{/size}"
    $ renpy.pause(3.0, hard=True)
    centered "{size=20}{i}Kegagalan bukan lawan dari keberhasilan,\nkegagalan adalah bagian dari perjalanannya.{/i}{/size}"
    $ renpy.pause(3.0, hard=True)
    scene black with fade
    return

label post_sidang_akhir:
    $ thesis_advance_to(THESIS_DONE)
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen calendar_now
    hide screen calendar_window
    hide screen game_maps
    scene kos_morning with fade
    "Paijo berdiri di depan cermin."
    "Kemeja putih. Jas almamater. Dasi yang baru pertama kali dia pakai."
    p "..."
    p "Ini nyata."
    "Hari ini adalah hari wisuda."
    "Hari di mana semua yang dimulai dari malam itu, malam saat Joko mengingatkannya soal deadline sempro, akhirnya sampai ke titik ini."
    scene black with fade
    "Beberapa jam kemudian."
    "Di atas panggung, rektor menyebutkan namanya."
    "Paijo melangkah maju."
    "Toga di kepalanya. Ijazah di tangannya."
    p "..."
    "Satu langkah sederhana yang terasa seperti ujung dari perjalanan panjang."
    "Dan awal dari perjalanan yang baru."
    scene kos_afternoon with fade
    "Setelah acara, Paijo duduk di teras kos untuk terakhir kalinya."
    "Barang-barangnya sudah hampir semua terpak."
    "Notif.sfx"
    j "\"Jo! Selamat ya, S.Kom!\""
    p "\"Lu juga Jok. Kita lulus bareng.\""
    j "\"Gila ya. Dari yang lu panik ga ada topik, sampe sekarang.\""
    p "\"Haha. Iya. Ga nyangka juga.\""
    j "\"Lu tuh bukti kalo mau bisa.\""
    p "\"Asal ga nunda-nunda lagi.\""
    j "\"Wkwkwk. Iya dah. Oke Jo, see you di dunia nyata!\""
    p "\"See you Jok.\""
    "Paijo meletakkan handphone-nya."
    "Dia menatap langit-langit kamarnya untuk terakhir kali."
    "Tidak ada keajaiban. Tidak ada jalan pintas."
    "Hanya hari demi hari yang dikerjakan, satu per satu, sampai selesai."
    p "..."
    p "Makasih ya."
    scene black with fade
    centered "{color=#f5c518}{size=52}SELAMAT{/size}{/color}\n\n{size=28}Paijo Sarjana Komputer{/size}"
    $ renpy.pause(4.0, hard=True)
    centered "{size=20}Terima kasih sudah bermain {b}First Paper{/b}.\n\nSemoga perjalanan Paijo menginspirasi perjalananmu sendiri.{/size}"
    $ renpy.pause(4.0, hard=True)
    scene black with fade
    return

label kos:
    if pending_jump:
        $ _pj = pending_jump
        $ pending_jump = None
        jump expression _pj
    $ current_location = "kos"
    $ cg = current_location + "_" + time_of_day_state
    scene expression cg with fade
    $ time_stop = False
    # $ renpy.show(cg.lower())
    call screen interactive_kos

label dapur:
    if pending_jump:
        $ _pj = pending_jump
        $ pending_jump = None
        jump expression _pj
    $ current_location = "dapur"
    $ cg = current_location + "_" + time_of_day_state
    scene expression cg with fade
    $ time_stop = False
    # $ renpy.show(cg.lower())
    call screen interactive_dapur

label activity_kos_kasur:
    $ activity = None
    $ time_stop = True
    $ _m_tidur = get_activity_motivation("tidur")
    $ _l_tidur = get_activity_motivation_label("tidur")
    menu:
        "Mau Ngapain?"
        "Tidur (Motivasi: [_m_tidur]/[max_stat] - [_l_tidur])":
            $ activity = "tidur"
        "Batal":
            jump kos
    call process_activity
    jump kos

label activity_kos_laptop:
    $ activity = None
    $ time_stop = True
    $ _m_thesis     = get_activity_motivation("skripsi")
    #$ _m_workshop   = get_activity_motivation("workshop")
    $ _m_belajar_mandiri  = get_activity_motivation("belajar_mandiri")
    $ _m_jurnal     = get_activity_motivation("cari_jurnal")
    $ _m_chat_online = get_activity_motivation("chat_online")
    $ _m_main_game = get_activity_motivation("main_game")
    $ _l_thesis          = get_activity_motivation_label("skripsi")
    $ _l_belajar_mandiri = get_activity_motivation_label("belajar_mandiri")
    $ _l_jurnal          = get_activity_motivation_label("cari_jurnal")
    $ _l_chat_online     = get_activity_motivation_label("chat_online")
    $ _l_main_game       = get_activity_motivation_label("main_game")
    menu:
        "Mau Ngapain?"
        "Kerjakan Skripsi (Motivasi: [_m_thesis]/[max_stat] - [_l_thesis])":
            if not thesis_can_write():
                "Kamu belum mendapatkan topik untuk skripsimu, jadi kamu belum bisa mulai mengerjakan skripsimu."
                jump kos
            elif thesis_check_completion():
                jump kos
            $ activity = "skripsi"
        "Daftarkan Workshop":
            if not appt_is_booked("workshop"):
                "Kamu belum mendaftar ke workshop apapun."
                menu:
                    "Apakah kamu yakin ingin mendaftar workshop?"
                    "Ya":
                        $ appt_book("workshop")
                        "Workshop dijadwalkan besok tanggal [appt_workshop_day]/[appt_workshop_month]/[appt_workshop_year] pukul 10:00."
                        jump kos
                    "Tidak":
                        jump kos
            else:
                "Kamu telah mendaftar ke workshop."
                "Kamu dapat menghadiri workshop pada menu aktivitas di kos."
                jump kos
        "Belajar Mandiri (Motivasi [_m_belajar_mandiri]/[max_stat] - [_l_belajar_mandiri])":
            $ activity = "belajar_mandiri"
        "Ajukan Bimbingan Dengan Dosen":
            if not thesis_has_topic():
                "Kamu belum mendapatkan topik untuk skripsimu, jadi kamu belum bisa bimbingan."
                jump kos
            if not appt_is_booked("bimbingan"):
                "Kamu belum mengajukan jadwal bimbingan dengan dosen."
                menu:
                    "Apakah kamu yakin ingin mengajukan jadwal bimbingan?"
                    "Ya":
                        if current_hour >= 18 or current_hour < 7:
                            "Ga sopan amat ngechat dosen di luar jam kerja."
                            "Kalo mau chat dosen usahakan di jam kerja ya (pukul 7-18), biar dosennya juga ga terganggu."
                            jump kos
                        $ appt_book("bimbingan")
                        "Bimbingan dijadwalkan besok tanggal [appt_bimbingan_day]/[appt_bimbingan_month]/[appt_bimbingan_year] pukul 10:00."
                        jump kos
                    "Tidak":
                        jump kos
            else:
                "Kamu telah mengajukan jadwal bimbingan dengan dosen."
                "Kamu dapat melakukan bimbingan pada menu aktivitas di kos."
                jump kos
        "Cari Jurnal (Motivasi [_m_jurnal]/[max_stat] - [_l_jurnal])":
            $ activity = "cari_jurnal"
        "Chat Online (Motivasi [_m_chat_online]/[max_stat] - [_l_chat_online])":
            $ activity = "chat_online"
        "Main Game (Motivasi [_m_main_game]/[max_stat] - [_l_main_game])":
            $ activity = "main_game"
        "Batal":
            jump kos

    call process_activity
    jump kos

label activity_kos:
    $ activity = None
    $ time_stop = True
    $ _m_olahraga_ringan   = get_activity_motivation("olahraga_ringan")
    $ _m_olahraga_sedang   = get_activity_motivation("olahraga_sedang")
    $ _m_olahraga_berat    = get_activity_motivation("olahraga_berat")
    #$ _m_bimbingan  = get_activity_motivation("bimbingan")
    $ _m_sosialisasi  = get_activity_motivation("sosialisasi")
    $ _m_meditasi = get_activity_motivation("meditasi")
    $ _l_olahraga_ringan = get_activity_motivation_label("olahraga_ringan")
    $ _l_olahraga_sedang = get_activity_motivation_label("olahraga_sedang")
    $ _l_olahraga_berat  = get_activity_motivation_label("olahraga_berat")
    $ _l_sosialisasi     = get_activity_motivation_label("sosialisasi")
    $ _l_meditasi        = get_activity_motivation_label("meditasi")
    menu:
        "Mau Ngapain?"
        "Olahraga Ringan (Motivasi [_m_olahraga_ringan]/[max_stat] - [_l_olahraga_ringan])":
            $ activity = "olahraga_ringan"
        "Olahraga Sedang (Motivasi [_m_olahraga_sedang]/[max_stat] - [_l_olahraga_sedang])":
            $ activity = "olahraga_sedang"
        "Olahraga Berat (Motivasi [_m_olahraga_berat]/[max_stat] - [_l_olahraga_berat])":
            $ activity = "olahraga_berat"
        "Bimbingan dengan dosen" if appt_is_booked("bimbingan"):
            $ _time_diff = appt_get_time_diff("bimbingan")
            if _time_diff < 0:
                python:
                    _wait_m = -_time_diff
                    _wait_str = "{} jam {} menit".format(_wait_m // 60, _wait_m % 60) if _wait_m >= 60 else "{} menit".format(_wait_m)
                "Kamu masih ada waktu [_wait_str] sebelum bimbingan."
                "Apakah kamu ingin menunggu hingga waktu bimbingan tiba?"
                menu:
                    "Apakah kamu ingin menunggu hingga waktu bimbingan tiba?"
                    "Ya":
                        pass
                    "Tidak":
                        jump kos
                "Kamu menunggu [_wait_str] hingga waktu bimbingan tiba..."
                scene expression selected_bidang.lower() + "_sidang" with fade
                python:
                    advance_time(-_time_diff)
                    decrease_stats(-_time_diff)
            elif _time_diff >= 60:
                scene expression selected_bidang.lower() + "_sidang" with fade
                python:
                    _late_h = _time_diff // 60
                    _late_m = _time_diff % 60
                    _late_str = "{} jam {} menit".format(_late_h, _late_m)
                    store.competence  = max(0, store.competence  - 20)
                    store.relatedness = max(0, store.relatedness - 20)
                    store.valence     = max(0, store.valence     - 40)
                "Kamu terlambat [_late_str] dari jadwal bimbingan dan dosen sudah pergi!"
                "Bimbingan dengan dosen dibatalkan. Dosen pembimbingmu tidak bisa menunggumu lebih lama lagi!"
                $ appt_dismiss("bimbingan")
                jump kos
            elif _time_diff > 0:
                scene expression selected_bidang.lower() + "_sidang" with fade
                python:
                    _late_h = _time_diff // 60
                    _late_m = _time_diff % 60
                    _late_str = "{} jam {} menit".format(_late_h, _late_m) if _late_h > 0 else "{} menit".format(_late_m)
                    if _time_diff >= 30:
                        store.competence = max(0, store.competence - 10)
                        store.valence    = max(0, store.valence    - 20)
                    else:
                        store.competence = max(0, store.competence - 5)
                        store.valence    = max(0, store.valence    - 10)
                "Kamu terlambat [_late_str] dari jadwal bimbingan!"
                "Dosen pembimbingmu terlihat tidak senang dengan keterlambatanmu."
            $ appt_dismiss("bimbingan")
            $ activity = "bimbingan"
        "Hadiri Workshop" if appt_is_booked("workshop"):
            $ _time_diff = appt_get_time_diff("workshop")
            if _time_diff < 0:
                python:
                    _wait_m = -_time_diff
                    _wait_str = "{} jam {} menit".format(_wait_m // 60, _wait_m % 60) if _wait_m >= 60 else "{} menit".format(_wait_m)
                "Kamu masih ada waktu [_wait_str] sebelum workshop."
                "Apakah kamu ingin menunggu hingga waktu workshop tiba?"
                menu:
                    "Apakah kamu ingin menunggu hingga waktu workshop tiba?"
                    "Ya":
                        pass
                    "Tidak":
                        jump kos
                "Kamu menunggu [_wait_str] hingga waktu workshop tiba..."
                scene kelas with fade
                python:
                    advance_time(-_time_diff)
                    decrease_stats(-_time_diff)
            elif _time_diff > 0:
                scene kelas with fade
                python:
                    _late_h = _time_diff // 60
                    _late_m = _time_diff % 60
                    _late_str = "{} jam {} menit".format(_late_h, _late_m) if _late_h > 0 else "{} menit".format(_late_m)
                if _time_diff >= 120:
                    $ competence = max(0, competence - 25)
                    "Workshop sudah selesai dan kamu sangat terlambat, lebih dari 2 jam!"
                    $ appt_dismiss("workshop")
                    jump kos
                elif _time_diff >= 60:
                    $ competence = max(0, competence - 15)
                elif _time_diff >= 30:
                    $ competence = max(0, competence - 10)
                else:
                    $ competence = max(0, competence - 5)
                "Kamu terlambat [_late_str] dari jadwal workshop!"
                "Kamu merasa sedikit tertinggal dari materi workshop."
            $ appt_dismiss("workshop")
            $ activity = "workshop"
        "Sosialisasi dengan teman (Motivasi [_m_sosialisasi]/[max_stat] - [_l_sosialisasi])":
            $ activity = "sosialisasi"
        # "Just rest and do nothing":
        #     $ activity = "rest"
        "Meditasi (Motivasi [_m_meditasi]/[max_stat] - [_l_meditasi])":
            $ activity = "meditasi"
        "Skip time":
            $ activity = "skip"
        "Batal":
            jump kos
    
    call process_activity
    jump kos

label activity_dapur:
    $ activity = None
    $ time_stop = True
    $ _m_bergizi = get_activity_motivation("makan_bergizi")
    $ _m_enak    = get_activity_motivation("makan_enak")
    $ _m_kopi    = get_activity_motivation("minum_kopi")
    $ _l_bergizi = get_activity_motivation_label("makan_bergizi")
    $ _l_enak    = get_activity_motivation_label("makan_enak")
    $ _l_kopi    = get_activity_motivation_label("minum_kopi")
    menu:
        "Mau ngapain?"
        "Makan Bergizi (Motivasi [_m_bergizi]/[max_stat] - [_l_bergizi])":
            $ activity = "makan_bergizi"
        "Makan Enak Sembarangan (Motivasi [_m_enak]/[max_stat] - [_l_enak])":
            $ activity = "makan_enak"
        "Minum Kopi (Motivasi [_m_kopi]/[max_stat] - [_l_kopi])":
            $ activity = "minum_kopi"
        "Ga jadi":
            jump dapur

    call process_activity
    jump dapur

label activity_dapur_cheat:
    python:
        if thesis_fsm_state in (THESIS_EXPLORING, THESIS_SUPERVISED, THESIS_PROPOSAL_WRITING):
            thesis_advance_to(THESIS_SEMPRO_READY)
        elif thesis_fsm_state in (THESIS_POST_SEMPRO, THESIS_WRITING):
            thesis_advance_to(THESIS_DONE)
        store.thesis_progress = min(100, store.thesis_progress + 100)
        _activity_skripsi()

        _thesis_on_writing_tick()

        if store.thesis_progress >= 100 and thesis_fsm_state == THESIS_SEMPRO_READY:
            renpy.say(None, "Kamu sudah menyelesaikan semua yang bisa kamu kerjakan untuk proposalmu.")
            renpy.say(None, "Kamu bisa langsung melewati waktu ke hari deadline proposal untuk lanjut ke seminar proposal.")
            renpy.say(None, "Atau kamu bisa tetap melakukan aktivitas lain untuk meningkatkan skill praktis dan menulismu.")
        elif store.thesis_progress >= 100 and thesis_fsm_state == THESIS_DONE:
            renpy.say(None, "Kamu sudah menyelesaikan semua yang bisa kamu kerjakan untuk skripsimu.")
            renpy.say(None, "Kamu bisa langsung melewati waktu ke hari deadline skripsi untuk lanjut ke sidang akhir.")
    jump dapur

label process_activity:
    $ activity_data = activities[activity]
    $ min_dur = activity_data["min_duration"]
    $ max_dur = activity_data["max_duration"]
    $ def_h = activity_data["default_duration_hours"]
    $ def_m = activity_data["default_duration_minutes"]
    $ current_motivation_value = get_activity_motivation(activity)
    if current_motivation_value <= 20:
        "Kamu tidak termotivasi untuk melakukan aktivitas ini."
        return

    if min_dur == max_dur:
        if activity == "workshop":
            $ time_minutes = (12 - current_hour - 1) * 60 + (60 - current_minute)
        else:
            $ time_minutes = min_dur
    else:
        if activity == "tidur":
            $ hours_input = renpy.input("Kamu akan tidur berapa jam? (Min: {} - Max: {})".format(format_duration(min_dur), format_duration(max_dur)), default=str(def_h))
            $ minutes_input = renpy.input("Berapa menit?", default=str(def_m))
            $ hours = int(hours_input) if hours_input.isdigit() else def_h
            $ hours = max(min_dur // 60, min(max_dur // 60, hours))
            $ minutes = int(minutes_input) if minutes_input.isdigit() else def_m
            $ time_minutes = hours * 60 + minutes
            $ time_minutes = max(min_dur, min(max_dur, time_minutes))
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

    if activity not in ["bimbingan", "workshop"]:
        "Yakin mau melakukan aktivitas ini?"
        menu:
            "Yakin mau melakukan aktivitas ini?"
            "Yakin":
                pass
            "Tidak":
                return

    $ delay_batch = max(1, time_minutes // 30)

    python:
        activity_fsm_start(activity)
        for minutes_activity in range(time_minutes + 1):
            if interrupted:
                break
            activity_fsm_tick()
            if minutes_activity % delay_batch == 0:
                renpy.pause(delay=delay)
            if current_motivation_value <= 60:
                if renpy.random.random() < (1 - current_motivation_value / 100.0) / 20.0:
                    renpy.say(None, "Kamu merasa sudah cukup melakukan aktivitas ini.")
                    interrupted = True
                    break
        activity_fsm_stop()

    # Show completion messages
    if activity == "skripsi":
        "Kamu mengerjakan skripsi selama [minutes_activity] menit."
        "Kamu mendapatkan [int(earned_score)] poin!"
        $ earned_score = 0
    elif activity == "bimbingan":
        if not thesis_advisor_approved():
            "Kamu bimbingan dengan dosen selama [minutes_activity] menit, namun topikmu belum disetujui."
            "Dosen menyarankan untuk memperdalam pemahamanmu tentang topik yang kamu pilih dan kembali lagi nanti."
            $ thesis_advance_to(THESIS_EXPLORING)
        else:
            "Kamu bimbingan dengan dosen selama [minutes_activity] menit. Kamu memperoleh kejelasan dan arah!"
    elif activity == "cari_jurnal":
        if not thesis_has_topic():
            "Kamu belum berhasil menemukan topik proposal yang kamu pahami."
        "Kamu mencari dan membaca jurnal selama [minutes_activity] menit. Kamu mendapatkan ilmu baru."
    else:
        $ renpy.say(None, activities[activity]["completion_message"].format(minutes=minutes_activity))

    $ interrupted = False
    return

# # Random event system - 1% chance after any activity
# label check_random_event:
#     $ random_chance = renpy.random.randint(1, 100)
#     if random_chance > 1:
#         call random_event
#     return

# label random_event:
#     $ set_cutscene_mode(True)  # Enter cutscene mode to hide UI
#     $ event_type = renpy.random.choice(["lucky_find", "unexpected_visitors", "inspiration", "small_accident"])
    
#     if event_type == "lucky_find":
#         "While going about your day, you find a useful reference article on the ground!"
#         "It turns out to be exactly what you needed for your thesis."
#         $ thesis_progress = min(100, thesis_progress + 3)
#         $ competence = min(max_stat, competence + 5)
#         "You gained 3 thesis progress and 5 competence!"
    
#     elif event_type == "unexpected_visitors":
#         "Someone knocks on your door - it's an old friend you haven't seen in a while!"
#         "They came to surprise you with a visit."
#         $ relatedness = min(max_stat, relatedness + 15)
#         $ valence = min(max_stat, valence + 10)
#         "You gained 15 relatedness and 10 valence!"
    
#     elif event_type == "inspiration":
#         "A sudden flash of inspiration hits you!"
#         "You feel motivated to work on your thesis right now."
#         $ motivation = min(100, motivation + 20)
#         $ competence = min(max_stat, competence + 5)
#         "You gained 20 motivation and 5 competence!"
    
#     elif event_type == "small_accident":
#         "Oh no! You accidentally spilled water on your notes."
#         "You'll need to redo some of your work."
#         $ thesis_progress = max(0, thesis_progress - 2)
#         $ valence = max(0, valence - 10)
#         "You lost 2 thesis progress and 10 valence!"
    
#     $ set_cutscene_mode(False)  # Exit cutscene mode after event
#     return