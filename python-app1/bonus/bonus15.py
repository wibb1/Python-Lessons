import bonus15_functions


def main():
    data = bonus15_functions.open_file()
    data.pop(0)
    results = []
    for question in data:
        answer_list = question[1].split(",")

        correct_answer = question[2]

        bonus15_functions.print_answer_list(answer_list)

        user_answer = bonus15_functions.get_answer(answer_list)

        results.append(bonus15_functions.evaluate_answer(user_answer, correct_answer))

    bonus15_functions.print_results(results)


if __name__ == '__main__':
    main()
