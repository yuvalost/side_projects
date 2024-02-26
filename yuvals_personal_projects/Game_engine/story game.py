import time
you=input("before we start....whats your name?   ")
town_name = input("give the town you're from a name? ")


def intro():
    print(f"You are the sheriff in the quaint town of {town_name}, \n")
    print("where the air is always filled with the sweet scent of blossoms, \n")
    print(f'and the streets are lined with charming shops. You are the protector of the town, Sheriff {you}.\n')
    print("One day, a notorious gang led by Billy the Bitch has shown up, causing trouble in the town.\n")
    print("His gang started to harass the townsfolk. As the sheriff, you decide to intervene.\n")
    print(f"{you} say: Stop this nonsense! This is my town, and I won't tolerate such behavior!\n")
    print("You need to decide how to confront the gang and restore peace to the town.\n")
    print("What will you do?\n")
    print("1. Confront Billy the Bitch and his gang head-on with force.")
    print("2. Try to negotiate a truce with Billy the Bitch and his gang.")
    print(f"3. Hesitate and retreat to a different part of {town_name}.")

    decision = input("Enter the number of your decision: ")

    if decision == "1":
        confront_billy()

    elif decision == "2":
        negotiate_billy()

    elif decision == "3":
        abandoned_house()

    else:
        intro()

def confront_billy():
    print("You decide to confront Billy the Bitch and his gang by drawing your gun and opening fire.\n")
    print("One gang member gets hit, and the rest flee, including Billy, who always manages to escape.\n")
    print("Billy the Bitch yells, 'Why did you shoot me?'\n")
    print(f"{you}: Because I'm not like you.\n")
    print("The rest of the town reacts with surprise, 'Ooh, burn!'\n")
    print("Billy the Bitch responds, 'Okay, now it's personal!'\n")
    print("He takes out his gun and starts shooting at you. You return fire, and the whole town takes cover.\n")
    print("A chaotic shootout ensues. You manage to take down a few gang members,\n"
          "but their gunfire is accurate, and you get severely wounded.\n"
          "You fall to the ground, staring at the sky, realizing your fate.\n"
          "Billy the Bitch and his gang laugh, continuing their mischief.\n")
    print("However, you wake up, shocked that you're still alive. The town appears abandoned.\n"
          "You muster your last strength to get up, bewildered by your survival.\n"
          f"You think, 'How is this possible, and where is everyone?'\n")
    print("What will you do?")
    print(f"1. Look around the town of {town_name}.")
    print("2. Run away to find answers elsewhere.")

    decision = input("Enter the number of your decision: ")

    if decision == "1":
        print(f"You realize your wounds have miraculously healed. Curious for answers, you search the town and hear a voice"
              f" coming from the old saloon. You cautiously approach for some answers.")
        abandoned_house()
    elif decision == "2":
        print("You spot an abandoned horse nearby and decide to ride away in search of answers.")
        new_town()
    else:
        print("Invalid choice!")
        confront_billy()




def negotiate_billy():
    print("You decide to attempt a risky negotiation with Billy the Bitch and his gang...\n"
          "Surprisingly, they agree to listen, and you join the gang in one unexpected event.\n"
          "After it's all done, Billy asks you to join his gang and fight as an outlaw. You contemplate and decide it's your destiny.\n")
    print("What do you want to do?")
    print("1. Join the gang as an outlaw, embracing this new path.")
    print("2. Reject Billy's offer and fight against him to uphold justice.")

    decision = input("Enter the number of your decision: ")

    if decision == "1":
        print(f"{you} say, 'I'm in! Let's make this gang the best it can be.' But there's a problem: Billy.\n"
              f"You don't need him. You pull out your gun and shoot Billy. The rest of the gang is shocked by your actions.\n"
              f"You look at them and declare, 'Now it's just me and the gang.'\n"
              f"But suddenly, one of the gang members starts acting strangely. His eyes turn white, and his body transforms into a half-man, half-bear.")
        half_man_half_bear()
    elif decision == "2":
        print(f"You take your gun out and shoot Billy. The rest of the gang is shocked by your actions.\n"
              f"You look at them and declare, 'Now it's just me and the gang.'\n"
              f"But suddenly, one of the gang members starts acting strangely. His eyes turn white, and his body transforms into a half-man, half-bear.")
        half_man_half_bear()
    else:
        negotiate_billy()


def half_man_half_bear():
    print("The creature declares, 'Finally, I'm free! Billy put a stupid spell on me. No more leaders, I'm going to kill everyone!' *Meow*.\n"
          "You realize you only have one bullet left, and the sky turns red. The rest of the gang looks hopeless as the half-man-half-bear meows at you.\n")
    print("The creature continues, 'I'll let you survive, but you must eat one person from your gang!'")
    print("What will you do?")
    print("1. Eat a gang member.")
    print("2. Face the half-man-half-bear.")

    decision = input("Enter the number of your decision: ")

    if decision == "1":
        eat_gang_member()
    elif decision == "2":
        print("You take out your gun, but you remember you have only one bullet left.\n"
              "The creature laughs at you and says, 'Take your shot... only a spell can kill me.'")
        print("One of the gang members takes out a D&D dice and suggests, 'To put a spell on the half-man-half-bear, you need to roll above 10. Do you take the chance?'")
        print("What will you do?")
        print("1. Roll the dice.")
        print("2. Shoot the gang member and eat him.")

        decision = input("Enter the number of your decision: ")

        if decision == "1":
            print(f"You say, 'I live for these moments... let's do it.'")

            import random

            def throw_dice():
                return random.randint(1, 20)

            num_throws = 1  # Change this to the desired number of dice throws

            for _ in range(num_throws):
                result = throw_dice()
                print("Dice rolled:", result)
                if result >= 10:
                    print("You beat the half-man-half-bear! The curse slowly disappears, and the creature turns into a little boy.")
                    print("The boy looks at you and says, 'You have freed me from my curse, and I can be a boy again!'")
                    print(f"You say, 'But you were an adult before... you've been in an... event.'")
                    print("A gang member suggests, 'Let's shoot him.'")
                    print("What will you do?")
                    print("1. Shoot the kid.")
                    print("2. Let the kid live.")

                    decision = input("Enter the number of your decision: ")

                    if decision == "1":
                        print(f"You take out your pistol and shoot the kid with your last bullet.")
                        print(f"You smile, because you're sick and think it's funny.\n"
                              f"As the kid slowly dies, you decide to leave the gang and start a new life as a cowboy.")
                        abandoned_house()
                    elif decision == "2":
                        print(f"The gang members look at each other and decide to make the kid the gang leader.")
                        print(f"They make you leave {town_name} town, as the gang led by the kid takes over.")
                        abandoned_house()

                else:
                    print("The gang members look at you slowly and say, 'We always loved your... personality!'")
                    print("As the half-man-half-bear slowly approaches you, you realize your fate.")
                    print("Do you want to try again? (y/n)")
                    decision = input("Enter the number of your decision: ")

                    if decision == "y":
                        intro()
                    else:
                        print("Thanks for playing.")
        elif decision == "2":
            eat_gang_member()
    else:
        half_man_half_bear()

