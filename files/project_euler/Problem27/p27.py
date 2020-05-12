
def Sieve_E(upper_limit):

    prime_bool = [True for i in range(upper_limit+1)]
    prime_list = []
    p = 2
    while(p * p <= upper_limit):
        if(prime_bool[p]):
            for i in range(p*2, upper_limit + 1, p):
                prime_bool[i] = False
        p += 1
    prime_bool[0] = False
    prime_bool[1] = False

    return [i for i in range(2, upper_limit+1) if prime_bool[i]]


def is_prime(num):
    nums = range(2, int(num ** 0.5)+1)
    for i in nums:
        if(num % i == 0):
            return False
    return True


def check_sequence(a, b):
    sequence = 1
    i = 1
    prime = 1 + a + b
    while(is_prime(abs(prime))):
        sequence += 1
        i += 1
        prime = i**2 + i * a + b
    return sequence


def find_longest_quadratic_prime_sequence():
    possible_a_b = Sieve_E(1000)
    val_a = 0
    val_b = 0
    highest_sequence = 0
    for b in possible_a_b:
        for a in possible_a_b:
            possible_sequence = check_sequence(a, b)
            if(possible_sequence > highest_sequence):
                highest_sequence = possible_sequence
                val_a = a
                val_b = b
            possible_sequence = check_sequence(-a, b)
            if(possible_sequence > highest_sequence):
                highest_sequence = possible_sequence
                val_a = -a
                val_b = b
            """possible_sequence = check_sequence(a, -b)
            if(possible_sequence > highest_sequence):
                highest_sequence = possible_sequence
                val_a = a
                val_b = -b
            possible_sequence = check_sequence(-a, -b)
            if(possible_sequence > highest_sequence):
                highest_sequence = possible_sequence
                val_a = -a
                val_b = -b"""
    return val_a * val_b


if __name__ == "__main__":
    print(find_longest_quadratic_prime_sequence())
