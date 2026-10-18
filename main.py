import csv
import random

print("Welcome to Polish Flashcards!")

with open("data/db.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    words = list(reader)
    random.shuffle(words)

score = 0

for word in words:

    print("Translate ", word["polish"])
    answer = input("Your translation: ")
    if answer.strip().lower() == word["ukrainian"].strip().lower():
        print("Perfect!")
        score += 1
    else:
        print("Nope, correct answer is ", word["ukrainian"].strip())
    print("Your current score is", score)


print("Spaced repetition session finished. You are amazing!")