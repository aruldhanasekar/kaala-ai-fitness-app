def bmi_calculator():
    print("=====Calculate you BMI(BODY MASS INDEX)=====")
    print("")
    print("")

    while True:
        try:
            print("Select your metrics scale: \nA) Kilogram(kg) and Centimeter(cm). \nB) Kilogram(kg) and Meter(m) \nC)Pounds(lb) and Feet(ft)/inches(in)\n")

            unit = input("Select the option: ").lower()
            print("\n")

            if unit == "a":
               weight =  get_weight("a")
               print("\n")
               height =  get_height("a")
               print("\n")
               bmi = weight / height
               print(f"Here is your BMI: {bmi:.1f}")
               break
            elif unit == "b":
                weight =  get_weight("b")
                print("\n")
                height =  get_height("b")
                print("\n")
                bmi = weight / height
                print(f"Here is your BMI: {bmi:.1f}")
                break
            elif unit == "c":
                weight =  get_weight("c")
                print("\n")
                height =  get_height("c")
                print("\n")
                bmi = weight / height
                print(f"Here is your BMI: {bmi:.1f}")
                break

        except ValueError:
            continue


def get_weight(n):
    while True:
        try:
            if n == "a":
                weight = int(input("Enter you weight in kg: "))
                return weight
            elif n == "b":
                weight = int(input("Enter your weight in kg: "))
                return weight
            elif n == "c":
                weight = int(input("Enter your weight in the lb: "))
                return weight * 703
        except ValueError:
            continue

def get_height(n):
    while True:
        try:
            if n == "a":
                height = int(input("Enter your height in cm: "))
                # It converts cm to m and m^2 (weight / m^2)
                return (height / 100) ** 2
            elif n == "b":
                height = int(input("Enter your height in m: "))
                return (height ** 2)
            elif n == "c":
                feet = int(input("Enter your input in feet: "))
                inches = int(input("Enter your input in inches: "))
                height = ((feet * 12 + inches)  ** 2)
                return height
        except ValueError:
            continue


if __name__ == "__main__":
    bmi_calculator()