def sum_of_amicable_numbers_under(num):
    sum = 0
    for i in range(0, num):
        divisors_i = find_divisor_sum(i)


def find_divisor_sum(num):
    sum = 0
    for i in range(1, num/2+1):
        if(num % i == 0):
            sum += i
    return sum


if __name__ == "__main__":
    print(sum_of_amicable_numbers_under(10000))
