#Set the scene, and present first choice.
a = 1
print("Welcome to your adventure. Type 1 for the first option and 2 for the second." )
while a > 0:
    choice = input("You wake up in an abandoned house. Do you call for help OR explore?\n")
    choice = choice.replace(" ","")

    #Chose to call for help
    if choice == "1":
        a = 0
        #Chose to run away
        b = 1
        print()
        print("You have woken up a ghost and now it is chasing after you.")
        while b > 0:
            choice = input("Run away OR fight the ghost?\n")
            choice = choice.replace(" ","")
            if choice == "1":
                b = 0
                c = 1
                print()
                print("You fall into a trap door and you see a cake on a table.")
                while c > 0:
                    choice = input("Do you eat it OR leave it?\n")
                    choice = choice.replace(" ","")
                    #Chose to eat cake
                    if choice == "1":
                        c = 0
                        print()
                        print("You found a key in the cake! A door has appear that leads you outside. CONGRATULATIONS!")
                    #Chose to leave cake
                    elif choice == "2":
                        c = 0
                        print()
                        print("Oh no! The cake disappears and you will now die of starvation. GAME OVER!")
                    #Incorrect input to Cake Q
                    else:
                        print()
                        print("Sorry, try again. Press 1 or 2.")

            #Chose to fight the ghost
            elif choice == "2":
                b = 0
                d = 1
                print()
                print("You win the fight and another ghost appears.")
                while d > 0:
                    choice = input("Do you fight OR talk to it?\n")
                    choice = choice.replace(" ","")
                    #Chose to fight second ghost
                    if choice == "1":
                        d = 0
                        print()
                        print("Oh no! The ghost won. You are now dead. GAME OVER!")
                    #Chose to talk to second ghost.
                    elif choice == "2":
                        d = 0
                        print()
                        print("You talk to the ghost and it gives you a key. A door to the outside world appears. CONGRATULATIONS!")
                    #Incorrect input to 2nd ghost Q
                    else:
                        print()
                        print("Sorry, try again. Press 1 or 2.")

            #Incorrect input to 1st ghost Q
            else:
                print()
                print("Sorry, try again. Press 1 or 2.")




    #Chose to explore the house
    elif choice == "2":
        a = 0
        e = 1
        print()
        print("Upon exploring, you discover 2 doors.")
        while e > 0:
            choice = input("Door 1 OR Door 2?\n")
            choice = choice.replace(" ","")
            #Chose Door 1
            if choice == "1":
                e = 0
                f = 1
                print()
                print("Behind Door 1, a rope is hanging from the ceiling. A knife rests on the floor.")
                while f > 0:
                    choice = input("Do you pull the rope OR cut it with the knife?\n")
                    choice = choice.replace(" ","")
                    #Chose to pull the rope
                    if choice == "1":
                        f = 0
                        print()
                        print("The ceiling collapses and a pile of skulls falls and crushes you to your death. GAME OVER!")
                    #Chose to cut the rope
                    elif choice == "2":
                        f = 0
                        print()
                        print("The spirits are angry with you for cutting their sacred rope. You die. GAME OVER!")
                    #Incorrect input to rope Q
                    else:
                        print()
                        print("Sorry, try again. Press 1 or 2.")

            #Chose Door 2
            elif choice == "2":
                e = 0
                g = 1
                print()
                print("You are in a child's room filled with decaying dolls. They call out to play.")
                while g > 0:
                    choice = input("Do you play OR not?\n")
                    choice = choice.replace(" ","")
                    #Chose to play with dolls
                    if choice == "1":
                        g = 0
                        print()
                        print("After playing, they give you a key. A door to the outside world appears. CONGRATULATIONS!")
                    #Chose not to play
                    elif choice == "2":
                        g = 0
                        print()
                        print("Oh no! The dolls became angry and attacked you to your death. GAME OVER!")
                    #Incorrect input to playing w/ dolls Q
                    else:
                        print()
                        print("Sorry, try again. Press 1 or 2.")
            #Incorrect input to Door Q
            else:
                print()
                print("Sorry, try again. Press 1 or 2.")
    #Incorrect input to initial Q
    else:
        print()
        print("Sorry, try again. Press 1 or 2.")
