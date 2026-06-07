#!/usr/bin/env python3
"""
HorizonTechX Internship - Task 1: Hangman Game
Author: Intern
Description: A simple text-based Hangman game where the player guesses a word one letter at a time.
"""

import random

# Predefined word list - strictly 5 words as per simplified scope.
WORDS = ["python", "developer", "programming", "internship", "horizon"]
MAX_INCORRECT_GUESSES = 6


def display_word_state(word, guessed_letters):
    """
    Returns the string representation of the word showing correctly guessed letters
    and underscores for unguessed letters.
    """
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)


def play_hangman():
    """
    Main function to run the Hangman game loop.
    """
    print("=" * 45)
    print("      Welcome to Horizon TechX Hangman!      ")
    print("=" * 45)
    print(f"I have chosen a secret word. You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.")
    print("Let's begin!\n")

    # Select a random word from the hardcoded list
    secret_word = random.choice(WORDS).lower()
    guessed_letters = set()
    incorrect_guesses = 0

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        # Display the current progress of the word
        current_state = display_word_state(secret_word, guessed_letters)
        print(f"Word to guess: {current_state}")
        print(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        
        # Display letters already guessed if any
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        # Get and validate user input
        guess = input("Enter a letter: ").strip().lower()
        print("-" * 45)

        # Validation checks
        if not guess.isalpha():
            print("Invalid input! Please enter a letter (a-z).")
            print("-" * 45)
            continue
        if len(guess) != 1:
            print("Invalid input! Please enter exactly one letter at a time.")
            print("-" * 45)
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            print("-" * 45)
            continue

        # Add to guessed letters
        guessed_letters.add(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        print("-" * 45)

        # Check if the player has guessed all letters in the secret word
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 45)
            print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
            print(f"You guessed the word: {secret_word.upper()}")
            print("=" * 45 + "\n")
            break
    else:
        # Loop finished without breaking: player ran out of guesses
        print("\n" + "=" * 45)
        print("💀 GAME OVER! 💀")
        print(f"You ran out of guesses. The word was: {secret_word.upper()}")
        print("Better luck next time!")
        print("=" * 45 + "\n")


if __name__ == "__main__":
    play_hangman()
