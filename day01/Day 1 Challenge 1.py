data = open("input.txt").read()
example1 = "R2, L3"
example2 = "R2, R2, R2"
example3 = "R5, L5, R5, R3"
x, y = 0, 0
direction = 1 # 1 North 2 East 3 South 4 West
moves = data.split(", ")
for move in moves:
    if move.__contains__("R"):
        direction += 1
    else:
        direction -= 1

    # reset direction if full circle clockwise or counter clockwise
    if direction < 1:
        direction = 4
    elif direction > 4:
        direction = 1

    move_distance = int(move.replace("L", "").replace("R", ""))

    if direction == 1:
        y += move_distance
    elif direction == 2:
        x += move_distance
    elif direction == 3:
        y -= move_distance
    elif direction == 4:
        x -= move_distance
    else:
        print "Error"

    print x, y
print str(x+y) + " squares away"

