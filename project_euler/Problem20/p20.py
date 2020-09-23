from math import factorial


def factorial_digit_sum(number):
    return sum([int(i) for i in str(factorial(number))])


if __name__ == "__main__":
    print(factorial_digit_sum(100))
