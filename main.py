with open("./input/names/invited_names.txt") as names:
    # name_list = names.read().splitlines()
    name_list = names.readlines()

with open("./input/letters/starting_letter.txt") as letter:
    letter_content = letter.read()

for name in name_list:
    stripped_name = name.strip()
    letter_name = letter_content.replace("[name]", stripped_name)
    new_file = "./output/readytosend/letter_for_" + stripped_name + ".txt"
    with open(new_file, 'w') as file:
        file.write(letter_name)
