import random

words = ["python", "computer", "programming", "developer", "keyboard"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have", max_guesses, "wrong guesses.")

while wrong_guesses < max_guesses:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_guesses)

else:
    print("\nGame Over!")
    print("The correct word was:", word)