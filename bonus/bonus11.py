# Program that gets integers from a text file and returns the sum

FILE_LOCATION = 'bonus11/bonus11.txt'


def read_file():
    with open(FILE_LOCATION, 'r') as file:
        return file.readlines()


def get_temperatures():
    temperatures = []
    lines = read_file()
    for line in lines:
        try:
            temperatures.append(float(line.strip('\n')))
        except ValueError:
            exit("Value received was not an integer")
    return temperatures


def main():
    integers = get_temperatures()
    sum_value = sum(integers)
    average_value = sum_value/len(integers)
    print(f"sum = {sum_value}")
    print(f"average = {average_value}")


if __name__ == '__main__':
    main()
