def bmi_calculator(age: int):
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
               bmi_results(weight, height, age)
               break
            elif unit == "b":
                weight =  get_weight("b")
                print("\n")
                height =  get_height("b")
                print("\n")
                bmi_results(weight, height, age)
                break
            elif unit == "c":
                weight =  get_weight("c")
                print("\n")
                height =  get_height("c")
                print("\n")
                bmi_results(weight, height, age)
                break

        except ValueError:
            continue

def bmi_results(weight, height, age):
    
    results = weight / height

    if 0 < results < 18.5:
        print(f"Here is your BMI: {results:.1f}")
        print(f"At this {age}, this is Underweight (Less weight)")
    elif 18.5 <= results < 24.9:
        print(f"Here is your BMI: {results:.1f}")
        print(f"At this {age}, this is  Normal (Correct weight)")
    elif 25.0 <= results < 29.9:
        print(f"Here is your BMI: {results:.1f}")
        print(f"At this {age}, this is Overweight")
    elif results > 30.0:
        print(f"Here is your BMI: {results:.1f}")
        print(f"At this {age}, this is Obesity")


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