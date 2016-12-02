currentPasscode = ""
current_x = 1 # 2nd column
current_y = 1 # 2nd row

num_pad = {}
num_pad[0, 0] = 1
num_pad[1, 0] = 2
num_pad[2, 0] = 3
num_pad[0, 1] = 4
num_pad[1, 1] = 5
num_pad[2, 1] = 6
num_pad[0, 2] = 7
num_pad[1, 2] = 8
num_pad[2, 2] = 9

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

            if new_x < 0 or new_x > 2:
                new_x = current_x # reset back to previous value

            if new_y < 0 or new_y > 2:
                new_y = current_y # reset back to previous value

            # print "Landed at", new_x, new_y
            current_x, current_y = new_x, new_y

        num_pad_digit = num_pad[current_x, current_y]
        passcode += str(num_pad_digit)
        print "line finished at position", current_x, current_y, "landing on digit", num_pad[current_x, current_y]

        # if new_x < current_x and new_x >= 0: # valid x

print passcode