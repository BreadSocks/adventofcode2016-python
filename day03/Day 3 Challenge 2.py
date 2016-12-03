invalid_triangles = 0
valid_triangles = 0

column_1 = []
column_2 = []
column_3 = []

with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.strip()
        sides = line.split(" ")
        while "" in sides: sides.remove("") # remove extra spaces between values and smaller numbers
        column_1.append(int(sides[0]))
        column_2.append(int(sides[1]))
        column_3.append(int(sides[2]))

# print "First Column:", column_1
# print "Second Column:", column_2
# print "Third Column:", column_3

columns = [column_1, column_2, column_3]
for column in columns:
    while len(column) > 0:
        first, second, third = column[0], column[1], column[2]
        if first + second > third and second + third > first and third + first > second:
            valid_triangles += 1
        else:
            invalid_triangles += 1
        column.remove(first)
        column.remove(second)
        column.remove(third)

print "Using columns there are", valid_triangles, "valid triangles and", invalid_triangles, "invalid"