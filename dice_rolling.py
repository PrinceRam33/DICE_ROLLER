import random

def roll():

    dice= {
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
    roll_the_dice = input("Roll the dice? (Yes/No) : ")
    while roll_the_dice.lower() == "Yes". lower():
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        print("dice rolled: {} and {}". format(dice_1, dice_2))
        print("\n".join(dice[dice_1]))
        print("\n".join(dice[dice_2]))
        
        roll_the_dice = input("Roll again? (Yes/no): ")
roll()
