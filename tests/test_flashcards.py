
from flashcards import (
    load_words,
    shuffle_words,
    check_answer,
    run_session
)


# TEST 1: Checking loading words from csv
def test_load_words(tmp_path):
    csv_file = tmp_path / "words.csv"

    csv_file.write_text(
        "polish,ukrainian\n"
        "kot,кіт\n"
        "dom,дім\n",
        encoding="utf-8"
    )

    words = load_words(csv_file)

    assert len(words) == 2
    assert words[0]["polish"] == "kot"
    assert words[0]["ukrainian"] == "кіт"


# TEST 2: Checking the correct answer
def test_check_answer_correct():
    assert check_answer("кіт", "кіт") is True


# TEST 3: Checking the wrong answer
# Also checking that register and spaces do not impact the result
def test_check_answer_with_spaces_and_case():
    assert check_answer("  КІТ ", "кіт") is True


# TEST 4: Checking shuffling cards
def test_shuffle_words():
    words = [
        {"polish": "kot", "ukrainian": "кіт"},
        {"polish": "dom", "ukrainian": "дім"},
        {"polish": "pies", "ukrainian": "пес"}
    ]

    shuffled = shuffle_words(words)

    assert sorted(shuffled, key=lambda x: x["polish"]) == sorted(
        words, key=lambda x: x["polish"]
    )

    assert shuffled is not words
    assert len(words) == 3


# TEST 5: Checking spaced rep session result
def test_run_session(monkeypatch):
    words = [
        {"polish": "kot", "ukrainian": "кіт"},
        {"polish": "dom", "ukrainian": "дім"}
    ]

    answers = iter(["кіт", "неправильно"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    score = run_session(words)

    assert score == 1
