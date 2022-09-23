import random

from hangman_random_words import word_list, logo



#TODO-1: - Create an empty List called display.gp

print(logo)

# Get random word
chosen_word = random.choice(word_list)


# Get user input to get chosen word
guess = input("Guess a letter \n").lower()

#TODO-2: - Loop through each position in the chosen_word;gp




#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".