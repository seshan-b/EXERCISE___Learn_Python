# Import the random and stages modules
import random
from graphic import stages

# Import the word_list and logo variables from the hangman_random_words module
from hangman_random_words import word_list, logo

# Print the logo
print(logo)

# Initialize the lives variable to 6
lives = 6

### Generate a Random Word.

# Choose a random word from the word list
chosen_word = random.choice(word_list)

# Initialize the display variable to an empty list
display = []

# Get the length of the chosen word
word_length = len(chosen_word)

### Generate as many blanks as letters in a word.

# Add a blank character to the display list for each letter in the chosen word
for letter in range(word_length):
    display += "_"

# Print the display list, which shows the number of blanks equal to the number of letters in the chosen word
print(display)   

# To check the chosen word, we can comment this out
# print(chosen_word)


# Initialize the end_of_game flag to False
end_of_game = False

# Start a loop that continues until the end_of_game flag is set to True
while not end_of_game:
    
    ### Ask the user to guess a letter.
    
    # Get user input for the letter guess
    guess = input("Guess a letter \n").lower()

    # Loop through the chosen word
    for position in range(word_length):
        # Get the current letter in the chosen word
        letter = chosen_word[position]
        # If the letter matches the guess, update the corresponding position in the display list
        if letter == guess:
            display[position] = letter
            
    # If the guess is not in the chosen word, decrease the number of lives by 1 and check if the game is over
    if guess not in chosen_word:
      print(f"You have guess the word: {guess} Not in particular word You loose a life.")
      lives -= 1
      if lives == 0:
        # If the number of lives is 0, set the end_of_game flag to True to end the game
        end_of_game = True
        print("You Loose")            
            
    # Print the updated display list
    print(display)
    
    # Check if there are any blank characters left in the display list
    if "_" not in display:
        # If there are no blank characters, set the end_of_game flag to True to end the game
        end_of_game = True
        print("You win")
    
    # Print the current stage of the hangman game based on the number of lives remaining
    print(stages[lives])
