label start:
    scene training center
    with fade
    show screen Progress
    "Chapter 1"
    "Today, is the day you complete your mage training
    and head out into the world to see what it holds for you"
    $ y=renpy.input('What is your name?')
    show r at right
    show y at left
    r '[y], come here'
    r 'it is the time you get your own Evil slaying weapon before leaving this institute'
    r 'You also get to know your inner magic known today'
    r 'But never forget that a mage"s weapon is always his mind'
    r 'Call your team too for this'
    y 'Sure Sir!'
    hide r
    hide y
    'You go to call your friends who are in their institute rooms, packing'
    show y at left
    show j at right
    y 'Guys! Trainer Ray is calling all of us for the Graduation ceremony'
    j 'I think i will really miss this institute'
    y 'Same here bro'
    y 'At least all 4 of us will be a team'
    hide j
    show s at right
    s 'Exactly!'
    hide s
    show l at right
    l 'Come on guys, we have to go before Trainer Ray comes after us'
    hide l
    hide y
    "You and your team slowly make your way to the great hall, where Sir Ray is waiting"
    show r at right
    r 'Welcome, Mages of the future'
    r 'this is a mage"s true calling
    to rid this world of all the evil creatures
    left after the Great War'
    r 'This is the time, to find your inner magic'
    r 'close your eyes and concentrate'
    r 'focus on your core'
    show y at left
    menu:
        r 'What do you feel?'
        'Wet and Fluid':
            r 'Your magic is of the element water'
            $Magic = 'Water'
        'Dry and scorching':
            r 'Your magic is of the fire element'
            $Magic = 'Fire'
        'restless and raging':
            r 'Your magic is of the air element'
            $Magic = 'Air'
        'Fresh and Natural':
            r 'Your magic is of the Earth element'
            $Magic = 'Earth'
    hide y
    r 'Know that as you become more powerful, your magic type will change'
    r 'Now that every one has got to know their inner magic, it is recive your weapons'
    r 'follow me mages'
    hide r
    'You and your team follow Trainer Ray to the weaponary'
    'Trainer Ray randomly picks up some strange looking swords and hands it out'
    show r at right
    show j at left
    j 'Sir, what are these sword made from?'
    r 'these are made from a special metal called StarStone, which is extremly potent against creatures of darkness'
    hide j
    r 'Grab a sword and test its balance'
    hide r
    'you look at all the swords, and pick one up. It feels a bit heavy, so you put it back again.
    after checking some more swords, you finally pick a sword which is perfectly balanced'
    show r at right
    r 'Perfect guys, now the last thing before you head out'
    r 'it is time to choose your runes'
    show s at left
    s 'Are we finally get our own permanent spell rune Sir?'
    r 'Of course [s]'
    s 'How will we get new runes Sir?'
    r 'Whenever a monster is defeated, it drops a rune'
    hide s
    r 'Guys, Now pick your first rune'
    r 'Use your magic to absorb the rune'
    r 'it will then vanish, and whenever you draw the rune symbol, you can channel your magic through it'
    hide r
    'You pick up the rune, a shimmering block of wood, with a strange symbol carved into it'
    'it feels soft to touch'
    show r at right
    r 'Now slowly channel your magic into in [y]'
    hide r
    'You focus your [Magic] magic on the rune and with a burst of light it vanishes'
    'You picture your rune and draw the symbol'
    'It leaves behind a glittring irdsent'
    show r at right
    show y at left
    r 'Do you recognise this symbol [y]?'
    y 'Yes Sir, this is a healing rune'
    r 'Good!'
    r 'Now this is your starting rune, but you will get more as you travel'
    hide r
    hide y
    'Your team finishes collecting their runes and heads out of the institute behind Trainer Ray'
    show r
    r 'Good work on completing your training mages'
    r 'Please do not get killed'
    r 'the future of the mages is in your hands'
    r 'Good Bye!'
    show y
    y 'Good Bye Trainer Ray!,We will miss you'
    hide r
    hide y
    'You and your team, slowly walk away from the institute, and stop
    to look back, thinking off all the memories of the past 5 years you spent here'

    #call Minigame
