import calculator_utils


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(f"Addition: {calculator_utils.add(a, b)}")
    print(f"Subtraction: {calculator_utils.sub(a, b)}")
    print(f"Multiplication: {calculator_utils.mul(a, b)}")
    print(f"Division: {calculator_utils.div(a, b)}")


main()
