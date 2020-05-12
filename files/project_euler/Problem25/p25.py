import sys

sys.setrecursionlimit(10**6)


def fibonacci(term_num):
    if(term_num == 1 or term_num == 2):
        return 1
    else:
        return (fibonacci(term_num-1)+fibonacci(term_num-2))


def check_first_fib_term_over(limit):
    third_last_term = 1
    second_last_term = 1
    last_term = 2
    term_index = 3
    while(last_term < limit):
        temp = last_term
        last_term += second_last_term
        third_last_term = second_last_term
        second_last_term = temp
        term_index += 1
    return term_index


if __name__ == "__main__":
    print(check_first_fib_term_over(10**999))
