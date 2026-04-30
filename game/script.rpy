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
    $ sleep = 50
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
    $ activity = None
    menu:
        "What would you like to do?"
        
        "Work on thesis (Requires motivation > 30)":
            $ activity = "thesis"
        
        "Eat a healthy meal":
            $ activity = "eat"
        
        "Exercise / Go for a walk":
            $ activity = "exercise"
        
        "Meet with advisor":
            $ activity = "advisor"
        
        "Socialize with friends":
            $ activity = "socialize"
        
        "Take a nap":
            $ activity = "nap"
        
        "Attend a workshop / Learn new skills":
            $ activity = "workshop"
        
        "Practice self-directed learning":
            $ activity = "selflearn"
        
        "Just rest and do nothing":
            $ activity = "rest"
        
        "Skip time":
            $ activity = "skip"

        "Cancel":
            $ activity = "cancel"
    
    if activity == "cancel":
        call screen interactive_room
    
    # Ask for time
    $ time_input = renpy.input("How many minutes will you spend on this activity?", default="60")
    $ time_minutes = int(time_input) if time_input.isdigit() else 60
    if time_minutes <= 0:
        $ time_minutes = 60
    
    # Set base minutes for scaling
    if activity == "thesis":
        $ base_minutes = 60
    elif activity == "eat":
        $ base_minutes = 30
    elif activity == "exercise":
        $ base_minutes = 60
    elif activity == "advisor":
        $ base_minutes = 60
    elif activity == "socialize":
        $ base_minutes = 60
    elif activity == "nap":
        $ base_minutes = 60
    elif activity == "workshop":
        $ base_minutes = 120
    elif activity == "selflearn":
        $ base_minutes = 60
    elif activity == "rest":
        $ base_minutes = 60
    elif activity == "skip":
        $ base_minutes = 1  # doesn't matter
    
    $ per_scale = 1.0 / base_minutes
    
    # Loop through each minute
    python:
        for i in range(time_minutes):
            advance_time(1)
            decrease_stats(1)
            
            if activity == "thesis":
                if motivation > 30:
                    store.thesis_progress = min(100, store.thesis_progress + 2 * per_scale)
                    store.competence = min(store.max_stat, store.competence + 1 * per_scale)
                    store.writing_xp += 10 * per_scale
                    store.practical_xp += 5 * per_scale
                    store.arousal = max(0, store.arousal - 5 * per_scale)
                    store.nutrition = max(0, store.nutrition - 3 * per_scale)
            
            elif activity == "eat":
                store.nutrition = min(store.max_stat, store.nutrition + 50 * per_scale)
            
            elif activity == "exercise":
                store.physical_activity = min(store.max_stat, store.physical_activity + 30 * per_scale)
                store.arousal = min(store.max_stat, store.arousal + 15 * per_scale)
                store.valence = min(store.max_stat, store.valence + 10 * per_scale)
            
            elif activity == "advisor":
                store.autonomy = min(store.max_stat, store.autonomy + 15 * per_scale)
                store.competence = min(store.max_stat, store.competence + 10 * per_scale)
                store.relatedness = min(store.max_stat, store.relatedness + 20 * per_scale)
                store.practical_xp += 5 * per_scale
            
            elif activity == "socialize":
                store.relatedness = min(store.max_stat, store.relatedness + 30 * per_scale)
                store.valence = min(store.max_stat, store.valence + 20 * per_scale)
            
            elif activity == "nap":
                store.arousal = min(store.max_stat, store.arousal + 25 * per_scale)
                store.valence = min(store.max_stat, store.valence + 10 * per_scale)
            
            elif activity == "workshop":
                store.practical_xp += 15 * per_scale
                store.writing_xp += 10 * per_scale
                store.competence = min(store.max_stat, store.competence + 10 * per_scale)
                store.arousal = max(0, store.arousal - 10 * per_scale)
            
            elif activity == "selflearn":
                store.autonomy = min(store.max_stat, store.autonomy + 20 * per_scale)
                store.writing_xp += 8 * per_scale
            
            elif activity == "rest":
                store.arousal = min(store.max_stat, store.arousal + 10 * per_scale)
                store.valence = min(store.max_stat, store.valence + 5 * per_scale)
            
            # For skip, no effects
    
    # Update levels and motivation after loop
    if activity in ["thesis", "advisor", "workshop", "selflearn"]:
        $ update_levels()
    
    $ update_motivation_and_progress()
    
    # Show messages
    if activity == "thesis":
        if motivation > 30:
            $ earned_score = calculate_thesis_score()
            "You worked on your thesis for [time_minutes] minutes. Progress made!"
            "You earned [earned_score] points!"
        else:
            "You're too unmotivated to work effectively right now."
    
    elif activity == "eat":
        "You ate a nutritious meal for [time_minutes] minutes. You feel better!"
    
    elif activity == "exercise":
        "You exercised for [time_minutes] minutes. You feel refreshed and energized!"
    
    elif activity == "advisor":
        "You met with your advisor for [time_minutes] minutes. You gained clarity and direction!"
    
    elif activity == "socialize":
        "You spent time with friends for [time_minutes] minutes. You feel connected and happy!"
    
    elif activity == "nap":
        "You took a nap for [time_minutes] minutes. You feel more alert now!"
    
    elif activity == "workshop":
        "You attended a workshop for [time_minutes] minutes. Your skills improved!"
    
    elif activity == "selflearn":
        "You studied independently for [time_minutes] minutes. You feel more in control!"
    
    elif activity == "rest":
        "You rested for [time_minutes] minutes."
    
    elif activity == "skip":
        "You skipped [time_minutes] minutes."
    
    # Fast-forward effect
    "Time passes quickly..."
    $ renpy.pause(0.5)
    
    # Check for random event (1% chance)
    call check_random_event
    
    call screen interactive_room

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
            $ score = 0
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