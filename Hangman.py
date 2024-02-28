import random

def hangman():
    words = ["brazil", "france", "espana", "england", "japan", "germany", "italy", "greece"]
    chosen_word = random.choice(words)
    word_length = len(chosen_word)
    attempts = 6
    guessed_letters = []
    guessed_word = ['_'] * word_length

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print(" ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        guess = input("Enter a letter or the full word guess: ").lower()

        if guess == chosen_word:
            print("Congratulations! You guessed the word correctly.")
            break

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        if len(guess) == 1:
            guessed_letters.append(guess)
            if guess in chosen_word:
                print("Correct guess!")
                for i in range(word_length):
                    if chosen_word[i] == guess:
                        guessed_word[i] = guess
                if '_' not in guessed_word:
                    print("Congratulations! You guessed the word correctly.")
                    break
            else:
                print("Incorrect guess!")
                attempts -= 1
        else:
            print("Invalid input. Please enter a single letter or the full word guess.")

    if attempts == 0:
        print("You ran out of attempts. The word was:", chosen_word)


hangman()