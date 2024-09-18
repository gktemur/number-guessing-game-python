import random

# 1. Display welcome message to the player
def display_welcome_message():
  print("Welcome to the Number Guessing Game!")
  print("I have selected a number between 1 and 100.")
  print("Can you guess the number?")

 # 2. Select a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# 3. Get the player's guess and validate the input
def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")

 # 4. Provide feedback based on the player's guess
def give_feedback(guess, secret_number):
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the correct number.")

# 5. Main game loop where the guessing takes place
def play_game():
    display_welcome_message()
    secret_number = generate_random_number()
    attempts = 0

    while True:
        guess = get_player_guess()
        attempts += 1

        if guess == secret_number:
            print(f"You've guessed the number {secret_number} in {attempts} attempts!")
            break
        else:
            give_feedback(guess, secret_number)

# 6. Entry point to start the game
if __name__ == "__main__":
    play_game()