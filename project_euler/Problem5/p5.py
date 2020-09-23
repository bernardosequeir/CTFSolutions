def smallest_evenly_divisible():
    divisor = 20
    smallest = 2520
    while divisor != 1:
        if(smallest % divisor == 0):
            divisor -= 1
        else:
            divisor = 20
            smallest += 1

    return smallest


def main():
    print(smallest_evenly_divisible())


if __name__ == "__main__":
    main()
