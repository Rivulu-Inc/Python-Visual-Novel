label Minigame:
    python:
        List=['p','y','t','h','o','n']
        L2=['p','_','_','_','_','n']
        renpy.say(None,"""Welcome To Hang-Man
You have 10 Chances to guess a word
Press Enter To Continue""")
        guess=10
        while guess>0:
            b=renpy.input("""Enter Alphabet
Press Enter To Continue""")
            b=b.strip()
            if b in List:
                a=List.index(b)
                L2[a]=b
                L3=''.join(L2)
                renpy.say(None,"""letter Found!
This is the Word [L3]""")
            else:
                L3=''.join(L2)
                renpy.say(None,"""Letter Not Found
This is the Word [L3]""")
            if List == L2:
                break
        if guess>0:
            renpy.say(None,'You won!!')
        else:
            renpy.say(None,'You Lost')
    return
label minigame2:
    python:
        import random
        renpy.say(None,'Welcome to: Guess the Number!!:')
        a=random.randint(0,10)
        b=renpy.input("Enter Number")
