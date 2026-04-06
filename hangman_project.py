import random

def hangman():
    words = ["python", "programming", "computer", "hangman", "developer"]
    word = random.choice(words)   # Random word
    guessed = set()
    tries = 6

    print("\n--- Hangman Game ---")
    print("Guess the word! It has", len(word), "letters.")

    while tries > 0:
        display = "".join([ch if ch in guessed else "_" for ch in word])
        print("Word:", display)
        print("Guessed letters:", " ".join(sorted(guessed)))

        if display == word:
            print("🎉 You guessed the word!")
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter!")
            continue

        if guess in word:
            guessed.add(guess)
            print("✅ Correct guess!")
        else:
            tries -= 1
            print(f"❌ Wrong! {tries} tries left.")

    if tries == 0:
        print("😢 You lost! The word was:", word)


hangman()
