# import random function
import random
# define a function
def dice_game():
    # initialize all the necessary value
    rounds = 0
    win = 0


    while True:
        dice_total_value = 0

        user_guess = input("\n Enter your guess(or q to quit ):  ")
        if (user_guess == "q"):
            print("game quitted!!")
            break

        user_guess = int(user_guess)
        while user_guess > 12:
            user_guess = int(input("\n your guess should be less than 12 \n Enter your guess again: "))

        rounds += 1

        # prompt user to roll the dice for first time
        user = str(input(" \n Enter roll or r to roll the first dice:  "))
        if (user == "r") or (user == "roll"):
            dice_value = random.randint(1,6)
            dice_total_value += dice_value
            print(f" value of first dice roll : {dice_value}")

        # prompt user to roll the dice for second  time
        user = str(input("\n Enter roll or r to roll the second dice:  "))
        if (user == "r") or (user == "roll"):
            dice_value = random.randint(1,6)
            dice_total_value += dice_value
            print(f" value of seond dice roll : {dice_value}")

        # print the total values
        print(f" \n Your guess is {user_guess}")
        print(f" total value of dice  is {dice_total_value} \n ")

        # compare the user guess and the dice value
        if (dice_total_value < user_guess):
            print(f"Your guess is higher ")
        elif (dice_total_value > user_guess):
            print(f"Your guess is lower")
        else:
            win += 1
            print("congrats!! you guesse it right")

        # display win percenatage and total rounds played
        print(f"\n Total games played: {rounds}")
        print(f"win percentage: {win / rounds}")

# call the function
dice_game()