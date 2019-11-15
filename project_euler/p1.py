def sum_of_3_and_5_multiples(limit):
    sum = 0
    i = 0
    while(i < limit):
        if(i % 3 == 0 or i % 5 == 0):
            sum += i
        i += 1
    return sum


def main():
    print(sum_of_3_and_5_multiples(1000))


if __name__ == "__main__":
    main()
