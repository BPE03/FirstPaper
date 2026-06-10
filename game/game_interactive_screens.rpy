# Imagemap for interactive areas (always visible)
screen interactive_kos():
    $ _kos_bg    = "kos_" + time_of_day_state
    $ _kos_hover = "kos_" + time_of_day_state + "_hover"
    zorder -1
    # Main room imagemap
    imagemap:
        ground _kos_bg
        hover _kos_hover
        
        # Define clickable hotspots (x, y, width, height)
        # Adjust these coordinates to match your background image
        hotspot (0, 0, 900, 1080) action Jump("activity_kos_kasur") sensitive not (show_calendar or show_map)
        hotspot (1050, 500, 450, 300) action Jump("activity_kos_laptop") sensitive not (show_calendar or show_map)
        # hotspot (0, 0, 900, 1080) action Jump("activity_kos_kasur") sensitive not (show_detailed_stats or show_calendar or show_map)
        # hotspot (1050, 500, 450, 300) action Jump("activity_kos_laptop") sensitive not (show_detailed_stats or show_calendar or show_map)
    
    # Optional: Show a button overlay if you want a visible button
    # You can remove this if you want just invisible hotspots
    # imagebutton:
    #     xalign 0.95
    #     yalign 0.95
    #     idle "gui/button/do_something_idle.png"  # Replace with your image
    #     hover "gui/button/do_something_hover.png"  # Replace with your image
    #     action SetVariable("show_activity_menu", True)
    
    # Alternative text button (remove if using image button above)
    textbutton "Lakukan Sesuatu":
        xalign 0.95
        yalign 0.95
        xsize 200
        ysize 60
        text_size 22
        sensitive not (show_calendar)
        action Jump("activity_kos")
        background Frame("#1a1a1acc", 8, 8)
        hover_background Frame("#3a3a3aee", 8, 8)
        insensitive_background Frame("#1a1a1a66", 8, 8)

    # textbutton "Map":
    #     xalign 0.95
    #     yalign 0.85
    #     xsize 200
    #     ysize 60
    #     text_size 22
    #     sensitive not (show_detailed_stats or show_calendar)
    #     action Show("game_maps")

    imagebutton:
        xalign 0.78
        yalign 0.1
        idle "icon_map1.png"  # Replace with your image
        hover "icon_map1.png"  # Replace with your image
        action ToggleVariable("show_map")

# Imagemap for interactive areas (always visible)
screen interactive_dapur():
    $ _dapur_bg    = "dapur_" + time_of_day_state
    $ _dapur_hover = "dapur_" + time_of_day_state + "_hover"
    zorder -1
    # Main room imagemap
    imagemap:
        ground _dapur_bg
        hover _dapur_hover
        
        # Define clickable hotspots (x, y, width, height)
        # Adjust these coordinates to match your background image
        # hotspot (0, 610, 1220, 470) action Jump("activity_dapur") sensitive not (show_detailed_stats or show_calendar or show_map)
        # # Cheat to skip thesis progress
        # hotspot (1529, 459, 117, 98) action Jump("activity_dapur_cheat") sensitive not (show_detailed_stats or show_calendar or show_map)
        hotspot (0, 610, 1220, 470) action Jump("activity_dapur") sensitive not (show_calendar or show_map)
        # Cheat to skip thesis progress
        # hotspot (1529, 459, 117, 98) action Jump("activity_dapur_cheat") sensitive not (show_calendar or show_map)

    imagebutton:
        xalign 0.75
        yalign 0.1
        idle "icon_map1.png"  # Replace with your image
        hover "icon_map1.png"  # Replace with your image
        action ToggleVariable("show_map")

    # Alternative text button (remove if using image button above)
    # textbutton "Map":
    #     xalign 0.95
    #     yalign 0.85
    #     xsize 200
    #     ysize 60
    #     text_size 22
    #     sensitive not (show_detailed_stats or show_calendar)
    #     action Show("game_maps")