import math


def num_of_divisors(num):
    divisor_count = 0
    i = 1
    while (i < math.sqrt(num)):
        if(num % i == 0):
            if(num / i == i):
                divisor_count += 1
            else:
                divisor_count += 2
        i += 1
    return divisor_count


def find_triangular_number_with_n_divisors(limit):
    i = 1
    divisors = 0
    triangular_num = 0
    while(divisors < limit):
        triangular_num += i
        divisors = num_of_divisors(triangular_num)
        print(f"Triangular number: {triangular_num}")
        print(f"Try number: {i}")
        print(f"Number of divisors: {divisors}")
        i += 1
    return triangular_num


def main():
    print(
        f"And the number issssssss: {find_triangular_number_with_n_divisors(500)}!!")


if __name__ == "__main__":
    main()
