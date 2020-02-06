number_len_dict = {
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety"),
    1000: len("onethousand")
}


def get_letter_count_1_to_1000():
    count = 0
    for i in range(1, 1000+1):
        if(i < 20):
            count += number_len_dict.get(i)
            print(count)
        elif(i < 100):
            ones = i % 10
            tens = (i-ones) % 100
            count += number_len_dict.get(tens, 0) + \
                number_len_dict.get(ones, 0)
            print(count)
        elif(i < 1000):
            ones = i % 10
            tens = (i-ones) % 100
            hundreds = (i - ones - tens) % 1000 / 100
            if(ones + tens < 20):
                count += number_len_dict.get(ones + tens, 0) + \
                    len("hundredand") + number_len_dict.get(hundreds, 0)
            else:
                count += number_len_dict.get(ones, 0) + number_len_dict.get(tens, 0) + \
                    len("hundredand") + number_len_dict.get(hundreds, 0)
        else:
            count += number_len_dict.get(1000)
    return count


if __name__ == "__main__":
    print(get_letter_count_1_to_1000())
