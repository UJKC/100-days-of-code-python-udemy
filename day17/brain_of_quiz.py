class Quiz_Brain:
    def __init__(self, q_list):
        self.questionnumber = 0
        self.questionlist = q_list
        self.score = 0
    def stillhasquestions(self):
        return self.questionnumber < len(self.questionlist)
            
    def next_question1(self):
        currentquestion = self.questionlist[self.questionnumber]
        self.questionnumber += 1
        useranswer = input(f"Q.{self.questionnumber}: {currentquestion.question} (true/false): ")
        self.checkanswer(useranswer, currentquestion.answer)
    def checkanswer(self, useranswer, correctanswer):
        if useranswer.lower() == correctanswer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("Wrong")
        print(f"The correct answer is: {correctanswer}")
        print(f"The score is: {self.score}/{self.questionnumber}")