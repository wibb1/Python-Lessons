import csv

FILEPATH = "bonus15/bonus15.csv"


def print_answer_list(answers):
    for index, answer in enumerate(answers):
        print(f"{index + 1}-{answer.capitalize()}")


def open_file(filepath=FILEPATH):
    with open(filepath) as file:
        return list(csv.reader(file))


def evaluate_answer(given_answer, correct_answer):
    return {
        "user_answer": given_answer,
        "correct_answer": correct_answer,
        "status": "Correct" if given_answer == correct_answer else "Incorrect",

    }


def get_answer(available_answers):
    answer = ""
    while True:
        try:
            answer = input("Enter your answer: ").strip()
            index = int(answer) - 1
            return available_answers[index]
        except ValueError:
            print(f"{answer} is not a valid answer")


def print_results(result_list):
    correct_answers = 0
    for answer in result_list:
        print(f"{answer['status']} Answer: \t User Answer: {answer['user_answer'].ljust(10)} \t "
              f"Correct Answer: {answer['correct_answer']}")
        if answer['status'] == 'Correct':
            correct_answers += 1
    print(f"Score {correct_answers} / {len(result_list)}")