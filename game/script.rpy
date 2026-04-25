# Label to start the game
label start:
    "Welcome to the Thesis Writing Simulator!"
    "You are a graduate student working on your thesis."
    "Manage your wellbeing, skills, and motivation to complete your thesis successfully!"
    "Click on interactive areas or the button to perform activities."

    # Show all screens
    show screen main_stats
    show screen detailed_stats_window
    show screen calendar_now
    show screen calendar_window
    
    call screen interactive_room

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