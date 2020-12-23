def fizz_buzz(input):
    output = ""

    if input % 3 == 0:
        output = "Fizz"
    if input % 5 == 0:
        output += "Buzz"

    return output if output else input


def print_first_100():
    for i in range(1, 101):
        print(fizz_buzz(int(i)))
