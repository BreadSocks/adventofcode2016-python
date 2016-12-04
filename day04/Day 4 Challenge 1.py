from room import Room

valid_rooms = []

print "\nFound rooms:"
with open("input.txt") as inputFile:
    for line in inputFile:
        room = Room(line)
        print room
        if room.is_valid():
            valid_rooms.append(room)

sector_id_sum = 0
print "\nFound valid rooms:"
for room in valid_rooms:
    print room
    sector_id_sum += int(room.sector_id)

print "Sum of sector ids : ", sector_id_sum

