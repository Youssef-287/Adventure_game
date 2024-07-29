import time  # to use time.sleep
import random  # to make a random function

score = 0


def validate_input(text, value, options):  # to check the input that comes from the user
    while value not in options:
        print("invalid input")
        value = input(text)


def print_pause(text):  # to make pause to the text for some seconds
    print(text)
    time.sleep(1)


def print_score():  # to make a score for the player
    global score
    print(f"your current score is {score}")


def Scenario1(weapon):  # to make a scenario
    beasts = ["Bear", "2 Wolvies", "Lion"]
    print_pause("Youssef entered the forest and he know how it dangerous")


def Scenario2(weapon):  # to make a scenario
    print_pause("Don't do it please")


def game():  # to make the game

    global score  # to make the score global

    print_pause("Youssef is an scout... He is going on a new advanture in the forest ")

    print_pause(
        "Youssef find a small village...some people offereed to help Youssef in this advanture "
    )

    print_pause(
        "Suddenly Youssef heard something moving...He should pickup a weapon from his packbag"
    )

    char = input(
        "Select one of them to help Youssef in his advanture \n 1- chris (Knight) \n 2- Steven (Worrior) \n 3- Peter (Shooter)"
    )
    while char not in ["1", "2", "3"]:
        print("Invalid input")
    char = input(
        "Select one of them to help Youssef in his advanture \n 1- chris (Knight) \n 2- Steven (Worrior) \n 3- Peter (Shooter)"
    )

    if char == "1":
        # Chris
        score += 50
    elif char == "2":
        # Steven
        score += 40
    else:
        # Peter
        score += 60
    print(f"your current score is {score}")
    print_score()

    weapon = input(
        "Please, select a weapon to help Youssef \n 1- 2 Handsword \n 2- Shotgun \n 3- sword \n Enter a Number: "
    )

    while weapon not in ["1", "2", "3"]:
        print("Invalid input")
    weapon = input(
        "Please, select a weapon to help Youssef \n 1- 2 Handsword \n 2- Shotgun \n 3- sword \n Enter a Number"
    )

    if weapon == "1":
        # 2 Handsword
        score += 50
    elif weapon == "2":
        # Shotgun
        score += 60
    else:
        # sword
        score += 40

    print(f"your current score is {score}")

    beasts = ["Bear", "2 Wolvies", "Lion"]

    beast = random.choice(beasts)

    print_pause(f"Suddenly you see a {beast} in front of you...")

    print_score()

    if beast == "Bear":
        dmg = 75
        if score > dmg:
            print("You killed the bear...You Win")
        else:
            print("You dead...You lost the game")
    elif beast == "2 Wolvies":
        dmg = 90
        if score > dmg:
            print("You killed the 2 Wolvies...You win")
        else:
            print("You dead...You lost the game")
    elif beast == "Lion":
        dmg = 110
        if score > dmg:
            print("You killed the Lion...You win")
        else:
            print("You dead...You lost the game")

    sc = random.choice([Scenario1, Scenario2])

    sc(weapon)


game()

print("End")

while True:
    print("Do you want to play again? y/n")
    user_input = input(["y", "n"])
    if user_input == "y":
        score = 0
        game()
    elif user_input == "n":
        print("Thank you for playing")
        break
    else:
        print("invalid input")
        print("Do you want to play again? y/n")
