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
    show text "First Paper"
    $ renpy.pause(5.0, hard=True) # Matches the transition time
    show text "Dikembangkan oleh: Bimantara Putra Ernandra" with fade
    $ renpy.pause(5.0, hard=True) # Matches the transition time
    scene kos with fade
    "Sabtu, 13 Desember 2025."
    "Hari ini adalah hari di mana Paijo memulai perjalanannya untuk menyelesaikan proposalnya."
    "Bantu Paijo kelola waktunya dengan baik, jaga kesehatan fisik dan mentalnya, dan kembangkan keterampilannya agar dia bisa menyelesaikan proposalnya tepat waktu!"

    # Show all screens
    show screen main_stats
    show screen detailed_stats_window
    show screen calendar_now
    show screen calendar_window
    
    call screen interactive_room

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
    $ valence = 20
    $ arousal = 80
    $ physical_activity = 20
    $ nutrition = 15
    $ autonomy = 20
    $ competence = 20
    $ current_hour = 12
    scene black with fade
    return

label prologue_lanjut_besok:
    "Paijo memutuskan untuk istirahat dan melanjutkan pencarian referensi untuk proposalnya besok."
    "Tentu saja hal ini tidak membuatnya merasa lebih baik, karena dia tahu bahwa deadline seminar proposal semakin dekat."
    "Namun, dia merasa bahwa dia tidak bisa memaksakan dirinya untuk terus mencari referensi ketika dia sudah sangat lelah."
    scene black with fade
    return

# Main gameplay loop
label main_gameplay:
    menu:
        "What would you like to do?"
        
        "Work on thesis (Requires motivation > 30)":
            if motivation > 30:
                $ thesis_progress = min(100, thesis_progress + 2)
                $ competence = min(max_stat, competence + 1)
                $ writing_xp += 10
                $ practical_xp += 5
                $ update_levels()
                $ arousal = max(0, arousal - 5)
                $ nutrition = max(0, nutrition - 3)
                $ update_motivation_and_progress()
                "You worked on your thesis. Progress made!"
            else:
                "You're too unmotivated to work effectively right now."
        
        "Eat a healthy meal":
            $ nutrition = min(max_stat, nutrition + 35)
            $ valence = min(max_stat, valence + 5)
            $ update_motivation_and_progress()
            "You ate a nutritious meal. You feel better!"
        
        "Exercise / Go for a walk":
            $ physical_activity = min(max_stat, physical_activity + 30)
            $ arousal = min(max_stat, arousal + 15)
            $ valence = min(max_stat, valence + 10)
            $ update_motivation_and_progress()
            "You exercised. You feel refreshed and energized!"
        
        "Meet with advisor":
            $ autonomy = min(max_stat, autonomy + 15)
            $ competence = min(max_stat, competence + 10)
            $ relatedness = min(max_stat, relatedness + 20)
            $ practical_xp += 5
            $ update_levels()
            $ update_motivation_and_progress()
            "You met with your advisor. You gained clarity and direction!"
        
        "Socialize with friends":
            $ relatedness = min(max_stat, relatedness + 30)
            $ valence = min(max_stat, valence + 20)
            $ update_motivation_and_progress()
            "You spent time with friends. You feel connected and happy!"
        
        "Take a nap":
            $ arousal = min(max_stat, arousal + 25)
            $ valence = min(max_stat, valence + 10)
            $ update_motivation_and_progress()
            "You took a nap. You feel more alert now!"
        
        "Attend a workshop / Learn new skills":
            $ practical_xp += 15
            $ writing_xp += 10
            $ update_levels()
            $ competence = min(max_stat, competence + 10)
            $ arousal = max(0, arousal - 10)
            $ update_motivation_and_progress()
            "You attended a workshop. Your skills improved!"
        
        "Practice self-directed learning":
            $ autonomy = min(max_stat, autonomy + 20)
            $ writing_xp += 8
            $ update_levels()
            $ update_motivation_and_progress()
            "You studied independently. You feel more in control!"
        
        "Just rest and do nothing":
            $ arousal = min(max_stat, arousal + 10)
            $ valence = min(max_stat, valence + 5)
            $ update_motivation_and_progress()
            "You took some time to rest."
        
        "Cancel":
            call screen interactive_room
    call screen interactive_room

# Burnout ending
label burnout:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen interactive_room
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
            jump start
        
        "No, quit":
            "Thanks for playing!"
            return

# Thesis completion ending
label thesis_complete:
    hide screen main_stats
    hide screen detailed_stats_window
    hide screen interactive_room
    hide screen calendar_now
    hide screen calendar_window
    
    scene bg graduation with dissolve
    
    centered "{color=#2ecc71}{size=50}CONGRATULATIONS!{/size}{/color}\n\nYou've completed your thesis!"
    centered "Through managing your wellbeing and developing your skills,\nyou've achieved your academic goal!"
    
    "Final Stats:"
    "Practical Skill Level: [practical_level]"
    "Writing Skill Level: [writing_level]"
    "Final Motivation: [motivation]"
    
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
            jump start
        
        "No":
            "Thanks for playing!"
            return