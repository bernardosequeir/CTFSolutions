from math import factorial
chance_boy = 1.09 / 2.09


def combination(n, k):
    if (k > n):
        return 0
    else:
        return factorial(n) / (factorial(k) * factorial(n-k))


def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1-p, n-k)


prob = 0

for i in range(3, 6+1):
    prob += round(binomial(6, i, chance_boy), 3)
print(prob)
