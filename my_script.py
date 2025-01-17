def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        num = 20
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is: {result}")
            print("Ajays contribution")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
