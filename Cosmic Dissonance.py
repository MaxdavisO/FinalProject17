#this imports random probability
import random
#this console puts in a time waiting time before next action
import time

#this is what is supposed to print at the start of the game
def displayintro():
    print("Hello, Space Captain")
    time.sleep(2)
    print("You are the commander of an interstellar colonization spaceship")
    time.sleep(2)
    print("Your mission is to select the best candidate for human settlement")
    time.sleep(2)
    print("A lot is resting on your shoulders so choose wisely")
    time.sleep(2)
    print("The planets you have to choose from are Volturnus and Janus")
    time.sleep(2)
    print("Volturnus is a very Earth-like planet, that's 1.2 times the size of Earth and has 1.047 times the gravity of Earth and the surface is almost 74% water")
    time.sleep(2)
    print("Janus is also very close to the size of Earth, it's 0.96x the size of Earth, has 0.98x times the gravity of Earth and the surface is about 68% water")

#this is supposed to give you an option to choose a planet
def choosePath():
    path = ""
    while path !="Volturnus" and path !="Janus":
        path = input("which planet will you choose? (Volturnus or Janus): ")

    return path

#this prints a message after you choose your planet
def checkPath(chosenPath):
    print("You arrive at the planet")
    time.sleep(2)

    correctPath = ("Janus")

    if chosenPath == str(correctPath):
        print("You notice a small structure on the dark side of the planet's moon")
        time.sleep(2)
        print("You and your crew decide to investigate")
        time.sleep(2)
        print("It appears to be some kind of obelisk about 12 meters or 39 feet tall")
        time.sleep(2)
        print("Next to it you find the frozen bodies of two aliens with a message next to them")
        time.sleep(2)
        print("The message seems to tell you that the civilization living on that planet died due to a worldwide nuclear war")
        time.sleep(2)
        print("The message also seems give instructions on how to revive the aliens if the aliens if they were ever found")
        time.sleep(2)
        print("Do you revive the aliens or do you leave them?")

        def choosePath():
             path = ""
             while path != "Revive" and path != "Leave": # input validation
                path = input("Which path will you choose? (Revive or Leave): ")

             return path

             correctPath = ("Revive")

             if chosenPath == str(correctPath):
                 print("You revive the two aliens and they share their knowledge with you and help you build your colony")
                 time.sleep(2)
                 print("In turn you help them rebuild their civilization and you coexist on the same planet")
             else:
                 print("You leave the aliens alone to forever rest")
                 print("leaving the obelisk and a small outpost on the other side of the moon as a monument to their existence")
                 time.sleep(2)
                 print("You build your settlement on the ashes of a once prospering civilization")

            #this is supposed return you to the start of the game after you've gone down this path
            playAgain = "yes"
            while playAgain == "yes" or playAgain == "y":
             displayIntro()
             choice = choosePath()
             checkPath(choice)
            playAgain = input("Do you want to play again? (yes or y to continue playing): ")
    else:
        print("You realize that the planet is populated with primative life, including some multi-cellular organisms and single cellular life")
        print("If you attempt to settle the planet no you could expose the lifeforms to your bacteria and viruses that could kill them off, or expose yourself to the planet's bacteria and virus that could be life threatning to you")
        print("Do you take the risk?")

        def choosePath():
            path = ""
            while path !="Yes" and path !="No":
                path = input("What will you choose? (Yes or No): ")

            return path

            #this is supposed to give you a random ending
            correctPath = random.randint(Yes,No)

        if chosenPath == str(correctPath):
            print("Congratulations, you managed not to get killed by space germs")

        else:
            print("You failed your mission to settle this planet, better luck next time")

            playAgain = "yes"
            while playAgain == "yes" or playAgain == "y":
              displayIntro()
              choice = choosePath()
             checkPath(choice)
             playAgain = input("Do you want to play again? (yes or y to continue playing): ")



