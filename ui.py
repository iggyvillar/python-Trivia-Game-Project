from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#8b2aa3"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain

        self.window = Tk()
        self.window.title("Iggy's Random Trivia Game")
        self.window.config(pady=20, padx=20, bg = THEME_COLOR)

        self.header_text = Label(text="Iggy's Trivia Game", bg= THEME_COLOR, fg= "white", font=("Arial", 15, "bold"))
        self.header_text.grid(row=0, column=0)

        self.score_label = Label(text = "Score : 0 ",fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question_text= self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question Text",
            fill = THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button= Button(image=true_img, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command = self.false_button_pressed)
        self.false_button.grid(column=1, row=2)

        question_mark = PhotoImage(file="images/Black_question_mark.png")
        self.question_mark = Canvas(width=500, height=500, bg=THEME_COLOR, highlightthickness=0)
        self.question_mark.create_image(250, 255, image = question_mark)
        self.question_mark.grid(column=0, row=3, columnspan=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text =q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


