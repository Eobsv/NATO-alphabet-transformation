student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_df)

""" Used this as a preparation exercise to craete a dict comprehension"""
# Loop through rows of a data frame
dict_nato =  {}
# for (index, row) in nato_df.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     print(row.letter)
#     print(row.code)
#     dict_nato[row.letter] = row.code
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"} / Done
nato_alphabet = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_alphabet)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs. / Done
user_input = input("What word would you like to see in NATO alphabet?")
# user_input.split()
print(user_input)
input_in_nato = [nato_alphabet[letter] for letter in user_input.upper()]
print(input_in_nato)