def difference_bt_sq_sum_and_sum_sq(num):
    sum_sq, sq_sum = 0, 0
    i, j = 1, 1
    while (i <= num and j <= num):
        sum_sq += i * i
        sq_sum += i
        i += 1
        j += 1
    return sq_sum * sq_sum - sum_sq


def main():
    print(difference_bt_sq_sum_and_sum_sq(100))


if __name__ == "__main__":
    main()
