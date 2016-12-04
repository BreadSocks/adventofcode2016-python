from room import Room

valid_rooms = []

print "\nFound rooms:"
with open("input.txt") as inputFile:
    for line in inputFile:
        room = Room(line)
        # print room
        if room.is_valid():
            valid_rooms.append(room)

for room in valid_rooms:
    # print room.decrypted_name()
    if room.decrypted_name().__contains__("northpole"):
        print room
