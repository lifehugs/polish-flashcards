
import csv
import random


def load_words(file_path):
    with open(file_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def shuffle_words(words):
    shuffled_words = words.copy()
    random.shuffle(shuffled_words)
    return shuffled_words


def check_answer(answer, correct_answer):
    return answer.strip().lower() == correct_answer.strip().lower()


def run_session(words):
    score = 0

    for word in words:
        print("Translate", word["polish"])
        answer = input("Your translation: ")

        if check_answer(answer, word["ukrainian"]):
            print("Perfect!")
            score += 1
        else:
            print("Nope, correct answer is", word["ukrainian"].strip())

        print("Your current score is", score)

    return score
