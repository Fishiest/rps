
#rock paper scissors because i need to learn how to spell scissors

from random import randint
print("I was thinking pulling a spamton, but not everyone will know who he is, so rock, paper, or scissors?")
def rpschoose():
    global rps
    if input() == "rock":
        rps = 1
    else:
        if input() == "paper":
            rps = 2
        else:
            if input() == "scissors":
                rps = 3
                if input() == "Rock":
                    rps = 1
                else:
                    if input() == "Paper":
                        rps = 2
                    else:
                        if input() == "Scissors":
                            rps = 3
                            if input() == "r":
                                rps = 1
                            else:
                                if input() == "p":
                                    rps = 2
                                else:
                                    if input() == "s":
                                        rps = 3
                                        if input() == "R":
                                            rps = 1
                                        else:
                                            if input() == "P":
                                                rps = 2
                                            else:
                                                if input() == "S":
                                                    rps = 3
            else:
                print ("You didn't type rock, paper, or scissors, restarting...")
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