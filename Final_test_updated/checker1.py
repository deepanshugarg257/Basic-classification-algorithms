import sys

filename = sys.argv[1]
classes = ["0", "1"]


def clean(line):
    return line.strip()


def verify(datalines, list_of_classes):
    for line in datalines:
        line = clean(line)
        if line not in list_of_classes:
            return "ERROR"
    return "OK"


def readdata():
    with open(filename) as f:
        tempdata = f.readlines()
    return tempdata

if __name__ == "__main__":
    data = readdata()
    result = verify(data, classes)
    print result
