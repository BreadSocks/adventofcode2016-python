import hashlib, string

example = "abc"
input = "ffykfhsq"

index = 0
mapped_letters = {}


def deal_with_hash(md5_hash):
    position = md5_hash[5]  # 6th character
    character = md5_hash[6]  # 7th character
    if not position.isdigit():
        print "ignoring character", character, "at position", position
        return
    else:
        position = int(position)  # safely make it a number

    if position in mapped_letters.keys() or position > 7:
        print "ignoring character", character, "at position", position
    else:
        mapped_letters[position] = character
        print "adding character", character, "at position", position

while len(mapped_letters) is not 8:
    temp = input + str(index)
    md5_hash = hashlib.md5(temp).hexdigest()
    if md5_hash.startswith("00000"):
        deal_with_hash(md5_hash)
    index += 1

answer = ""
for key, value in mapped_letters.iteritems():
    answer += value
print "Answer:", answer
