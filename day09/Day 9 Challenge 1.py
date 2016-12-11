example1 = "ADVENT"
example2 = "A(1x5)BC"
example3 = "(3x3)XYZ"
example4 = "A(2x2)BCD(2x2)EFG"
example5 = "(6x1)(1x3)A"
example6 = "X(8x2)(3x3)ABCY"

data = open("input.txt").read()
# data = example6
finished_string = ""

while len(data) is not 0:
    for character in data:
        if character == "(":
            index_of_closing_bracket = data.index(")")
            rules = data[:-(len(data) - index_of_closing_bracket - 1)]  # extract rules (y * z)
            how_many_characters = int(rules.split("x")[0].replace("(", ""))
            number_of_times = int(rules.split("x")[1].replace(")", ""))
            test = data.index(rules[-1]) + 1
            act_on = data[test:test+how_many_characters]
            for x in range(number_of_times):
                finished_string += act_on

            data = data.replace(rules, "", 1).replace(act_on, "", 1)  # we've read the rules and what they do, don't repeat
            print rules, how_many_characters, number_of_times, act_on
        else:
            finished_string += character
            data = data.replace(character, "", 1)
        break

print "Old String:", data
print "New String:", finished_string, "\nLength:", len(finished_string)