def eat_gang_member():
    print("You line up the gang as they start crying for their lives.")
    print(f"{you} say, 'Okay, since I only know you from... previous events, state your name and why I shouldn't eat you.'\n")
    print("Gang Member 1: 'Yo, gather 'round, let me tell you a tale. My name is John the Fun, a name known to all.'")
    print("Gang Member 2: 'I will tell you my life story! My name is Bob. With a hat and boots, I'd ride the range, but...'")
    print("Bob continues, 'But Bob soon realized it wasn't right. To steal and fight, causing fright. He chose a path of kindness and grace, left the gang, found a better place. Cowboy Bob, he turned it around, helped folks smile in his hometown.'")
    print("Gang Member 3: 'I'm Yosi the Crazy. Kill me, just kill me! I'm sorry, I'm just having a bad day...'")
    print("Yosi continues, '...started with an event where girls just didn't show up, and now, one guy I had... interactions with is some kind of bear-man... like what is this? You know Jesse likes kids! Eat him.'")
    print("Jesse: 'My name is Jesse... Wait, what!? I only like kids because of the happy meals...'")
    print("Jesse continues, 'Om, Jesse Messy here, in those wild, olden days, gang life stirred trouble in twisted arrays. Under the moon's eerie gleam, a dark pact grew...'")
    print(f"{you} say, 'The rest are dead... Who will you eat?'")

    print("1. Eat Gang Member John the Fun.")
    print("2. Eat Gang Member Bob.")
    print("3. Eat Gang Member Yosi the Crazy.")
    print("4. Eat Gang Member Jesse the Messy.")
    print("5. Eat Gang Member Jimmy Knife.")

    decision = input("Enter the number of your decision: ")

    if decision == "1":
        print("John the Fun's last words: 'Ride on, partners, but remember my grin, In these desert depths, my tale begins and ends.'")
        print(f"You shoot John the Fun and start eating him...")
        print("The rest of the gang starts cheering you on, saying: 'You can do it, {you}! We believe in you!'")
        print("But suddenly, the half-man-half-bear charges at you with ferocity...")
        print("You engage in a fierce battle for survival, but it's evident you're outmatched. Just as you realize it's the end,")
        print("a shot goes through the half-man-half-bear's head. Confused, you look around to see a man calling you from the saloon.")
        crazy_cowboy()

    elif decision == "2":
        print("Bob: 'Okay...' You shoot Bob and start eating him...")
        print("The rest of the gang starts cheering you on, saying: 'You can do it, {you}! We believe in you!'")
        print("But suddenly, the half-man-half-bear charges at you with ferocity...")
        print("You engage in a fierce battle for survival, but it's evident you're outmatched. Just as you realize it's the end,")
        print("a shot goes through the half-man-half-bear's head. Confused, you look around to see a man calling you from the saloon.")
        crazy_cowboy()

    elif decision == "3":
        print("Yosi the Crazy: 'What is wrong with you...? Well okay...' You shoot Yosi and start eating him...")
        print("The rest of the gang starts cheering you on, saying: 'You can do it, {you}! We believe in you!'")
        print("But suddenly, the half-man-half-bear charges at you with ferocity...")
        print("You engage in a fierce battle for survival, but it's evident you're outmatched. Just as you realize it's the end,")
        print("a shot goes through the half-man-half-bear's head. Confused, you look around to see a man calling you from the saloon.")
        crazy_cowboy()

    elif decision == "4":
        print("Jesse the Messy: 'Across the time's river, I rode back to save Yosi from being eaten...'")
        print("You shoot Jesse and start eating him...")
        print("The rest of the gang starts cheering you on, saying: 'You can do it, {you}! We believe in you!'")
        print("But suddenly, the half-man-half-bear charges at you with ferocity...")
        print("You engage in a fierce battle for survival, but it's evident you're outmatched. Just as you realize it's the end,")
        print("a shot goes through the half-man-half-bear's head. Confused, you look around to see a man calling you from the saloon.")
        crazy_cowboy()

    elif decision == "5":
        print("Jimmy Knife shoots you... As you look up, you see an angel laughing at you.")
        print("The angel says, 'Try again?'")
        print("1. Try again.")
        print("2. Just die.")

        decision = input("Enter the number of your decision: ")

        if decision == "1":
            intro()
        else:
            print("Thanks for playing.")

