def sorter():
    with open("p022_names.txt", "r") as reader:
        list = reader.read()
    list = list.strip().split(",")
    list = [x[1:-1] for x in list]
    list.sort()
    result = 0
    for i in range(0, len(list)):
        result += score(list[i])*(i+1)
    return result


def score(name):
    chars = list(name)
    chars = [ord(x)-64 for x in chars]  # 64 is the ascii value before A
    return sum(chars)
    

if __name__ == "__main__":
    print(sorter())
