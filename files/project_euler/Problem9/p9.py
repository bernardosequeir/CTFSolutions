def find_pythagorean_triplet_sum(sum):
    c = 1
    while(c < sum):
        c += 1
        b = 1
        while(b < c):
            a = 1
            while(a < b):
                if (check_pythagorean_triplet(a, b, c) and (a + b + c) == sum):
                    return [a, b, c]
                a += 1
            b += 1


def check_pythagorean_triplet(a, b, c):
    return (a ** 2 + b ** 2) == c ** 2


def main():
    a, b, c = find_pythagorean_triplet_sum(1000)
    print(a * b * c)


if __name__ == "__main__":
    main()
