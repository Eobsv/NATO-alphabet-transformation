import pandas


nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_df)

""" Used this as a preparation exercise to craete a dict comprehension"""
#  Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
# dict_nato =  {}

# Loop through rows of a data frame
# for (index, row) in nato_df.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     print(row.letter)
#     print(row.code)
#     dict_nato[row.letter] = row.code
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_alphabet = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# print(nato_alphabet)


def generate_phonetic():
    user_input = input("What word would you like to see in NATO alphabet?").upper()
    try:
        input_in_nato = [nato_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Please keep word in English alphabet")
        generate_phonetic()
    else:
        print(input_in_nato)

generate_phonetic()
