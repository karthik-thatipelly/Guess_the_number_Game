import random

print("Welcome to the Number Guessing Game. You have 7 chances to guess the number")

#start_value = int(input("Range Start:"))
#end_value = int(input("End Range:"))

number_to_guess = random.randrange(1, 100)

chances = 7
guess_counter = 0

while guess_counter <= chances:
    guess_counter += 1
    user_guess = int(input("Please enter your guess:"))

    if user_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it right in the {guess_counter} attempt")
        break
    
    elif guess_counter > chances:
        print(f"Oops sorry, The number is {number_to_guess}.Better Luck Next Time!")

    elif user_guess > number_to_guess:
        print('Your guess is higher')
    
    elif user_guess < number_to_guess:
        print('Your guess is lower')
