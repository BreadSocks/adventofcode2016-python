import re
found_addresses = []
remove_addresses = []


def invalid(string):
    # first check they aren't all the same
    if all(character == string[0] for character in string):
        print "Found part with identical letters:", string
        return False


def has_abba(string):
    for index in range(0, len(string) - 3):  # so it only tries in groups of 4
        first_char = string[index]
        second_char = string[index + 1]
        third_char = string[index + 2]
        forth_char = string[index + 3]
        if first_char == second_char and first_char == third_char and first_char == forth_char:
            return False
        if second_char == third_char and first_char == forth_char:
            return True
    return False

with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.replace("\n", "")

        brackets = re.findall("\[(.*?)\]", line)
        # print brackets

        for bracket_pair in brackets:
            if has_abba(bracket_pair):
                print "Found line with abba in brackets:", line
                remove_addresses.append(line)
                break

        without_bracket_parts = []
        against_line = line
        for bracket in brackets:
            sides = against_line.split("[" + bracket + "]")
            if "[" in sides[0]:
                against_line = sides[0]  # save the new line to work against
            else:
                without_bracket_parts.append(sides[0])
            if "]" in sides[1]:
                against_line = sides[1]
            else:
                without_bracket_parts.append(sides[1])  # save the new line to work against

        for part in without_bracket_parts:
            if invalid(part):
                remove_addresses.append(line)
                break
            elif has_abba(part) and "[" + part + "]" not in line:
                found_addresses.append(line)

print "Done"
for removal in remove_addresses:
    if removal in found_addresses:
        found_addresses.remove(removal)

print len(found_addresses)
unique = []
for address in found_addresses:
    if address not in unique:
        unique.append(address)
    print address

print len(unique)
