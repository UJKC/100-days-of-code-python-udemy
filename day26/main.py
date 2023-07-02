import pandas

nemo_alpha = []

data = pandas.read_csv("day26\\nemo_alphabet.csv")
name = input("Enter your name: ").upper()
x = data.iterrows()
data_dick = {code["letter"]: code["code"] for (letter, code) in x}
data_dick_list = [data_dick[letter] for letter in name]
print(data_dick_list)