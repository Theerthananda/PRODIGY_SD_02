import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Can you guess what it is?")

    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Too low. Try again!")
            elif guess > target_number:
                print("Too high. Try again!")
            else:
                print("Congratulations! You've guessed the number correctly.")
                print("It took you", attempts, "attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()