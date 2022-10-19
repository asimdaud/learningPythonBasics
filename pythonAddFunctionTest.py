# Adds and multiplies the integers provided.
# To run --> pyhton pythonAddFunctionTest.py


def adding(a, b):
    try:
        a = int(a)
        return a + b
    except ValueError:
        if user_input != "exit" and user_input != "Exit" and user_input != "EXIT":
            print("Can't run the program!!")
        else:
            print("Terminating the program!")


def multiply(a, b):
    try:
        a = int(a)
        return a * b
    except ValueError:
        if user_input != "exit" and user_input != "Exit" and user_input != "EXIT":
            print("Can't run the program!")
        else:
            print("Terminating the program!")


def start():
    try:
        user_input = ""
        initial_choice = int(input("Enter 1 for addition and 2 for multiplication: \n"))
        while (
            user_input != "exit" and user_input != "Exit" and user_input != "EXIT"
        ) and (int(initial_choice) == 1 or int(initial_choice) == 2):
            if int(initial_choice) == 1:
                user_input = input("Enter numbers to add separating with comma (,): \n")
                var_add = 0
                for number_element in user_input.split(","):
                    var_add = adding(number_element, var_add)
                print("The answer is: ", var_add)
            elif int(initial_choice) == 2:
                user_input = input(
                    "Enter numbers to multiply separating with comma (,): \n"
                )
                var_multiply = 1
                for number_element in user_input.split(","):
                    var_multiply = multiply(number_element, var_multiply)
                print("The answer is: ", var_multiply)
    except ValueError:
        print("Invalid choice, terminating program...")


start()
