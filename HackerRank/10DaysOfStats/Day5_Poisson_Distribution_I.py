from math import factorial, e


def poisson(k, delta):
    return pow(delta, k) * pow(e, -delta) / factorial(k)


if __name__ == "__main__":
    print(round(poisson(5, 2.5), 3))
