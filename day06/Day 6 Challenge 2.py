columns = []
word = ""

with open("input.txt") as inputFile:
    for i, line in enumerate(inputFile):

        line = line.strip()

        if i == 0:  # first line, work out how many columns
            for x in range(len(line)):
                columns.append([])

        for index, letter in enumerate(line):
            columns[index].append(letter)

print "Found columns:"
for column in columns:
    print "".join(column)
    character = min(set(column), key=column.count)
    word += character

print "Found word:", word
