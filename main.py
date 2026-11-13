
from flashcards import load_words, shuffle_words, run_session


def main():
    print("Welcome to Polish Flashcards!")

    words = load_words("data/polish_lesson_vocabulary.csv")
    words = shuffle_words(words)

    run_session(words)

    print("Spaced repetition session finished. You are amazing!")


if __name__ == "__main__":
    main()