def crazy_cowboy ():
        print(f"as {you} and the rest of the gang walk in the saloon,\n you look around and see the the saloon is empty"
              f" the cowboy in the saloon looks at you with his crazy eyes\n")
        print(f"{you} ask's the cowboy whats his name\n , so he answers: call me Blaze....and i want to know who shot my brother"
              f"Billy the bitch... ")
        print(f" the room was even more quite than before,\n"
              f"one of the gang member replied: ohhh snap it the new guy {you} who took his place as our gang leader\n")
        print(f"{you} answers: well thats how we do stuff now in the bitch gang...\n")
        print(f" Blaze looks around and spit to the floor, the tension rises in the saloon\n "
              f"Blaze says: well well.... looks like a shoot out is called for ")
        print(f"1. shoot out it is")
        print(f"2. ask a gang member to give blaze a blow job")
        print(f"3. run and leave the outlaw life behind\n")


        decision = input("Enter the number of your decision: ")

        if decision == "1":
                print(f"blaze says: i will return tomrrow at 7 am, after i kill you my vengeance will end here\n")
                print(f"{you} and the gang start the last party with every drink in the saloon, it's now 2 am and everyone pass out"
                      f"except for you\n for some reason you hear a weird sound coming from the next room decision time!!")
                print(f"1. go back to sleep and get ready for the shoot out")
                print(f"2. run away and leave the outlaw life")
                print(f"3. check the sound for the next room")

                decision = input("Enter the number of your decision: ")

                if decision == "1":
                    shootout()

                elif decision == "2":
                    print(" quietly you leave as you dont wake up anyone....\n")
                    abandoned_house()

                elif decision == "3":
                    print(f"you walk towards the sound, it sounds like banging. you say to yourself: probably another fight in the gang\n ")
                    print(f"you open the door from where the sound comes from and a flash shows up while green monsters show up,\n "
                          f"the say the want to take you to their mothership!!!")
                    print("as much as you fight the want to abduct you!!!\n no bullets left you cant fight them\n")
                    alien()
                else:
                    crazy_cowboy()

        elif decision == "2":
                print("Blaze thinks about it and says: im not gay as my brother we shall wait for tomorrow shoot out")
                shootout()
        elif decision == "3":
                print("you wait for night time to quietly you leave as you dont want to wake up anyone....\n")
                abandoned_house()
        else:
            crazy_cowboy()


def alien():
    print("As the green aliens surround you, their technology immobilizes you. You struggle against their grasp,")
    print("but their advanced tools render you powerless. With a blinding flash, you're transported onto their spaceship.\n")

    print("Inside the spacecraft, you find yourself in a sterile chamber filled with pulsating lights and unfamiliar machinery.")
    print("You're probed and examined by the aliens, who communicate in strange electronic chirps and clicks.")
    print("Despite the language barrier, their intentions appear curious rather than malicious.\n")
    print("After what feels like hours, you're brought before a serene and wise-looking alien elder.")
    print("'We seek to understand your world,' the elder conveys in a soothing, echoing tone.'\n")
    print("You lose consciousness and awaken to find yourself in your bed with two attractive women.")
    print("You notice that you feel strange.")
    print("Both women say: 'We have learned much from you. As a token of gratitude, we shall return you to your home.'")
    print("With another flash of light, you find yourself back in the desert, the aliens gone.")
    print("The memory of your abduction remains vivid, a testament to the uncharted frontiers of the cosmos.\n")
    third_town_coward()

def shootout():
    print(f"It's 7 am and you step outside, finding yourself in the dusty streets of {town_name}. ")
    print("Rumors have been circulating about this shootout between you and the dangerous gunslinger named Blaze, who's been causing trouble. All townspeople come to see.")
    print("Once Blaze notices you, his eyes lock on you.\n")
    print(f"Blaze stands up, a sinister grin on his face. 'Well, well, if it isn't the new sheriff {you}.")
    print("'I heard you've got a quick draw. Let's settle this now, the cowboy way.'\n")
    print("You feel the weight of your six-shooter at your side. The townspeople gather around, eager to witness the showdown.")
    print("The tension in the air is palpable as the minutes tick by, bringing you closer to the fateful duel.\n")

    print("The clock strikes 7:01, and the sun beats down as you and Blaze stand facing each other.")
    print("Your fingers twitch above your holster, ready to draw your weapon at the slightest movement.\n")

    decision = input("Press 'D' to draw your gun and shoot: ")

    if decision.lower() == "d":
        print(
            "In a flash, you draw your gun and fire! The sound of gunshots echoes through the town as bullets fly.")
        print("Blaze reacts just as quickly, and bullets whiz by you as you both exchange gunfire.\n")
        print("You manage to take cover behind a barrel, narrowly avoiding Blaze's shots.")
        print("With each shot, you inch closer to a better position, trying to outmaneuver your opponent.\n")

        print("The shootout continues, bullets kicking up dust and splintering wood around you.")
        print("Your heart races as you focus on your target, carefully aiming and firing in the hopes of hitting Blaze.\n")
        shootout_aim()


import random
def shootout_aim():
    target_number = random.randint(1, 3)

    print("last chance to beat Blaze")
    print("Guess the number rolled on the dice (1-3).")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 3:
                print("Please enter a valid guess between 1 and 3.")
                continue

            if guess == target_number:
                print("Your aim is true, and your shot finds its mark. Blaze stumbles back, a look of surprise on his face.")
                print("He collapses to the ground, defeated. The townspeople cheer as you emerge victorious.")
                print("With Blaze out of the picture, the town is finally free from his reign of terror.\n")
                print("as you celebrate with the towns folk umtil the nights full you see an abandoned house.\n")
                abandoned_house()

            else:
                print(f"you hesitate and miss...giving Blaze the advantage. In a split second, he draws and fires!")
                print("The sound of a gunshot rings in your ears as a searing pain courses through your chess.")
                print("You collapse to the ground, your vision fading as the townspeople's voices grow distant.")
                print("Blaze stands above you laughing....as he start pissing on you\n")
                print("you try to get up but you're to weak and full of urine and the rest of the townpeople joins pissing on you\n")

                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() == "yes":
                    print("back to the start")
                    intro()
                    break
                    intro()
                elif play_again.lower() != "yes":
                    print("Invalid input. Game over.")
                    break

                target_number = roll_dice()

        except ValueError:
                print("Please enter a valid number.")


        else:
            print("You hesitate for a moment, giving Blaze the advantage. In a split second, he draws and fires!")
            print("The sound of a gunshot rings in your ears as a searing pain courses through your side.")
            print("You collapse to the ground, your vision fading as the townspeople's voices grow distant.")
            print("Blaze stands above you laughing....as he start pissing at you\n")
            print("you try to get up but youre to weak and the rest of the townpeople are now pissing at you as well\n")
            print(f"you look up to and see an angle laughing at you\n"
                  f"the angle says: try again? \n")
            print(f"1. try again")
            print(f"2. just die")

            decision = input("Enter the number of your decision: ")

            if decision == "1":
                intro()
            else:
                print("thanks for playing")

