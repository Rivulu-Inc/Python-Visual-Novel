define r = Character('Sir Raymond')
define f = Character('Fae Clan Representative')
define e = Character('Elven Clan Representative')
define d = Character('Dwarven Clan Representative')

 # Water Magic
 # Fire Magic
 # Air Magic
 # Earth magic
 # Physic magic
 # Metal Magic
 # Dawn Magic
define Money = 1000
define Health = 100
define Army = 0
define Mana = 100

label start:
 scene bg Isle of peace
 with fade
 label Prologue:
     show screen Progress
     'PROLOGUE'
     'Isle of peace, 1 Feb, 19 Dynasty years'
     'It was a cold foggy night. An assembly of all the clan Chieftains was called,
     to the storm castle to discuss the terms of the peace treaty between the various factions of the humans,
     the fae and the other inhabitants of this land'
     'you are currently playing as Sir Raymond, a representative of the Human clans'

 scene throne room
 with fade
 show r grim
 r 'This is what the human clans have decided: What you ask of the world
 is madness'
 r 'We will not give up our magic'
 r 'all our clans apart from the dragon clan stands with us on this matter'
 r 'even the elven clans and dwarven clan stand with us'
 menu:
     'Bribe the elven and dwarven clans to stand with you to gain more allies!'
     'I will ask (500 coins)':
         $Money-=100
         $Army+=5
         e 'We pledge to stand with you dear humans!
         All our armies are in your disposal'
         e 'We just want territories for our own in the mountains'
         d 'We second that!'
     "Never Mind, i don't have money":
         e 'We will try stand with you, but some of our clans may not join you'
         d 'And we will be neutral in this fight'
         $Army+=1
 call Minigame
 'Nice Game, Right :D'
