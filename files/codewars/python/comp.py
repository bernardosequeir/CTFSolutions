def comp(array1, array2):
    if(array1 is None or array2 is None):
        return False
    if len(array1) != len(array2):
        return False
    elif(len(array1) == 0 or len(array2) == 0):
        return False
    else:
        squared_array = []
        for val in array1:
            squared_array.append(pow(val, 2))
        for val in array2:
            if(val not in squared_array):
                return False
    return True


if __name__ == "__main__":
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [
          121, 14641, 20736, 361, 25921, 361, 20736, 361]))
