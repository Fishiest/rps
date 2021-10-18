
#rock paper scissors because i need to learn how to spell scissors

from random import randint
import time
wins = 0
comwins = 0

def rpsask():
    global rps
    print("I am currently forcing you to play rock paper scissors. [R/P/S]")
    humanrps = input()
    if humanrps == "R":
        rps = 1
    elif humanrps == "P":
        rps = 2
    elif humanrps == "S":
        rps = 3
    else:
        print("When I said [R/P/S] I meant exactly [R/P/S], caps and everything")
        time.sleep(0.5)
        print("Restarting..")
        time.sleep(3)
        rpsask()
def main():
    global comwins
    global wins
    #Saying what the computer chose.
    rpsask()
    comprps = randint(1, 3)
    if comprps == 1:
        print("The computer chose rock!")
        time.sleep(.5)
    elif comprps == 2:
        print("The computer chose paper!")
        time.sleep(.5)
    elif comprps == 3:
        print("The computer chose scissors!")
        time.sleep(.5)
    #now for the mess of if/thens...
    if rps == comprps:
        print("Its a tie!")
        wins += .5
        comwins += .5
    elif rps == 1:
            if comprps == 2:
                print("The computer won!")
                comwins += 1
            elif comprps == 3:
                print("You won!")
                wins += 1
    elif rps == 2:
            if comprps == 1:
                print ("You won!")
                wins += 1
            elif comprps == 3:
                print ("The computer won!")
                comwins += 1
    elif rps == 3:
            if comprps == 1:
                print ("The computer won!")
                comwins += 1
            elif comprps == 2:
                    print ("You won!")
                    wins += 1
    print ("Would you like to have a rematch? [Y/N]")
    if input() == "Y":
        main()
    else:
        print("Alright, the score was", wins, "-", comwins,)

main()