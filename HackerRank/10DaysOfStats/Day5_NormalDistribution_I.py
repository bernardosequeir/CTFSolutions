from math import sqrt, pi, e, erf
mean = 20
standard_deviation = 2
variance = 2 ** 2


def normal_pdf(x, mean, variance):
    return 1/(sqrt(variance)*sqrt(2*pi)) * pow(e, -pow(x-mean, 2)/2*variance)


def normal_cdf(x, mean, standard_deviation):
    return 0.5 + 0.5 * erf((x-mean)/(standard_deviation * 2 ** 0.5))


if __name__ == "__main__":
    print(round(normal_cdf(19.5, mean, standard_deviation), 3))
    print(round(normal_cdf(22, mean, standard_deviation) -
                normal_cdf(20, mean, standard_deviation), 3))
