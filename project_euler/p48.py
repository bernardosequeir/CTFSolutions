def self_powers_series_last_10_digits():
    sum = 0
    for i in range(1, 1001):
        sum += i**i
    print(str(sum)[-10:])


if __name__ == "__main__":
    self_powers_series_last_10_digits()
