def find_nth_prime(nth):
    num_primes = 2
    prime = 2
    n = 3
    while(num_primes <= nth):
        if(is_prime(n)):
            prime = n
            num_primes += 1
        n += 2
    return prime


def is_prime(num):
    nums = range(2, int(num ** 0.5)+1)
    for i in nums:
        if(num % i == 0):
            return False
    return True


def main():
    print(find_nth_prime(10001))


if __name__ == "__main__":
    main()
