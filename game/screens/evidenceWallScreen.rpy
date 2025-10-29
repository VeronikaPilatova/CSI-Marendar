screen evidenceWallScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "bg/bg evidenceWall.png"

        button:
            xpos 50
            ypos 950
            text "Promluvit si s kolegy"
            action Jump ("guardhouseAgain")

        for note in notes:
            if note.isActive:
                imagebutton:
                    xpos note.x
                    ypos note.y
                    tooltip note.name
                    hover note.buttonImage
                    idle note.buttonImage
                    action Return(note.code)

        if seeMeNote:
            if "out of office" not in rauvin.status:
                imagebutton:
                    xpos 600
                    ypos 300
                    tooltip "Vzkaz od Rauvina"
                    hover "button seeme"
                    idle "button seeme"
                    action Return("seeMe")
            else:
                imagebutton:
                    xpos 600
                    ypos 300
                    tooltip "Vzkaz od Soliana"
                    hover "button seeme solian"
                    idle "button seeme solian"
                    action Return("seeMe")
            

        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]":
                xalign 0.02
                yalign 0.02
