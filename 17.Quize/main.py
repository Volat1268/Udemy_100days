from question_model import Question
from data import question_data

question_bank = []
for i_question in range(len(question_data)):
    question_bank.append(Question(question_data[i_question]["text"], question_data[i_question]["answer"]))


def plus(a, b):
    return a + b

print(plus(12, 12))