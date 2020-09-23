def power_digit_sum(power_of_two):
    number = str(2 ** power_of_two)
    return sum([int(i) for i in number])


if __name__ == "__main__":
    print(power_digit_sum(1000))
