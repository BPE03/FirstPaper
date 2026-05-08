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
    p "....."
    p "Bangun pagi ku terus...."
    p "Ngerjain skripsi."
    p "...."
    p "Oalah pantes"

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

label sempro:
    "Hari seminar proposal pun tiba."
    "Paijo merasa sangat gugup dan tidak percaya diri karena dia belum menyelesaikan proposalnya."
    "Namun, dia tahu bahwa dia harus menghadapi kenyataan dan melakukan yang terbaik dalam seminar proposalnya."
    scene black with fade
    return

label post_sempro:
    "Setelah seminar proposal, Paijo merasa sangat lega dan senang karena dia berhasil melalui seminar proposal dengan baik."

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

# Main gameplay loop
label activity_kos:
    $ activity = None
    menu:
        "Mau Ngapain?"

        "Work on thesis (Requires motivation > 30)":
            $ activity = "thesis"

        "Olahraga":
            $ activity = "olahraga"
        
        "Meet with advisor":
            $ activity = "advisor"
        
        "Socialize with friends":
            $ activity = "socialize"
        
        "Take a nap":
            $ activity = "nap"
        
        "Sleep (Full sleep cycle)":
            $ activity = "sleep"
        
        "Attend a workshop / Learn new skills":
            $ activity = "workshop"
        
        "Practice self-directed learning":
            $ activity = "selflearn"
        
        "Just rest and do nothing":
            $ activity = "rest"
        
        "Skip time":
            $ activity = "skip"

        "Cancel":
            jump kos
    
    call process_activity
    jump kos

label activity_dapur:
    $ activity = None
    menu:
        "Mau ngapain?"

        "Makan Bergizi":
            $ activity = "makan_bergizi"
        
        "Makan Enak Sembarangan":
            $ activity = "makan_enak"

        "Buat Kopi":
            $ activity = "buat_kopi"

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
        if activity == "sleep":
            $ hours_input = renpy.input("How many hours will you sleep? (Min: {} - Max: {})".format(format_duration(min_dur), format_duration(max_dur)), default=str(def_h))
            $ hours = int(hours_input) if hours_input.isdigit() else def_h
            $ hours = max(min_dur//60, min(max_dur//60, hours))
            $ time_minutes = hours * 60
        else:
            $ hours_input = renpy.input("How many hours will you spend on this activity? (Min: {} - Max: {})".format(format_duration(min_dur), format_duration(max_dur)), default=str(def_h))
            $ minutes_input = renpy.input("How many additional minutes?", default=str(def_m))
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
    
    # Special handling for sleep activity - uses dedicated sleep mechanic
    if activity == "sleep":
        $ sleep_hours = time_minutes // 60
        "You head to bed for the night..."
        "Zzzzzzz... [sleep_hours] hours of sleep..."
        $ perform_sleep(sleep_hours)
        scene black with fade
    # Loop through each minute for other activities
    else:
        "You spend [time_minutes] minutes on this activity..."
        python:
            for i in range(time_minutes):
                advance_time(1)
                decrease_stats(1)
                
                if activity == "thesis":
                    if motivation > 30:
                        store.thesis_progress = min(100, store.thesis_progress + 1/60)
                        decrease_stats(1)  # No additional decrease for thesis work
                        store.writing_xp += 25/60
                        store.practical_xp += 15/60
                
                elif activity == "makan_bergizi":
                    store.nutrition = min(store.max_stat, store.nutrition + 50/20)
                    store.valence = max(0, store.valence - 6/60)

                elif activity == "makan_enak":
                    store.nutrition = min(store.max_stat, store.nutrition + 50/20)
                    store.valence = min(store.max_stat, store.valence + 40/20)
                    store.autonomy = min(store.max_stat, store.autonomy + 10/20)
                    store.physical_activity = max(0, store.physical_activity - 6/60)

                elif activity == "buat_kopi":
                    store.caffeine_level = min(100, store.caffeine_level + 20/15)
                    store.arousal = min(store.max_stat, store.arousal + 25/15)
                
                elif activity == "olahraga":
                    store.physical_activity = min(store.max_stat, store.physical_activity + 30/60)
                    store.arousal = min(store.max_stat, store.arousal + 15/60)
                    #store.valence = min(store.max_stat, store.valence + 10/60)
                
                elif activity == "advisor":
                    #store.autonomy = min(store.max_stat, store.autonomy + 15)
                    store.competence = min(store.max_stat, store.competence + 10/60)
                    store.relatedness = min(store.max_stat, store.relatedness + 20/60)
                    store.valence = min(store.max_stat, store.valence + 15/60)
                    store.arousal = min(store.max_stat, store.arousal + 10/60)
                    store.writing_xp += 10
                    store.practical_xp += 5
                
                elif activity == "socialize":
                    store.relatedness = min(store.max_stat, store.relatedness + 30/60)
                    store.valence = min(store.max_stat, store.valence + 20/60)
                
                elif activity == "nap":
                    store.arousal = min(store.max_stat, store.arousal + 25/60)
                    store.valence = min(store.max_stat, store.valence + 10)
                
                elif activity == "workshop":
                    store.practical_xp += 15/20
                    store.writing_xp += 10/20
                    store.competence = min(store.max_stat, store.competence + 60/60)
                    store.arousal = max(0, store.arousal - 10/60)
                
                elif activity == "selflearn":
                    store.autonomy = min(store.max_stat, store.autonomy + 20/60)
                    store.writing_xp += 8/20
                
                elif activity == "rest":
                    store.arousal = min(store.max_stat, store.arousal + 10/60)
                    store.valence = min(store.max_stat, store.valence + 5/60)

                delay = 0.5/time_minutes
                renpy.pause(delay, hard=True)  # Small pause to allow UI to update each minute
            
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
    
    elif activity == "olahraga":
        "You olahragad for [time_minutes] minutes. You feel refreshed and energized!"
    
    elif activity == "advisor":
        "You met with your advisor for [time_minutes] minutes. You gained clarity and direction!"
    
    elif activity == "socialize":
        "You spent time with friends for [time_minutes] minutes. You feel connected and happy!"
    
    elif activity == "nap":
        "You took a nap for [time_minutes] minutes. You feel more alert now!"

    elif activity == "makan_bergizi":
        "You ate a nutritious meal for [time_minutes] minutes. Your nutrition improved!"

    elif activity == "makan_enak":
        "You enjoyed some tasty food for [time_minutes] minutes. Your mood lifted, but you skipped some olahraga."

    elif activity == "buat_kopi":
        "You brewed a coffee for [time_minutes] minutes. Your caffeine and alertness increased!"
    
    elif activity == "sleep":
        $ sleep_hours = time_minutes // 60
        $ circadian_quality = get_sleep_quality_factor()
        if circadian_quality >= 1.3:
            "You had a wonderful night's sleep! You feel completely refreshed!"
        else:
            "You woke up feeling reasonably rested."
        "Adenosine level: [int(adenosine_level)], Sleep debt: [int(sleep_debt)] hours"
    
    elif activity == "workshop":
        "You attended a workshop for [time_minutes] minutes. Your skills improved!"
    
    elif activity == "selflearn":
        "You studied independently for [time_minutes] minutes. You feel more in control!"
    
    elif activity == "rest":
        "You rested for [time_minutes] minutes."
    
    elif activity == "skip":
        "You skipped [time_minutes] minutes."
    
    # Check for random event (1% chance)
    call check_random_event
    
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
    call screen interactive_kos

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