data = open("input.txt").read()
example1 = "R8, R4, R4, R8"
x, y = 0, 0
previous_x, previous_y = 0, 0
visited_squares = [{0: 0}]
direction = 1 # 1 North 2 East 3 South 4 West
moves = data.split(", ")
for move in moves:

    # previous_x = dict(visited_squares).keys
    previous_move = visited_squares[-1]
    previous_x = previous_move.keys()[0]
    previous_y = previous_move.values()[0]
    # print "Previous square was", previous_x, previous_y

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

    # print x, y

    if x is previous_x and y is previous_y:
        print "Visiting", x, y, "for the second time"

    if x > previous_x:
        for x_axis in range(previous_x + 1, x):
            square = {x_axis: y}
            if visited_squares.__contains__(square):
                print "Visiting", square, "for the second time"
            else:
                visited_squares.append(square)

    if x < previous_x:
        for x_axis in range(previous_x - 1, x, -1):
            square = {x_axis: y}
            if visited_squares.__contains__(square):
                print "Visiting", square, "for the second time"
            else:
                visited_squares.append(square)

    if y > previous_y:
        for y_axis in range (previous_y + 1, y):
            square = {x: y_axis}
            if visited_squares.__contains__(square):
                print "Visiting", square, "for the second time"
            else:
                visited_squares.append(square)

    if y < previous_y:
        for y_axis in range (previous_y -1, y, -1):
            square = {x: y_axis}
            if visited_squares.__contains__(square):
                print "Visiting", square, "for the second time"
            else:
                visited_squares.append(square)

    square = {x: y}
    if visited_squares.__contains__(square):
        print "Visiting", square, "for the second time"
    else:
        visited_squares.append(square)

print str(x+y) + " squares away"
# print visited_squares
