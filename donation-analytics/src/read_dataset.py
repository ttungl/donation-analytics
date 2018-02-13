input_file1 = None
input_file2 = None

def set_inputs(filename1, filename2):
    global input_file1, input_file2
    input_file1, input_file2 = filename1, filename2
    return


def getLine(lineNumber): 
    with open(input_file1, "r") as fp:
        for i, line in enumerate(fp):
            if i == lineNumber-1:
                return line
            if line == '\n':
                return None

def getPercentile(perNumber):
    with open(input_file2, "r") as fp:
        for i, num in enumerate(fp):
            if i==perNumber: 
                return int(num.strip())
            if num == '\n': 
                return None


def readPercentile(percentNumber):
    percentile = getPercentile(percentNumber)
    return percentile


def readline(lineCounter):
    rawline =getLine(lineCounter)
    return rawline


def split(rawLine):
    splittedRawLine = rawLine.split("|")
    return splittedRawLine
