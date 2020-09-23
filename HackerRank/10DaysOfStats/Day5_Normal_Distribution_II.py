from math import sqrt, pi, e, erf
mean = 70
standard_deviation = 10


def normal_pdf(x, mean, variance):
    return 1/(sqrt(variance)*sqrt(2*pi)) * pow(e, -pow(x-mean, 2)/2*variance)


def normal_cdf(x, mean, standard_deviation):
    return 0.5 + 0.5 * erf((x-mean)/(standard_deviation * 2 ** 0.5))


print(round((1 -
             normal_cdf(80, mean, standard_deviation))*100, 2))
print(round((1 -
             normal_cdf(60, mean, standard_deviation))*100, 2))
print(round(normal_cdf(60, mean, standard_deviation)*100, 2))
