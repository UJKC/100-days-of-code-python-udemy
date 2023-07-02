PLACEHOLDER = "[name]"
with open("day24\day 24\Input\Letters\starting_letter.txt") as letter:
    initial_letter = letter.read()
with open("day24\\day 24\\Input\\Names\\invited_names.txt") as data:
    initial_names = data.readlines()
for name in initial_names:
    stripped_names = name.strip()
    new_letter = initial_letter.replace(PLACEHOLDER, stripped_names)
    with open(f"day24\day 24\Output\Ready_to_send\{stripped_names}.txt", mode="w") as complete_letter:
        complete_letter.write(new_letter)