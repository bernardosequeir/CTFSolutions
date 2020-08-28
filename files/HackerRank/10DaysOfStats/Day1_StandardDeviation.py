size = int(input())
numbers = list(map(int, input().split()))
mean = sum(numbers) / size
n = 0
for number in numbers:
    n += pow(number-mean, 2)
print(round(n/size, 1))
