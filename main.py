# guess game
import random

number = random.randint(1,100) # it will choose the random number by system
guess = 0

print("welcome to the guess game, guess the number between 1 and 100")

while True:
    guess_the_number = int(input("enter your guess:"))
    guess += 1

    if guess_the_number > number:
        print("too high try again")
    elif guess_the_number < number:
        print(" too low try again")
    else:
        print(f"Congratulations! You guessed the correct number: {guess_the_number}")
        break

###########################################################################################
# scramble game using for loop
import random

# List of words
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# this function will select random word from list
original_word = random.choice(words)

#  this function will Scramble the word
scrambled_word = ''.join(random.sample(original_word, len(original_word)))

print("Welcome to the Word Scramble Game!")
print(f"Unscramble this word: {scrambled_word}")


for i in range(100):  # Large number to allow many attempts
    guess = input("Your guess: ").lower()  # lower will used to avoid case sensitive error

    if guess == original_word:
        print(f"Congratulations! You guessed it right: {original_word}")
        break  # Exit loop when guessed correctly
    else:
        print("Wrong guess! Try again.")

