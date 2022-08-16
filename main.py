# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")


# for (index, row) in nato_alphabet.iterrows():

def generate_word():
    nato_alphabet_dic = {row.letter: row.code for (index , row) in nato_alphabet.iterrows()}
    # print(nato_alphabet_dic)
    user_input = input("Enter a word: ").upper()
    try:
        new_user_input_list = [char for char in user_input]
        new_alphabet = [nato_alphabet_dic[val] for val in new_user_input_list]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_word()
    else:
        print(new_alphabet)


generate_word()

# Dict comprehension

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# import pandas
# student_score = {
#     'student': ['Alex', 'Becky', 'Gina'],
#     'score': [40,56,50],
# }
# student_data_Frame = pandas.DataFrame(student_score)
# # print(student_data_Frame)
#
# for (index, row) in student_data_Frame.iterrows():
#     # print(index)
#     # print(row)
#     print(row.student)
#     print(row.score)

# dictionary comprehension
# student_score = {student:random.randint(1,100) for student in names}
# print(student_score)
# {'Alex': 23, 'Beth': 99, 'Caroline': 88, 'Dave': 19}
# passed_students = {key:value for (key, value) in student_score.items() if value > 60}
# print(passed_students)
