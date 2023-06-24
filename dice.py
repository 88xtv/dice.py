import random

dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }

def dice():

    roll = input("Do you want to roll?(y/n): ")

    while roll == "y":

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("The First Dice: ")
        print("\n".join(dice_drawing[dice1]))

        print("The second dice: ")
        print("\n".join(dice_drawing[dice2]))

        roll = input("Do you want to roll again?(y/n): ")


dice()


