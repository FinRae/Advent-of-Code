def parseinput():
    # This function is to parse the initial input into a usable form
    with open("input.dat") as file:
        input = file.readlines()
        file.close()
    return input

def task1(input):
    count = 0
    for line in input:
        digits = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                digits += line[i]
                break
        for i in range(len(line)):
            if line[::-1][i].isnumeric():
                digits += line[::-1][i]
                break
        count += int(digits)
    return count


def replacenums(line):
    numberdict = {"one":"o1e", "two":"t2o", "three":"t3e",
                  "four":"f4r", "five":"f5e", "six":"s6x",
                  "seven":"s7n","eight":"e8t", "nine":"n9e"}
    for key in numberdict:
            line =line.replace(key, numberdict[key])

    return line


def task2(input):
    count = 0
    for line in input:
        line = replacenums(line).strip()
        digits = ""
        for i in range(len(line)):
            if line[i].isdigit():
                digits += line[i]
                break
        for i in range(len(line)):
            if line[::-1][i].isdigit():
                digits += line[::-1][i]
                break
        count += int(digits)
    return count


if __name__ == "__main__":
    print(task1(parseinput()))
    print(task2(parseinput()))