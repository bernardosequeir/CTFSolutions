def is_prime(num):
    nums = range(2, int(num ** 0.5)+1)
    for i in nums:
        if(num % i == 0):
            return False
    return True


def prime_sum_until(limit):
    sum = 2
    n = 3
    while(n <= limit):
        if(is_prime(n)):
            sum += n
        n += 2
    return sum


def main():
    print(prime_sum_until(2000000))
    print(prime_sum_until(10))


if __name__ == "__main__":
    main()
