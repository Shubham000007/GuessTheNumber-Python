# Guess The Number is a game, where the user guess the number till it guess the exact  number that generates.

import random  # for generating randon number

# Generating number till the user guess number will match to the generated number


def guessTheShow():
    while True:

        try:
            # first taking input from user
            user_data = int(input("Guess a number between 1 to 10 "))
            random_number = random.randint(1, 10)
            if user_data == 0:
                raise Exception("Guess number cannot be 0...")
            elif user_data > 10:
                raise Exception("Guess a number between 1 to 10...")
            elif int(user_data) != random_number:
                print(f"The generated number is {random_number}")
                print("Opps! you guessed the wrong number")
            elif int(user_data) == random_number:
                print(f"The generated number is {random_number}")
                print("Hurray you guess the correct number")
                break

        except ValueError as err:
            print("You have to enter a number between 1 to 10")
        except Exception as err:
            print(err)
        # finally:
        #     print("Please Guess Again...")
        #     guessTheShow()


guessTheShow()
