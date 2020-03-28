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
        xalign 0.5 ypos 100
        vbox:
            text "Money=[Money]":
                size 30
            text "Army=[Army]":
                size 30
            text "Health=[Health]":
                size 30
            text "Mana=[Mana]":
                size 30
