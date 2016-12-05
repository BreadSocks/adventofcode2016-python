import hashlib

example = "abc"
input = "ffykfhsq"

answer = ""
index = 0

while len(answer) is not 8:
    temp = input + str(index)
    md5_hash = hashlib.md5(temp).hexdigest()
    if md5_hash.startswith("00000"):
        character = md5_hash[5]  # 6th character
        answer += character
        print "adding character", character
    index += 1

print answer
