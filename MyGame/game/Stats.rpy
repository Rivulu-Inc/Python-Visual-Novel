screen Progress():
     frame:
         xalign 0.5 ypos 25
         button:
             action Show('Stats')
             text _("View Stats") style "button_text"
screen Stats():
    modal True
    frame:
        xalign 0.5 ypos 25 xpos 60
        button:
            action Hide('Stats')
            text _("Return") style "button_text" size 30
    frame:
        #background "image.png"
        xalign 0.5 ypos 160 xpos 400
        vbox:
            text "Money=[Money]":
                size 30
            text "Army=[Army]":
                size 30
            text "Health=[Health]":
                size 30
            text "Mana=[Mana]":
                size 30
            text "Morale=[Morale]":
                size 30
    frame:
        xalign 0.5 ypos 90 xpos 800
        text "Skills":
            size 30
    frame:
        xalign 0.5 ypos 90 xpos 400
        text "Details":
            size 30
    frame:
        xalign 0.5 ypos 160 xpos 800
        vbox:
            text "Magic=[Magic]":
                size 30
            text "Weapon=[Weapon]":
                size 30
            text "Instinct=[Instinct]":
                size 30
            text "Skill1=[Skill1]":
                size 30
            text "Skill2=[Skill2]":
                size 30
            text "Elite Skill=[Elite_Skill]":
                size 30
