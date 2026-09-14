from operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root
)


def show_menu():
    print("\n=== PYTHON CALCULATOR V2 ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square root")
    print("0. Exit")


def main():
    while True:
        show_menu()

        option = input("Select an operation: ")

        if option == "0":
            print("Calculator closed.")
            break

        if option == "6":
            number = float(input("Enter a number: "))
            result = square_root(number)
            print(f"Result: {result}")
            continue

        if option not in ["1", "2", "3", "4", "5"]:
            print("Invalid option.")
            continue

        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if option == "1":
            result = add(a, b)
        elif option == "2":
            result = subtract(a, b)
        elif option == "3":
            result = multiply(a, b)
        elif option == "4":
            result = divide(a, b)
        elif option == "5":
            result = power(a, b)

        print(f"Result: {result}")


if __name__ == "__main__":
    main()