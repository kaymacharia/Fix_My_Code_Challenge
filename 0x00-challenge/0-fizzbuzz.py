import sys

def fizzbuzz(n):
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if not output:
            output = i
        print(output, end=" ")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        fizzbuzz(n)
    except ValueError:
        print("Please provide a valid number.")
