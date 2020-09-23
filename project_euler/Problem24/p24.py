import math


def swap(item1, item2):
    temp = item1
    item2 = item1
    item1 = temp


def nth_lexicographic_permutation(nth):
    perm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    N = len(perm)
    permNum = ""
    remain = nth - 1

    numbers = []
    for i in range(0, N):
        numbers += [i]

    for i in range(1, N):
        j = (int)(remain/math.factorial(N-i))
        remain = remain % math.factorial(N-i)

        permNum = permNum + str(numbers[j])
        del numbers[j]
        if (remain == 0):
            break

    for i in range(0, len(numbers)):
        permNum += str(numbers[i])

    return(permNum)


if __name__ == "__main__":
    print(nth_lexicographic_permutation(1000000))
