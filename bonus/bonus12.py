CONVERT_FEET_TO_METERS = 0.3048


def convert(total_feet):
    return total_feet * CONVERT_FEET_TO_METERS


def user_input():
    feet_inches = input("Enter feet and inches: ")
    measurements = feet_inches.split()
    return {
        "feet": float(measurements[0]),
        "inches": float(measurements[1]) / 12 if len(measurements) > 1 else 0
    }


if __name__ == '__main__':
    parts = user_input()
    total_meters = convert(parts['feet'] + parts['inches'])
    print(f"Feet = {parts['feet']}\nInches = {parts['inches']:.2f}\nTotal feet = {parts['feet'] + parts['inches']:.2f}\nTotal meters = {total_meters:.2f}")
    if total_meters > 0.5:
        print("You can use the slide!")
    else:
        print("Sorry, You can't use the slide.")


