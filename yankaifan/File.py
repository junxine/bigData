def rA():
    with open("E:\\时间简史.txt") as f:
        lines=f.readlines()
        for line in lines:
            print(line)
def rB():
    with open("E:\\时间简史.txt") as f:
        while line := f.readline():
            print(line)
def rC():
    for line in open("E:\\时间简史.txt"):
        print(line)
if __name__ == '__main__':
    rA()