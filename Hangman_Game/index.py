import random

from hangman_random_words import word_list, logo
from graphic import stages




# Print Logo
print(logo)

lives = 6

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




# Keep track of end game
end_of_game = False

while not end_of_game:
    
    ### Ask the user to guess a letter.
    # Get user input to get chosen word
    guess = input("Guess a letter \n").lower()

    # Loop through the chosen word length
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
            
    if guess not in chosen_word:
      print(f"You have guess the word: {guess} Not in particular word You loose a life.")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You Loose")            
            
    
    print(display)
    # Check to see if "_" is not in display var
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    
    print(stages[lives])
