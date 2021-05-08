import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# result = {letter_key: letter_word for (letter_key, letter_word) in nato.items() if letter_key in user_name_letters}
#
# print(result)

def generate_phonetic():
    user_name = input("Enter your name: ")
    user_name_letters = [letter.upper() for letter in user_name]
    # print(user_name_letters)
    try:
        output = [nato[letter.upper()] for letter in user_name_letters]
        # print(result_2)
    except KeyError:
        print("Sorry, only letters in alphabet only")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()