from math import factorial
chance_defective = 0.12


def combination(n, k):
    if (k > n):
        return 0
    else:
        return factorial(n) / (factorial(k) * factorial(n-k))


def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1-p, n-k)


prob_no_more_than_2 = 0
prob_more_than_2 = 0
for i in range(0, 2+1):
    prob_no_more_than_2 += binomial(10, i, chance_defective)
for i in range(2, 10+1):
    prob_more_than_2 += binomial(10, i, chance_defective)
print(round(prob_no_more_than_2, 3))
print(round(prob_more_than_2, 3))
