import math


def Sieve_E(upper_limit):

    prime_bool = [True for i in range(upper_limit+1)]
    prime_list = []
    p = 2
    while(p * p <= upper_limit):
        if(prime_bool[p]):
            for i in range(p*2, upper_limit + 1, p):
                prime_bool[i] = False
        p += 1
    prime_bool[0] = False
    prime_bool[1] = False

    return [i for i in range(2, upper_limit+1) if prime_bool[i]]


def sumOfFactorsPrime(number, prime_list):
    n = number
    factors_sum = 1
    p = prime_list[0]
    i = 0

    while (p * p <= n and n > 1 and i < len(prime_list)):
        p = prime_list[i]
        i += 1
        if (n % p == 0):
            j = p * p
            n = n / p
            while (n % p == 0):
                j = j * p
                n = n / p
            factors_sum = factors_sum * (j - 1) / (p - 1)
    if(n > 1):
        factors_sum *= n + 1

    return int(factors_sum - number)


def non_abundant_sums():
    limit = 28123  # All numbers greater than this can be written as the sum of two abundant numbers
    abundant = []
    prime_list = Sieve_E((int)(math.sqrt(limit)))

    # figuring out all abundant numbers under the limit
    for i in range(2, limit):
        if (sumOfFactorsPrime(i, prime_list) > i):
            abundant += [i]

    can_be_written_as_Abundant = [False for i in range(0, limit+1)]
    for i in range(0, len(abundant)):
        for j in range(i, len(abundant)):
            if(abundant[i] + abundant[j] <= limit):
                can_be_written_as_Abundant[abundant[i]+abundant[j]] = True
            else:
                break

    return sum([i for i in range(1, limit+1) if can_be_written_as_Abundant[i] == False])


if __name__ == "__main__":
    print(non_abundant_sums())
