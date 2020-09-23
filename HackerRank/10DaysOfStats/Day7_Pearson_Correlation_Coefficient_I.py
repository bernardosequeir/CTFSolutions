def mean(x):
    return round(sum(x)/float(n), 1)


def standardDeviation(values, mean):
    data = [(val-mean)**2 for val in values]
    return (sum(data)/float(len(data)))**0.5


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
mean_x = mean(X)
std_dev_x = standardDeviation(X, mean_x)
mean_y = mean(Y)
std_dev_y = standardDeviation(Y, mean_y)
sum = 0
for i in range(n):
    sum += (X[i]-mean_x)*(Y[i]-mean_y)

print(round(sum/(n*std_dev_x*std_dev_y), 3))
