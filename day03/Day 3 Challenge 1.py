invalid_triangles = 0
valid_triangles = 0

with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.strip()
        sides = line.split(" ")
        while "" in sides: sides.remove("") # remove extra spaces between values and smaller numbers

        if int(sides[0]) + int(sides[1]) > int(sides[2]) and int(sides[1]) + int(sides[2]) > int(sides[0]) and int(sides[2]) + int(sides[0]) > int(sides[1]):
            valid_triangles += 1
        else:
            invalid_triangles += 1

print "Out of", valid_triangles + invalid_triangles, valid_triangles, "are valid"