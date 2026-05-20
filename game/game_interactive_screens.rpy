# Imagemap for interactive areas (always visible)
screen interactive_kos():
    # Main room imagemap
    imagemap:
        ground "bg kos"  # Your background image
        hover "bg kos_hover"  # Optional: hover overlay image
        
        # Define clickable hotspots (x, y, width, height)
        # Adjust these coordinates to match your background image
        
        # Example: Click on desk area to open activity menu
        hotspot (800, 400, 200, 150) action SetVariable("show_activity_menu", True)
        
        # You can add more hotspots for different interactions
        # Example: Click on bed for rest activities
        # hotspot (100, 300, 150, 200) action Jump("rest_activities")
        
        # Example: Click on bookshelf for academic activities
        # hotspot (1200, 200, 180, 300) action Jump("academic_activities")
    
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
        action Jump("activity_kos")

    textbutton "Map":
        xalign 0.95
        yalign 0.85
        xsize 200
        ysize 60
        text_size 22
        action Show("game_maps")

# Imagemap for interactive areas (always visible)
screen interactive_dapur():
    # Main room imagemap
    imagemap:
        ground "bg dapur"  # Your background image
        hover "bg dapur_hover"  # Optional: hover overlay image
        
        # Define clickable hotspots (x, y, width, height)
        # Adjust these coordinates to match your background image
        
        # Example: Click on desk area to open activity menu
        hotspot (800, 400, 200, 150) action SetVariable("show_activity_menu", True)
        
        # You can add more hotspots for different interactions
        # Example: Click on bed for rest activities
        # hotspot (100, 300, 150, 200) action Jump("rest_activities")
        
        # Example: Click on bookshelf for academic activities
        # hotspot (1200, 200, 180, 300) action Jump("academic_activities")
    
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
        action Jump("activity_dapur")

    textbutton "Map":
        xalign 0.95
        yalign 0.85
        xsize 200
        ysize 60
        text_size 22
        action Show("game_maps")

screen game_maps():
    zorder 2
    modal True

    frame:
        xalign 0.5 yalign 0.5
        xsize 600
        ysize 800
        padding (20, 20)
        
        vbox:
            text "Tempat yang Dapat Dikunjungi" xalign 0.5 size 30
            null height 30
            
            for dest in locations[current_location]["explorable"]:
                $ loc_name = locations[dest]["name"]
                textbutton "[loc_name]" action Function(move_to_map, dest)
            
            null height 30
            textbutton "Tutup Map":
                action Hide("game_maps")
                xalign 0.5