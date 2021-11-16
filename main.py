listOfWin = {"r": ("sc", "l"),
              "p": ("r", "sp"),
              "sc": ("p", "l"),
              "l": ("sp", "p"),
              "sp": ("sc", "r")}
listOfChoice = {"r", "p", "sc", "l", "sp"}
import random

rps = "tehe this is just so the code doesn't break :)"
while True:
    #getting a choice
    humanChoice = input("What will your choice be? (r/p/sc/l/sp)")
    if humanChoice.lower()[0] == "s":
        if humanChoice.lower()[1] == "c":
            rps = "sc"
        elif humanChoice.lower()[1] == "p":
            rps = "sp"
    #detecting if the answer is anything but scissors or spock
    if rps == "tehe this is just so the code doesn't break :)":
        rps = humanChoice.lower()[0]
    if rps in listOfChoice:
        print("Not a smart choice, but okay..")
    else:
        print("You didn't type rock, paper, scissors, lizard, or spock...")
        continue
    #getting the computers choice
    comChoice = random.choice(["r", "p", "sc", "l", "sp"])
    #win, loss, or tie?
    if comChoice == rps:
        print("Its a tie!")
    elif comChoice in listOfWin[rps]:
        print("You won!")
    else:
        print("Oh wow you lost LMAO couldn't be me")
    print("Your choice:", humanChoice,"\nComputers Choice:", comChoice)
    #rematch?
    if input("Either way, would you like to try and murder me again?").lower()[0] == "y":
         continue
    else:
        exit()