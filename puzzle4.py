def has_doubles(number):
    repetitions = {}
    string = str(number)

    for index, char in enumerate(string):
        if char in repetitions:
            repetitions[char].append(index)
        else:
            repetitions[char] = [index]

    for key in repetitions:
        if len(repetitions[key]) == 2 and repetitions[key][1] - repetitions[key][0] == 1:
            return True

    return False


def has_match(number):    
    digits = [ int(x) for x in str(number) ]
    length = len(digits) - 1

    for j in range(length):
        if digits[j] > digits[j+1]:
            return False

    return has_doubles(number)


def main():
    hits = 0

    for i in range(146810, 612565):
        if has_match(i):
            hits += 1

    print(hits)


if __name__ == "__main__":
    main() 