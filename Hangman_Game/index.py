import random

from hangman_random_words import word_list, logo




# Print Logo
print(logo)

### Generate a Random Word.
# Get random word
chosen_word = random.choice(word_list)
# Initial display set to 0
display = []
# Get the word length
word_length = len(chosen_word)


### Generate as many blanks as letters in a word.
# Get complete set of words
for letter in range(word_length):
    display += "_"
print(display)   

# To check the chosen word we can comment this.gp
print(chosen_word)

### Ask the user to guess a letter.
# Get user input to get chosen word
guess = input("Guess a letter \n").lower()


# Keep track of end game
end_of_game = False

while not end_of_game:

    # Loop through the chosen word length
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(display)



#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".