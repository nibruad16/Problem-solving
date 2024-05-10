def split_and_join(line):
    l = line.split(" ")
    y = "-".join(l)
    return y

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
