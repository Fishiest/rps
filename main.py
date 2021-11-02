
#rock paper scissors because i need to learn how to spell scissors

from random import randint
import time
wins = 0
comwins = 0
global rpsList
rpsList = 1, 2, 3

def rpsask():
    global rps
    print("I am currently forcing you to play rock paper scissors. [R/P/S]")
    humanrps = input().lower()[0]
    if humanrps == "r":
        rps = 1
    elif humanrps == "p":
        rps = 2
    elif humanrps == "s":
        rps = 3
    else:
        print("Bruh.")
        time.sleep(0.5)
        print("Restarting..")
        time.sleep(2)
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
    if rps == comprps:
        print("Its a tie!")
        wins + .5
        comwins = .5
    elif rps == 1:
        if comprps == rpsList[1]:
            print("You lost!")
            comwins + 1
    elif rps == 2:
        if comprps == rpsList[0]:
            print("You lost!")
    elif rps == 3:
        if comprps == rpsList[3]:
            print("You lost!")
    print ("Would you like to have a rematch? [Y/N]")
    if "y" in input().lower()[0]:
        main()
    else:
        print("Alright, the score was", wins, "-", comwins,)

main()