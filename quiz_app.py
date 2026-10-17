import json, random

QUESTIONS = [
    {"q": "Capital of France?", "options": ["Paris", "Rome", "Madrid"], "a": "Paris"},
    {"q": "2 + 2", "options": ["3", "4", "5"], "a": "4"},
    {"q": "Largest ocean?", "options": ["Atlantic", "Pacific", "Indian"], "a": "Pacific"},
]

def main():
    random.shuffle(QUESTIONS)
    score = 0
    for q in QUESTIONS:
        print("\n" + q["q"])
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        ans = input("Answer: ")
        if ans in q["options"] and ans == q["a"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong. Answer: {q['a']}")
    print(f"\nScore: {score}/{len(QUESTIONS)}")

if __name__ == "__main__":
    main()