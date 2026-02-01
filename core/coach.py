from health_checks.bmi import bmi_calculator

"""
Kaala is your AI fitness coach.
"""


def coach_intro():
    print("==============================\n")
    print("Hi, I am Kaala, your AI fitness coach.\n")
    client_intro()


def client_intro():
    print("I need a few details to get started.\n")

    name = input("Enter your name: ").title()
    age = int(input("Enter your age: "))
    gender = input("Male(M) or Female(F): ")
    country = input("Enter your country: ")

    print("\n")

    checkup_list(name, age)


def checkup_list(name, age):
    print("==============================\n")
    print(f"What would you like to check now, {name}?")

    print("A) BMI check")
    print("B) Other")

    option = input("Select an option (a or b): ").lower()

    if option == "a":
        bmi_checkup(age)
    elif option == "b":
        print(f"\nCurrently, only BMI check is available, {name}.")
        y_n = input("Do you want to check your BMI? (y/n): ").lower()

        if y_n == "y":
            bmi_checkup(age)
        else:
            print(f"\nThank you for using Kaala, {name}.")


def bmi_checkup(age):
    bmi_calculator(age)


if __name__ == "__main__":
    coach_intro()
