import pandas

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split(" ")
print(sentence_list)
sentence_list_dict = {sentences: len(sentences) for sentences in sentence_list}
print(sentence_list_dict)