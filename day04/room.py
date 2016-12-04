class Room:

    def __init__(self, line):
        parts = line.split("-")
        checksum_sector_id = str(parts[-1])
        self.checksum = checksum_sector_id.split("[")[1].split("]")[0]
        self.sector_id = checksum_sector_id.replace("[" + self.checksum + "]", "").strip()
        part_to_remove = "-" + checksum_sector_id
        self.encrypted_name = line.replace(part_to_remove, "")

    def __str__(self):
        return "Name:" + self.encrypted_name + "\tSector ID:" + self.sector_id + "\tChecksum:" + self.checksum

    def is_valid(self):
        letters = self.encrypted_name.replace("-", "")
        letters_and_count = {}
        for character in letters:
            if character in letters_and_count:
                letters_and_count[character] += 1
            else:
                letters_and_count[character] = 1

        for character in self.checksum:
            most_common_letter = max(letters_and_count.iterkeys(), key=(lambda key: letters_and_count[key]))
            if character not in letters_and_count.keys():
                return False
            elif character == most_common_letter:
                del letters_and_count[character]
                continue
            elif letters_and_count[character] == letters_and_count[most_common_letter]:  # if same value its fine
                del letters_and_count[character]
                continue
            else:
                return False

        return True

