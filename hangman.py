# Firstly, we are using random because this game will take random words 
import random
#Now, lets create 5 words for this game 
words = ["python", "hello", "world", "game", "fun"]
word = random.choice(words)
guessed = ["_"] * len(word)
wrong_guesses = 0
max_wrong = 6
all_guesses = []

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"The word has {len(word)} letters: {' '.join(guessed)}")

while wrong_guesses < max_wrong and "_" in guessed:

    guess = input("\nEnter a letter: ").lower()
    if guess in all_guesses:
        print("You already guessed that letter!")
        continue
    all_guesses.append(guess)
    if guess in word:
        print(f"Good! '{guess}' is in the word.")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        wrong_guesses += 1
        print(f"Sorry! '{guess}' is not in the word.")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
    print("Word: " + " ".join(guessed))
if "_" not in guessed:
    print(f"\nCongratulations! You guessed the word: {word}")
else:
    print(f"\nGame Over! The word was: {word}")