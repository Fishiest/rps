
#rock paper scissors because i need to learn how to spell scissors

from random import randint



def rpschoose():
    global rps
    if input() == "rock" or "Rock" or "R" or "r":
        rps = 1
    else:
        if input() == "paper" or "Paper" or "P" or "p":
            rps = 2
        else:
            if input() == "scissors" or "Scissors" or "S" or "s":
                rps = 3
            else:
                print ("You didn't type rock, paper, or scissors, (or mispelled it-) restarting...")
                rpschoose()
def main():
    print("I was thinking pulling a spamton, but not everyone will know who he is, so rock, paper, or scissors?")
    rpschoose()
    comprps = randint(1,3)
    rpschoose()
    #Saying what the computer chose.
    if comprps == 1:
        print("The computer chose rock!")
    else:
        if comprps == 2:
            print("The computer chose paper!")
        else:
            if comprps == 3:
                print("The computer chose scissors!")
    #now for the mess of if/thens...
    if rps == comprps:
        print("Its a tie!")
    else:
        if rps == 1:
            if comprps == 2:
                print ("The computer won!")
            else:
                if comprps == 3:
                    print ("You won!")
        else:
            if rps == 2:
                if comprps == 1:
                    print ("You won!")
                else:
                    if comprps == 3:
                        print ("The computer won!")
            else:
                if rps == 3:
                    if comprps == 1:
                        print ("The computer won!")
                else:
                    if comprps == 2:
                        print ("You won!")
    print ("Would you like a rematch?")
    reanswer = input()
    if "y" or "Y" in reanswer:
        main()
    else:
        exit()
        print("Alright sounds good!")
    print("Alright sounds good!")

main()