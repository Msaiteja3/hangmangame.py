import random

def hangman():
    # List of words for the game
    word_list = ['python', 'hangman', 'programming', 'developer', 'internship', 'project']
    
    # Randomly select a word
    word_to_guess = random.choice(word_list)
    guessed_word = ['_'] * len(word_to_guess)
    incorrect_guesses = 0
    max_attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(f"The word has {len(word_to_guess)} letters.")
    print("You can guess one letter at a time.")
    print("You lose if you exceed the maximum number of incorrect guesses.")
    print(' '.join(guessed_word))

    while incorrect_guesses < max_attempts:
        guess = input("Enter a letter: ").lower()

        # Check for invalid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Incorrect guesses: {incorrect_guesses}/{max_attempts}")

        print(' '.join(guessed_word))

        # Check if the player has won
        if '_' not in guessed_word:
            print("Congratulations! You've guessed the word correctly!")
            break
    else:
        print("You've exceeded the maximum number of incorrect guesses. Game over!")
        print(f"The word was: {word_to_guess}")

# Run the game
hangman()
