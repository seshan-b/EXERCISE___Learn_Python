def test_hangman_game():
    # Create a mock input function to simulate user input
    def mock_input(prompt):
        # Provide a predetermined sequence of inputs
        inputs = ['a', 'b', 'c', 'd', 'e']
        # Return the next input in the sequence
        return inputs.pop(0)
    
    # Create a mock print function to capture the output of the hangman game
    def mock_print(output):
        # Append the output to a list for later assertion
        print_output.append(output)
    
    # Initialize the print_output list to capture the game output
    print_output = []
    
    # Replace the built-in input and print functions with the mock functions
    # This allows us to control the user input and capture the game output for testing
    original_input = __builtins__.input
    original_print = __builtins__.print
    __builtins__.input = mock_input
    __builtins__.print = mock_print
    
    # Run the hangman game
    hangman_game()
    
    # Restore the original input and print functions
    __builtins__.input = original_input
    __builtins__.print = original_print
    
    # Assert that the output is as expected
    assert print_output == [
        # Expected output for the first run of the game
        ' _ _ _ _ ',  # Initial display of blanks
        'You have guess the word: a Not in particular word You loose a life.',  # Incorrect guess
        ' _ _ _ _ ',  # Display remains unchanged
        'You have guess the word: b Not in particular word You loose a life.',  # Incorrect guess
        ' _ _ _ _ ',  # Display remains unchanged
        'You have guess the word: c Not in particular word You loose a life.',  # Incorrect guess
        ' _ _ _ _ ',  # Display remains unchanged
        'You have guess the word: d Not in particular word You loose a life.',  # Incorrect guess
        'You Loose',  # Game over
    ]


