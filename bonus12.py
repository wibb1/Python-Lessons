CONVERT_FEET_TO_METERS = 0.3048


def convert(total_feet):
    return total_feet * CONVERT_FEET_TO_METERS


def user_input():
    feet_inches = input("Enter feet and inches: ")
    measurements = feet_inches.split()
    return [
        float(measurements[0]),
        float(measurements[1]) / 12 if len(measurements) > 1 else 0
    ]


if __name__ == '__main__':
    [feet, inches] = user_input()
    total_meters = convert(feet + inches)
    print(f"Feet = {feet}\nInches = {inches:.2f}\nTotal feet = {feet + inches:.2f}\nTotal meters = {total_meters:.2f}")
    if total_meters > 0.5:
        print("You can use the slide!")
    else:
        print("Sorry, You can't use the slide.")


