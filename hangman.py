import random

WORDS = ["python", "programming", "keyboard", "science", "elephant"]

def play():
    word = random.choice(WORDS)
    guessed = set()
    lives = 6
    while lives > 0:
        display = " ".join(c if c in guessed else "_" for c in word)
        print(f"\n{display}  |  lives: {lives}")
        if all(c in guessed for c in word):
            print("You win!")
            return
        g = input("Guess a letter: ").lower()
        if g in guessed:
            continue
        guessed.add(g)
        if g not in word:
            lives -= 1
    print(f"Out of lives. Word was {word}")

if __name__ == "__main__":
    play()