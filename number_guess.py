import os
import random


# Takes the user input and compares it aginst the randomly generated number
def guess_checker(user_guess, number_to_guess):
    if user_guess < number_to_guess and number_to_guess - user_guess <= 5:
        print("You have guessed lower than my number, but you are within 5.\n"
              "Try again.\n")
        input("Press any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
    elif user_guess > number_to_guess and user_guess - number_to_guess <= 5:
        print("You have guessed higher than my number, but you are within 5.\n"
              "Try again.\n")
        input("Press any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
    elif user_guess < number_to_guess:
        print("You have guessed lower than my number.\n"
              "Try again.\n")
        input("Press any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
    elif user_guess > number_to_guess:
        print("You have guessed higher than my number.\n"
              "Try again.\n")
        input("Press any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("Congratulations! You have guessed my number!\n")
        input("Press any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
        return False  # Return false to break the loop and go back to the main menu


while True:  # Main game loop
    print("Welcome to the number guessing game!\n"
          "------------------------------------\n"
          "Press 1 to guess my number.\n"
          "Press 2 to quit.\n")
    user_choice = input()  # Get users choice for the menu options.
    os.system("cls" if os.name == "nt" else "clear")

    if user_choice == "1":  # Begin the game.
        number_to_guess = random.randint(1, 100)
        print("I am thinking of a number between 1 and 100.\n"
              "Can you guess it?\n")
        while True:  # Continues to ask the user for a guess until it is correct.
            user_guess = input("What number do you want to guess?\n")
            os.system("cls" if os.name == "nt" else "clear")
            if guess_checker(int(user_guess), int(number_to_guess)) == False:
                break
            else:
                continue
    elif user_choice == "2":  # Quits the application.
        os.system("cls" if os.name == "nt" else "clear")
        break
    else:  # Repeats the question if they enter an invalid response.
        print("Invalid option.")
        input("\nPress any key to continue")
        os.system("cls" if os.name == "nt" else "clear")
