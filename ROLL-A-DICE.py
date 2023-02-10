import random
dice_boards = {
    1: """
        [-----]
        [     ]
        [  0  ]
        [     ]
        [-----]
    """,
    2: """
        [-----]
        [     ]
        [ 0 0 ]
        [     ]
        [-----]
    """,
    3: """
        [-----]
        [     ]
        [0 0 0]
        [     ]
        [-----]
    """,
    4: """
        [-----]
        [0   0]
        [     ]
        [0   0]
        [-----]
    """,
     5: """
        [-----]
        [0   0]
        [  0  ]
        [0   0]
        [-----]
    """,
    6: """
        [-----]
        [0 0 0]
        [     ]
        [0 0 0]
        [-----]
    """
}
userResponse = "y"

while userResponse == "y":
    userInput = input("do you want to roll a dice (y) yes or (n) no ")
    randomNumber = 0
    if userInput == "y":
        randomNumber = random.randint(1,6)
        print(dice_boards[randomNumber])
    elif userInput == "n":
        print("Ending")
        break
    else:
        print("Error, program ending")
        break
