import sys

filename = sys.argv[1]
classes = ['galsworthy','galsworthy_2','mill','shelley','thackerey','thackerey_2','wordsmith_prose','cia','johnfranklinjameson','diplomaticcorr']



def clean(line):
    return line.strip()


def verify(datalines, list_of_classes):
    for line in datalines:
        line = clean(line)
        if line not in list_of_classes:
            print line
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
