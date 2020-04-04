define f = Character('Fae Leader')
define E = Character('Evil Twin')
define h = Character('Human Leader')
define end = 0
 # Water Magic
 # Fire Magic
 # Air Magic
 # Earth magic
 # Physic magic
 # Metal Magic
 # Dawn Magic
 # Dusk Magic
define Money = 0000
define Health = 100
define Mana = 00
define Army = 00
define Morale = 10
###################
define Magic = 'Locked'
define Weapon = 'Locked'
define Instinct = 'Locked'
define Skill1 = 'Locked'
define Skill2 = 'Locked'
define Elite_Skill = 'Locked'
####################
label start:
    scene bg I
    with fade
    show screen Progress
    'Prologue'
    'The Fall Of The Fae Empire'
    'Location: Crystal Tomb'
    'Date:10 Dynasty Years'
    show f
    with dissolve
    f 'Finally, The day I have been waiting for.'
    f 'Its time to unlock the crystal tomb'
    f 'And free our creator,The great ... Who has been trapped here
    by his evil twin,.... after the great purge, When he was expelled back
    to his dimention'
    scene bg I
    'The Fae Leader starts chanting in a strange language and the army behind
    him starts taking up the chant when suddenly'
    hide f
    show h at right
    with dissolve
    h 'Wait! Stop!'
    hide h
    show f
    with dissolve
    f 'Who are you to tell me to stop,Human? Your army is defeated
    and we are freeing our creator at last. Be sure he will punish you
    after he is free'
    hide f
    show h
    with dissolve
    h 'No,you guys are mistaken. Stop your chanting right now...'
    scene bg I
    'The crystal explodes as the powerful spell frees the prisoner,trapped inside the crystal'
    show h
    with dissolve
    h'Noo....'
    scene bg I
    'A Huge Monsterous humanoid creature rises towards the sky'
    show E
    with dissolve
    E 'Finally! I have been freed! HA HA HA'
    hide E
    show f happy
    with dissolve
    f 'But..But You are not our creator'
    hide f
    show E
    with dissolve
    E 'I Never said i was!'
    hide E
    show f sad
    with dissolve
    f 'But then what happened to our creator?'
    hide f
    show E
    with dissolve
    E 'You see, it was quite simple. Just before i was trapped into that horrible
    dimontion, I swapped places with him. I knew you guys will try to free the creator
    based on the tales my faithful ones wrote'
    hide E
    show f
    with dissolve
    f 'Your faithful ones?'
    'As one, a group of people from both humans and the fae walk to the side of evil t'
    f 'You Tratiors!'
    hide f
    show h
    with dissolve
    h 'We knew something like this would happen,That is why we fought to keep the fae away
    from the crystal'
    hide h
    show f
    with dissolve
    f 'We are so sorry, It was nice knowing you'
    hide f
    show E
    with dissolve
    E 'Calm down! That was a bit too dramatic!The world will not be recreated today'
    E 'I Am inviting all of you to join me to step into a better world'
    E 'I will be back'
    scene bg I
    'The evil t flicked his finger, teleporting his followers'
    show E
    with dissolve
    E 'But i have a last present to give you guys'
    scene bg I
    'An Arrow punched the hearts of the Human and Fae clan leaders, instantly killing them'
    show E
    with dissolve
    E 'Bye!! Seen you soon'
    hide E
    'The twin vanished without a trace'
    #call Minigame
