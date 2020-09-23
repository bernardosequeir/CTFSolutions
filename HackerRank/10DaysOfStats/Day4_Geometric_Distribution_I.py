def geometric(n, p):
    return pow(1-p, n-1) * p


p = 1/3
prob = sum([geometric(i, p) for i in range(1, 5+1)])
print(round(prob, 3))
