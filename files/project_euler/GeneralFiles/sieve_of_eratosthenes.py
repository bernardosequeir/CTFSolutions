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


if __name__ == "__main__":
    print(Sieve_E(15))
