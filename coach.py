def bmi_calculator():
    print("===== Calculate Your BMI (Body Mass Index) =====\n")

    while True:
        try:
            print(
                "Select the measurement system:\n"
                "A) Kilogram (kg) and Centimeter (cm)\n"
                "B) Kilogram (kg) and Meter (m)\n"
                "C) Pounds (lb) and Feet/Inches (ft/in)\n"
            )

            unit = input("Select an option (a, b, or c): ").lower()
            print()

            if unit == "a":
                weight = get_weight("a")
                print()
                height = get_height("a")
                print()
                bmi = weight / height
                print(f"Your BMI is: {bmi:.1f}")
                break

            elif unit == "b":
                weight = get_weight("b")
                print()
                height = get_height("b")
                print()
                bmi = weight / height
                print(f"Your BMI is: {bmi:.1f}")
                break

            elif unit == "c":
                weight = get_weight("c")
                print()
                height = get_height("c")
                print()
                bmi = weight / height
                print(f"Your BMI is: {bmi:.1f}")
                break

        except ValueError:
            continue


def get_weight(n):
    while True:
        try:
            if n == "a":
                return int(input("Enter your weight in kilograms: "))
            elif n == "b":
                return int(input("Enter your weight in kilograms: "))
            elif n == "c":
                return int(input("Enter your weight in pounds: ")) * 703
        except ValueError:
            continue


def get_height(n):
    while True:
        try:
            if n == "a":
                height = int(input("Enter your height in centimeters: "))
                return (height / 100) ** 2

            elif n == "b":
                height = int(input("Enter your height in meters: "))
                return height ** 2

            elif n == "c":
                feet = int(input("Enter your height in feet: "))
                inches = int(input("Enter your height in inches: "))
                return (feet * 12 + inches) ** 2
        except ValueError:
            continue


if __name__ == "__main__":
    bmi_calculator()