def tv_show():
    print(f"You wake up in a strange world, disoriented and confused.")
    print(f"Everything around you looks surreal, like you've stepped into a different reality.")
    print(f"A voice echoes in your head: 'Welcome to The {you} Show.'\n")

    print(f"Before you stands a picture-perfect suburban neighborhood called Tranquility Lane.")
    print(f"The houses are pristine, the lawns are immaculate, and the sky is an eternal blue.")
    print(f"A young girl named Betty approaches you, smiling innocently.")
    print(f"She explains that you are the star of this show, and she's your guide.\n")

    print(
        f"Betty gives you a series of tasks to complete. They start innocently enough: making a child cry, stealing a candy bar.")
    print(f"But as time passes, the tasks become increasingly sinister and violent.")
    print(f"You find yourself forced to hurt others in disturbing ways.")
    print(f"Betty's cheerful demeanor contrasts sharply with the darkness of the tasks she assigns.\n")

    print(f"You start to question the reality of this world. It's like a twisted dream, a nightmare you can't escape.")
    print(f"The people around you are trapped, their lives dictated by your actions.")
    print(
        f"You feel a growing sense of guilt and horror as you carry out the tasks, longing to wake up from this twisted nightmare.\n")

    print(f"One day, as the sun sets on Tranquility Lane, you have a choice:")
    print(f"1. Continue to follow Betty's tasks, perpetuating the cycle of violence.")
    print(f"2. Look for an alternative solution, something that could break the simulation and free everyone.\n")

    decision = input("Enter your decision: ")

    if decision == "1":
        print(f"You continue to follow Betty's orders, each task chipping away at your sanity.")
        print(f"The darkness in your heart grows, and the neighborhood's perfect facade becomes more disturbing.")
        print(f"Eventually, Betty reveals her true nature – an embodiment of chaos and cruelty.")
        print(
            f"You are trapped forever in this nightmarish show, condemned to commit unspeakable acts for her amusement.\n")
    elif decision == "2":
        print(f"You decide to find a way to break free from this twisted simulation.")
        print(f"You start to investigate the neighborhood, uncovering hidden clues and secrets.")
        print(f"You discover a failsafe option – an override that can release everyone from this nightmare.")
        print(f"With determination, you activate the failsafe, bringing an end to the torment.")
        print(
            f"Betty's illusion shatters, revealing the truth – you and the others were trapped by Dr. Stanislaus Braun.\n")

    print(f"The simulation collapses, and you wake up in a room that's a stark contrast to the suburban illusion.")
    print(f"You are reunited with your father, James, who had been trapped in dog form by Braun's sadistic experiment.")
    print(
        f"As you leave the room, you can't help but wonder if the events you experienced were real or just part of a twisted show.")
    print(f"The lingering doubt leaves you haunted, forever questioning the nature of reality.")
    print(f"you go outside and a cowboy named Blaze is waiting for a shootout.")
    shootout()


def abandoned_house():
        print("As you walk through the deserted town, you come across an old, abandoned house.")
        print("It looks eerie and unsettling. What will you do?")
        print("1. Enter the abandoned house to investigate.")
        print("2. Keep walking through the desolate streets, wary of the surroundings.")

        decision = input("Enter the number of your decision: ")

        if decision == "1":
            print("You cautiously enter the abandoned house.")
            print("Inside, you find remnants of the past and some supplies.")
            print("Suddenly, you hear footsteps behind you and turn around to face a mysterious figure.")
            print("The figure introduces themselves as Bobby B, a lone wanderer. His eyes gleamed with a sinister intensity, fixed on"
                  "you\n  ")
            print("The air grew colder as Bobby B.'s grin widened, revealing a row of yellowed teeth that seemed to belong to a creature from nightmares. "
                  "Shadows danced around him, casting an ever-changing pattern that played tricks on my mind, "
                  "making the room feel like a labyrinth of horrors.\n")
            print(f"{you} ask him: what are you doing here?\n")
            print(f"Bobby b replies: i want to make a deal with you....if you beat me than you can have my horse but if you lose....your soul is mine \n")
            print(f"1. take the bet")
            print(f"2. not the bet")

            decision = input("Enter the number of your decision: ")
            if decision == "1":
                print(f"Bobby b says: the game is called have i never ever")
                print(
                    f"The rules are i start by saying a simple statement starting with Never have I ever if you have sin, you lose your soul\n "
                    f"to me hahahah.....but if you are a saint than your soul stays with you and ill give you a horse.")
                bet_with_the_devil ()
            else:
                print(f"the doors locked by them self shut and bobby b says: i lied youre going to play for you soul...")
                print(f"Bobby b says: the game is called have i never ever")
                print(f"The rules are i start by saying a simple statement starting with Never have I ever if you have sin, you lose your soul\n "
                      f"to me hahahah.....but if you are a saint than your soul stays with you and ill give you a horse.")
                bet_with_the_devil ()

        elif decision == "2":
            print("You decide to avoid the abandoned house and continue walking through the desolate streets.")
            print("As you walk, you sense someone following you.")
            print("You turn around and come face-to-face with a mysterious figure.")
            print("The figure introduces themselves as Bobby B, a lone wanderer. They offer you a horse for a game do you agree? y/n.\n")

            decision = input("Enter of your decision: ")
            if decision == "y":
                print(f"Booby b revels himself to be the devil \n Bobby b says: good lets play a game for your soul.... if you win ill give you that horse")
                bet_with_the_devil()
            elif decision == "n":
                print(f"Booby b revels himself to be the devil, and takes out a dice and says: ill give you another chance to win a"
                      f" horse... (please decide what you want to do)")
                print(f"1. take the bet")
                print(f"2. not the bet\n")

                decision = input("Enter your decision: \n")
                if decision == "1":
                    print("i like you the devil says, above 10 to keep your soul but less.....")
                    throw_dice()

                elif decision == "2":
                    print("the devil says: well now you have to play would you rather....for your soul...")
                    bet_with_the_devil()
                else:
                    print("Invalid choice!")
                    abandoned_house()
        else:
            print("Invalid choice!")
        abandoned_house()

