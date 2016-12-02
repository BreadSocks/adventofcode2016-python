currentPasscode = ""
# current_x = 1 # 2nd column
# current_y = 1 # 2nd row
current_x = 0 # 1st column
current_y = 2 # 3rd row

num_pad = {}
# num_pad[0, 0] = 1
# num_pad[1, 0] = 2
# num_pad[2, 0] = 3
# num_pad[0, 1] = 4
# num_pad[1, 1] = 5
# num_pad[2, 1] = 6
# num_pad[0, 2] = 7
# num_pad[1, 2] = 8
# num_pad[2, 2] = 9

num_pad[2, 0] = 1
num_pad[1, 1] = 2
num_pad[2, 1] = 3
num_pad[3, 1] = 4
num_pad[0, 2] = 5
num_pad[1, 2] = 6
num_pad[2, 2] = 7
num_pad[3, 2] = 8
num_pad[4, 2] = 9
num_pad[1, 3] = 'A'
num_pad[2, 3] = 'B'
num_pad[3, 3] = 'C'
num_pad[2, 4] = 'D'

passcode = ""

print num_pad

with open("input.txt") as inputFile:
    for line in inputFile:
        for character in line:
            new_x, new_y = current_x, current_y
            if character == 'U':
                new_y -= 1
            elif character == 'D':
                new_y += 1
            elif character == 'L':
                new_x -= 1
            elif character == 'R':
                new_x += 1
            else:
                print "Found end of line"
                break

            check_key = (new_x, new_y)
            if check_key not in num_pad:
                new_x, new_y = current_x, current_y
            else:
                current_x, current_y = new_x, new_y

        num_pad_digit = num_pad[current_x, current_y]
        passcode += str(num_pad_digit)
        print "line finished at position", current_x, current_y, "landing on digit", num_pad[current_x, current_y]

print passcode