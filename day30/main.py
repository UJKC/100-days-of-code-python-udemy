# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("day30\\nato_phonetic_alphabet.csv")

def solve():
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    
    except KeyError:
        print("Ask for letters not numbers")
        solve()
    
solve()