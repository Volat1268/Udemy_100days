class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        next_question = self.question_list[self.question_number]
        u_answer = input(f"Q.{self.question_number + 1}: {next_question.text} (True or False): ").lower()



