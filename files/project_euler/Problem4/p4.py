def largest_palindrome_3_digit():
    num1, num2, biggest = 100, 100, 0
    while num1 < 1000:
        while num2 < 1000:
            mul = str(num1 * num2)
            if(mul[0] == mul[-1]):
                if(mul[1] == mul[-2]):
                    if(len(mul) == 6):
                        if(mul[2] == mul[-3]):
                            if (int(mul) > biggest):
                                biggest = int(mul)
                    else:
                        if (int(mul) > biggest):
                            biggest = int(mul)
            num2 += 1
        num1 += 1
        num2 = 100
    return biggest, num1, num2


def main():
    print(largest_palindrome_3_digit())


if __name__ == "__main__":
    main()
