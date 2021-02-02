# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# starting-letters = /Users/rishuroy/Desktop/Python/mail-merge-project-start/Input/Letters/starting_letter.txt
# invited_names.txt -> /Users/rishuroy/Desktop/Python/mail-merge-project-start/Input/Names/invited_names.txt
# ready-to-send -> /Users/rishuroy/Desktop/Python/mail-merge-project-start/Output/ReadyToSend

all_names = []
with open("/Users/rishuroy/Desktop/Python/mail-merge-project-start/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("/Users/rishuroy/Desktop/Python/mail-merge-project-start/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in names:
    new_name = name.replace("\n", '')
    all_names.append(new_name.rstrip())

# print(all_names)

for item in all_names:
    new_letter = letter.replace("[name]", item)
    with open(f"/Users/rishuroy/Desktop/Python/mail-merge-project-start/Output/ReadyToSend/{item.lower()}_letter.txt", mode="w") as file:
        file.write(new_letter)








