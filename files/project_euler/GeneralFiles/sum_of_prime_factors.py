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
