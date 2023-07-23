from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UI_Interface:

    def __init__(self, quiz_brain_catch: QuizBrain) -> None:
        self.quiz = quiz_brain_catch
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.Score_label = Label(text=f"Score: 0", font=("Arial", 20, "bold"), fg="white", bg=THEME_COLOR)
        self.Score_label.grid(row=0, column=1)

        self.canvas= Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueimage = PhotoImage(file="day34\\images\\true.png")
        self.true_button = Button(image=trueimage ,highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        falseimage = PhotoImage(file="day34\\images\\false.png")
        self.false_button = Button(image=falseimage, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.Score_label.config(text=f"Score: {self.quiz.score}")

    def true_pressed(self):
        self.quiz.check_answer("True")
        self.next_question()

    def false_pressed(self):
        self.quiz.check_answer("False")
        self.next_question()