def throw_dice():
    import random
    result = random.randint(1, 27)

    print("Dice rolled:", result)

    if result > 10:
            print("The devil looks at you with anger and says: 'You get to keep your soul... now take my horse...'")
            print(f"{you} gets on the horse and rides to a new town.")
            new_town()

    else:
        print("Bobby B steals your soul and leaves you to walk the earth without a soul.")
        print("Your soul entwined in a sinister pact, a heavy load.")
        print("Under the moon's watchful eye, you met the devil's dark embrace,")
        print("Trading your essence for power, a cold and calculated chase.")
        print("Your shots rang true, a master of the wild terrain,")
        print("Yet your laughter turned hollow, heartache and pain.")
        print("Years passed, a shadowed figure with eyes of coal,")
        print("At the crossroads once more, you reclaimed your stolen soul.")
        print("Haunted but wiser, you rode into the sunset's embrace,")
        print("A cowboy redeemed, scars etched in your weathered face.")
        third_town_coward()




def bet_with_the_devil ():
        print(f"never have i ever stole anyting? (y/n)")

        decision = input("Enter the Y/N of your decision: ")
        if decision == "y":
            print("Bobby b steals your soul....leave's you to walk the earth without a soul\n")
            print("soul entwined in a sinister pact, a heavy load.\n Under moon's watchful eye, he met the devil's dark embrace, \nTrading his essence for power, "
                  "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                  "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                  "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
            third_town_coward()

        if decision == "n":
            print(f"never have i ever had sex with a ''good personality'' ? (y/n)")

        decision = input("Enter the Y/N of your decision: ")
        if decision == "y":
            print("Bobby b steals your soul....leave's you to walk the earth without a soul\n")
            print("soul entwined in a sinister pact, a heavy load. Under moon's watchful eye, he met the devil's dark embrace, Trading his essence for power, "
                  "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                  "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                  "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
            print(f"1. try again")
            print(f"2. just die")

            decision = input("Enter the number of your decision: ")

            if decision == "1":
                intro()
            else:
                print("thanks for playing")
        if decision == "n":
            print(f"never have i ever stalk someone on facebook ? (y/n)")

            decision = input("Enter the Y/N of your decision: ")
            if decision == "y":
                print(
                    "Bobby b and steals your soul....leave's you to walk the earth without a soul\n")
                print(
                    "soul entwined in a sinister pact, a heavy load. Under moon's watchful eye, he met the devil's dark embrace, Trading his essence for power, "
                    "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                    "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                    "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
                print(f"1. try again")
                print(f"2. just die")

                decision = input("Enter the number of your decision: ")

                if decision == "1":
                    intro()
                else:
                    print("thanks for playing")
            if decision == "n":
                print(f"never have i ever had ghosted someone  ? (y/n)")

                decision = input("Enter the Y/N of your decision: ")
                if decision == "y":
                    print(
                        "Bobby b and steals your soul....leave's you to walk the earth without a soul\n")
                    print(
                        "soul entwined in a sinister pact, a heavy load. Under moon's watchful eye, he met the devil's dark embrace, Trading his essence for power, "
                        "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                        "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                        "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
                    print(f"1. try again")
                    print(f"2. just die")

                    decision = input("Enter the number of your decision: ")

                    if decision == "1":
                        intro()
                    else:
                        print("thanks for playing")
                if decision == "n":
                    print(f"never have i ever had one night-stand  ? (y/n)")

                    decision = input("Enter the Y/N of your decision: ")
                    if decision == "y":
                        print(
                            "Bobby b and steals your soul....leave's you to walk the earth without a soul\n")
                        print(
                            "soul entwined in a sinister pact, a heavy load. Under moon's watchful eye, he met the devil's dark embrace, Trading his essence for power, "
                            "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                            "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                            "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
                        print(f"1. try again")
                        print(f"2. just die")

                        decision = input("Enter the number of your decision: ")

                        if decision == "1":
                            intro()
                        else:
                            print("thanks for playing")
                    if decision == "n":
                        print(f"never have i ever sain the N word  ? (y/n)")

                        decision = input("Enter the Y/N of your decision: ")
                        if decision == "y":
                            print(
                                "Bobby b and steals your soul....leave's you to walk the earth without a soul\n")
                            print(
                                "soul entwined in a sinister pact, a heavy load. Under moon's watchful eye, he met the devil's dark embrace, Trading his essence for power, "
                                "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                                "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                                "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
                            print(f"1. try again")
                            print(f"2. just die")

                            decision = input("Enter the number of your decision: ")

                            if decision == "1":
                                intro()
                            else:
                                print("thanks for playing")
                        if decision == "n":
                            print(f"never have i ever had stole somthing  ? (y/n)")

                            decision = input("Enter the Y/N of your decision: ")
                            if decision == "y":
                                print(
                                    "Bobby b and steals your soul....leave's you to walk the earth without a soul\n")
                                print(
                                    "soul entwined in a sinister pact, a heavy load. Under moon's watchful eye, he met the devil's dark embrace, Trading his essence for power, "
                                    "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                                    "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                                    "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
                                print(f"1. try again")
                                print(f"2. just die")

                                decision = input("Enter the number of your decision: ")

                                if decision == "1":
                                    intro()
                                else:
                                    print("thanks for playing")
                            if decision == "n":
                                print(f"never have i ever peed in a pool ? (y/n)")

                                decision = input("Enter the Y/N of your decision: ")
                                if decision == "y":
                                    print(
                                        "Bobby b and steals your soul....leave's you to walk the earth without a soul\n")
                                    print(
                                        "soul entwined in a sinister pact, a heavy load. Under moon's watchful eye, he met the devil's dark embrace, Trading his essence for power, "
                                        "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                                        "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                                        "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
                                    print(f"1. try again")
                                    print(f"2. just die")

                                    decision = input("Enter your decision: ")

                                    if decision == "1":
                                        intro()
                                    else:
                                        print("thanks for playing")
                                if decision == "n":
                                    print(f"never have i ever made fun of a weak person  ? (y/n)")

                                    decision = input("Enter the Y/N of your decision: ")
                                    if decision == "y":
                                        print(
                                            "Bobby b and steals your soul....leave's you to walk the earth without a soul\n")
                                        print(
                                            "soul entwined in a sinister pact, a heavy load. Under moon's watchful eye, he met the devil's dark embrace, Trading his essence for power, "
                                            "a cold and calculated chase. His shots rang true, a master of the wild terrain, Yet his laughter turned hollow, heartache and pain. "
                                            "Years passed, a shadowed figure with eyes of coal, At the crossroads once more, he reclaimed his stolen soul. "
                                            "Haunted but wiser, he rode into the sunset's embrace, A cowboy redeemed, scars etched in his weathered face. \n")
                                        print(f"1. try again")
                                        print(f"2. just die")

                                        decision = input("Enter your decision: ")

                                        if decision == "1":
                                            intro()
                                        else:
                                            print("thanks for playing")
                                    if decision == "n":
                                        print(f"the devil mad and said: well well {you}.... you're a good but boring...live a little. and don't forget your horse.\n"
                                              f"you leave the abandoned house and see a beautiful horse. do you want to give a name? (y/n)")
                                        decision = decision = input("Enter the number of your decision: ")
                                        if decision == "y":
                                            print(f"well his name is horse")
                                        elif decision == "n":
                                            print(f"well his name is horse")
                                        new_town()


def new_town():
        print(f"{you} slowly get away from the old town to find a better life and opportunity\n")
        print(f"you ride for day's in the desert, as you drink the last drop of water left in your bottle")
        print(f"you see a new place!! you ride towards the town and see a sign: Welcome to {town_name}\n")
        print(
            f"As you ride into town of {town_name} on your trusty horse, you couldn't help but notice the smiles of the townspeople.\n"
            f"Despite their friendly nods and greetings, an underlying tension hung in the air. You think about leaving for a new place.")
        print(f"As you are about to leave, you hear a sweet voice. You see a young beautiful woman calling you as she walks towards you.\n")
        print(f"She says: 'You look new here, my name is Emily... and I could use your help. Would you help?'\n")
        print(f"1. Help the beautiful woman")
        print(f"2. Leave this town\n")

        decision = input("Enter your decision: \n")
        if decision == "1":
            print(f"Emily, leads you to her home and says: the bandits' are a group of bad bad people named ''Gang Bang Gang'' "
                  f" only at night they come out of their hideout to rob people like me.")
            print(f"they kidnap my father! the only way i can see him again is if i pay the ransom.\n i dont know what to do! the towns people won't help me!\n "
                  f"i saw you have a gun...so please help with ill give you some bullets")
            print(f"you think to yourself: i just finish with one gang should i do it again?")
            print(f"1. yeah let's kill the gang bang gang.")
            print(f"2x1. leave the bitch and go back to town {town_name}")
            print(f"2+1. leave the town {town_name} and the bitch")

            decision = input("Enter your decision: \n")

            if decision == "1":
                print("Under the cover of night, you and Emily set out to confront the bandits. Emily shows you that the cave that looks like a skull is the hideout")
                print("As you approach the hideout, tension fills the air. You devise a plan to catch them off guard.")
                print("The moonlight reveals their camp, and a stealthy approach gives you the upper hand.")
                print("you hear one the gang singing: were the Gang bang gang, and weve got a small craze, for old folks."
                  "ohh, we're the bandits lovin' wrinkled, we be rockin' with seniors and Emily's father.\n")
                print("Emily says: ok that song is a bit personal. and charges the hideout you run after Emily")
                print("Emily and you are shoked to see that its another gang bang....and the head-master (Emily's father nickname) looks at you with shoked")
                print(f"Emily father: who are you?! oh no emily i didnt want you to see me like this..... but now you have to die!\n "
                  f"the whole gang pulls out their guns...you grab Emily and take cover \n")
                print("A tense showdown unfolds, but your quick thinking and skilled marksmanship are shit so you miss every shot. Emily's father laugh's"
                  "and says: ill give you another chance you can join us or die\n")
                print("1. join the gang bang you sick sick person...")
                print("2. keep fighting")


                decision = input("Enter your decision: \n")

                if decision == "1":
                    print(f"{you} join's the gang bang....(wtf), Emily shocked but understand.\n as you finish and put your clothes back on,\n"
                      f" Emily shares a look with you and says: i'm not sure you needed to join but.... we survived. lets go back to my place and get cleaned up.\n ")
                    print(f"{you} get cleaned up, you tell Emily you need to leave. Emily asked to join you ")
                    print(f"{you} you think about it....")
                    print(f"1. Let Emily join you")
                    print(f"2. have sex with Emily and think about it")
                    print(f"3. explore the new town but alone ")

                    decision = input("Enter your decision: \n")
                    if decision == "1":
                        print("")
                    elif decision == "2":
                        print("Emily is still  ")
                    else:
                        print(f"{you} says: Emily thanks for the good times but i dont like you like that....\n {you} goes back to {town_name}")
                        back_to_town()


                elif decision == "2":
                    print(f"you look at Emily and say: lets fight!!\n as Emily does all the shooting for you but you sho")
                    print(f"With the bandits defeated, Emily expresses her heartfelt gratitude and invites you to stay in {town_name}.")
                    print(f"after you had sex with Emily a werid sound comes from the kitchen, you explore and see a green figure you get closer....")
                    alien()
                else:
                    print(
                        f"after you had sex with Emily a werid sound comes from the kitchen, you explore and see a green figure you get closer....")
                    alien()
            elif decision == "2":
                print("Feeling uncertain about the situation, you decide to leave the town and continue your journey elsewhere.")
                print(f"As you ride away, you can't shake the feeling that there's more to the story of {town_name}.")
                print("Months pass, and your journey takes you to distant lands and new adventures.")
                print(f"Yet, the memory of {town_name} lingers in your mind, reminding you of untold tales.")
                print(f"Sometimes, the wind carries whispers of {town_name} but you move on.")
                third_town()
            elif decision == "3":
                    print(f"{you} says: Emily thanks for the good times but i dont like you like that.... ")
                    back_to_town()
        elif decision == "2":
            print(f"{you} says: Emily thanks for the good times but i dont like you like that.... ")
            back_to_town()
        else:
            print("Invalid choice. Please enter '1' to help the woman or '2' to leave the town.")
            new_town()



def play_game():
    print("ds")


def back_to_town():
            print(f"The town seemed quiet and eerie. The buildings were old, and shadows danced in the moonlight.")
            print(f"You tied your horse and entered the town's saloon. The bartender eyed you with suspicion.")
            print(f"Strangely, there was no other soul in sight.\n")
            print(f"You ordered a drink and struck up a conversation with the bartender.")
            print(f"He spoke in hushed tones, warning you to leave before nightfall.")
            print(f"He mentioned rumors of creatures that roamed the town after dark – creatures that thirsted for blood.\n")
            print(f"1. Stay in {town_name}")
            print(f"2. Leave {town_name}\n")

            decision = input("Enter your decision: ")

            if decision == "1":
                print(f"Curiosity piqued, you decided to stay and investigate. As night fell, the air grew colder.")
                print(f"Flickering lanterns cast eerie glows on the town's deserted streets.")
                print(f"Shadows moved in the corners of your vision, and a chill ran down your spine.\n")

                print(f"Suddenly, figures emerged from the darkness – vampires with glowing eyes and sharp fangs.")
                print(f"You drew your revolver, heart pounding, ready to defend yourself against the supernatural threat.")
                print(f"The vampires hissed, circling you, but before they could attack, a powerful figure appeared.\n")

                print(
                f"The leader of the vampires, a regal and ancient creature, stepped forward. He introduced himself as Lord Howie.")
                print(
                f"He explained that {town_name} was their domain, and they had been here for centuries, hidden from the world.")
                print(
                f"Lord Howie offered you a choice – join their immortal ranks by Sucking Emily's blood or face their wrath.\n")

                print(f"You weighed your options, torn between the allure of immortality and your humanity.")
                print(f"The decision was yours:")
                print(f"1. Accept Lord Howie's offer and become a vampire.")
                print(f"2. Reject their offer and challenge the vampires to a battle for the town.\n")

                decision = input("Enter your decision: ")

                if decision == "1":
                    print(
                    f"You chose to accept Lord Howie's offer. You walk back to Emily's house while she's asleep and start sucking her blood.")
                    print(f"The transformation was painful, but you embraced your new immortal life.")
                    print(f"Over the centuries, you and the vampires ruled over {town_name}, shaping its history and destiny.")
                    print(f"But with immortality came the weight of eternal darkness, forever removed from the sun's warmth.\n")
                    vampire()


                elif decision == "2":

                    print(
                        "You rejected the offer, determined to protect the town and its people from the vampire threat.")

                    print("A fierce battle ensued. With your skills, you fought valiantly against the vampires.")

                    print("Though outnumbered, your determination prevailed, and you managed to be surrounded by them.")

                    print(f"{you} asked to tell a story before you die.")

                    print("Howie accepts your request, but if you don't add 'unicorn' to the story, then you die...")

                    print("Howie accepts your request, but if it's not good, then you die...")

                    while True:

                        story = input("Start writing your story here -> ")

                        if 'unicorn' in story.lower():

                            print("OK, you may leave this town.")

                            third_town_coward()

                            break

                        else:

                            print("Where is the unicorn? Start again.")

                else:
                    back_to_town()

            elif decision == "2":
                print(f"You ran like a coward to leave with your horse to the desert.")
                third_town_coward()
            else:
                print(f"You ran like a coward to leave with your horse to the desert.")
                third_town_coward()


def third_town():
        print(
        f"After days of walking through the unforgiving desert, {you} and emily arrived in the small town of {town_name}.")
        print(f"The scorching sun had taken its toll, but the promise of a new life in a peaceful town kept you going.\n")

        print(f"{town_name} seemed charming at first glance, with its quaint buildings and welcoming atmosphere.")
        print(f"But as you and emily settled in, you began to notice something was amiss.")
        print(f"A band of unruly kids, led by a troublemaker named Jack, terrorized the town.\n")

        print(f"Emily, who had lived in {town_name} before, told you stories of how the kids had taken over.")
        print(f"They extorted money from the townspeople, destroyed property, and created an atmosphere of fear.")
        print(f"Determined to put an end to this, you and emily decided to take matters into your own hands.\n")

        print(f"Together, you devised a plan to confront the band of bad kids and restore peace to {town_name}.")
        print(
        f"You trained the townspeople in self-defense, and with their support, you prepared for the inevitable showdown.\n")

        print(f"One evening, as the sun began to set, the showdown commenced.")
        print(f"Jack and his gang confronted you and emily, taunting and challenging you to a fight.")
        print(f"The air was tense, but your determination burned stronger than ever.\n")

        print(f"The fight was fierce, fists and dust flying as you and emily stood your ground.")
        print(f"The townspeople fought alongside you, refusing to be victims any longer.")
        print(
        f"Emily's quick thinking and your cowboy skills proved to be a formidable combination against the unruly gang.\n")

        print(f"After a long and intense battle, the gang was defeated.")
        print(f"Jack and his cronies retreated in defeat, leaving {town_name} for good.")
        print(f"The townspeople cheered, grateful for your bravery and emily's determination.\n")

        print(f"Emily's presence and your skills had saved {town_name} from the reign of the bad kids.")
        print(f"The town once again flourished, and its people could finally enjoy the peace they deserved.")
        print(f"You and emily were celebrated as heroes, and your bond grew stronger through the shared adventure.\n")

        print(f"In {town_name}, you found a new home, a new purpose, and a partner in emily.")
        print(f"The two of you became inseparable, ensuring that the town remained safe and prosperous.")
        print(
        f"And so, your journey through the desert led you to a new beginning and a life filled with adventure and love.")

def third_town_coward():
        print(
        f"After days of walking through the unforgiving desert, {you} and your loyal horse finally arrived at {town_name}.")
        print(f"The town looked empty, its buildings standing as if frozen in time.")
        print(f"Feeling parched and exhausted, you decided to seek refuge in the local saloon.\n")

        print(f"As you entered the saloon, an eerie silence greeted you. The air felt thick with an unnatural energy.")
        print(f"You took a seat at the bar and ordered a drink, your eyes scanning the room for any signs of life.\n")

        print(
        "Suddenly, a strange, scintillating light engulfed the saloon. Before you could react, you felt a powerful force pulling you.")
        print(
        "The world around you blurred, and the sensation was disorienting. When the light faded, you found yourself in a strange room.\n")

        print(
        f"You looked around, trying to make sense of your surroundings. The room was filled with bizarre machinery and glowing screens.")
        print(
        f"A voice echoed from an intercom, 'Welcome, {you}. You've entered the Transdimensional Enigma, a machine of my creation.'")
        print(f"Startled, you realized that the voice seemed to know your name.\n")

        print("1. Demand to know who's responsible for this.")
        print("2. Examine the machinery and try to understand the situation.")

        decision = input("Enter your decision: ")

        if decision == "1":
            print("You shouted, 'Who's behind this? What do you want from me?'")
            print(
            "The intercom crackled, 'I am Dr. Stanislaus Braun, the inventor of this machine. I seek your help for a vital task.'")
            print(
            "He explained that the machine was designed to recruit individuals from different dimensions to perform specific tasks.")
            print("You had been chosen because of your unique skills and attributes.")
            print(
            "Before you could react, a gloved hand reached out with a cloth soaked in chloroform. The sweet scent overwhelmed you, and you fell unconscious.\n")
            tv_show()

        elif decision == "2":
            print("Intrigued by the machinery, you approached the glowing screens and intricate devices.")
            print("As you examined them, you began to piece together that this was no ordinary technology.")
            print("Suddenly, a holographic projection appeared before you, depicting the face of an elderly man.")
            print("'Welcome, traveler. I am Dr. Stanislaus Braun, the creator of the Transdimensional Enigma.'")
            print(
            "He explained that the machine could traverse dimensions and that he needed your help for a crucial task.")
            print(
            "Before you could react, a gloved hand reached out with a cloth soaked in chloroform. The sweet scent overwhelmed you, and you fell unconscious.\n")
            tv_show()

        else:
            print("Indecision left you frozen in place as the strange situation continued to unfold around you.")
            print("The voice from the intercom grew impatient, 'Time is of the essence, make a choice.'")
            print(
            "Before you could react, a gloved hand reached out with a cloth soaked in chloroform. The sweet scent overwhelmed you, and you fell unconscious.\n")
            tv_show()

def vampire():
    print(f"{you}, the lone vampire cowboy, arrived in the remote town of {town_name}.")
    print(f"The air was thick with tension as evil Indian warriors, cursed with lycanthropy, terrorized the town.")
    print(f"Determined to bring peace, you took it upon yourself to rid {town_name} of these monstrous foes.\n")
    print(f"As night fell, you patrolled the streets, your vampire senses alert to danger.")
    print(f"Amid the darkness, you met Howie, a skilled and loyal gunslinger, who shared your mission.")
    print(f"United by a common purpose, you formed an unlikely partnership to combat the dual threat of werewolf Indians.\n")
    print(f"For weeks, you and Howie fought bravely, defending the town against the vicious attacks.")
    print(f"Your vampire strength and Howie's sharpshooting skills made you a formidable team.")
    print(f"The townspeople rallied behind you, inspired by your determination and resilience.\n")
    print(f"One fateful night, as you and Howie were planning your next move, you overheard a conversation.")
    print(f"Howie's voice carried a sinister tone as he spoke with one of the Indian leaders.")
    print(f"Shocked and betrayed, you realized Howie was working with the very enemies you were fighting against.\n")
    print(f"Confronting Howie, you demanded the truth. He confessed that he had been feeding information to the werewolf Indians.")
    print(f"He revealed that they promised him power and riches in exchange for his assistance in weakening the town's defenses.")
    print(f"Enraged and heartbroken, you knew that you could no longer trust Howie, and the only way forward was through combat.\n")
    print(f"A showdown ensued between you and Howie in the heart of {town_name}.")
    print(f"The town's fate hung in the balance as you fought with all your strength and vampire abilities.")
    print(f"Bullets and fangs clashed in a battle that symbolized the conflict between good and betrayal.\n")
    print(f"Finally, as dawn approached, the fight came to a climactic end.")
    print(f"Howie, bloodied and defeated, lay before you. Both of you were exhausted, wounded by more than just physical blows.")
    print(f"As the first rays of sunlight broke through the horizon, Howie's betrayal would be a secret taken to his grave.\n")
    print(f"The townspeople emerged from their hiding places, witnessing the aftermath of the battle.")
    print(f"You stood among them, a vampire cowboy who had faced down both supernatural enemies and the darkness within a friend.")
    print(f"{town_name} was saved, but the scars of the past would forever linger, a reminder of the sacrifices made for its survival.")
    print(f"Recognizing your courage and dedication, the townspeople offered you a new role – the sheriff of {town_name}.")
    print(f"With your supernatural abilities, you vowed to protect the town from any threat that might come its way.")
    print(f"And so, you became the enigmatic sheriff vampire of {town_name}, ensuring that its future would be safeguarded by your watchful eyes.")
    print("The end")


def main():
     intro()


if __name__ == "__main__":

     main()
