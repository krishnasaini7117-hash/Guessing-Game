import random

def guessing_game():
    lucky_number = random.randint(1,50)
    
    while True:
        try:
            guess_number = int(input("Guess the lucky number: "))
        
            if guess_number == lucky_number:
                print("Congratulations! You guessed the lucky number.")
                break
            elif guess_number < lucky_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

    print("thank you for playing the guessing game.")
        
guessing_game()