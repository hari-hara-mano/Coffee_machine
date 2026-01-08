from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, background= THEME_COLOR)

        self.canvas = Canvas(width= 300, height= 250, bg= "white")
        self.question_text = self.canvas.create_text(150, 125, text="test",width= 280, font= FONT, fill= THEME_COLOR)
        self.canvas.grid(row= 1, column= 0, columnspan= 3, pady= 20)

        self.score_label = Label(text= "Score :",
                                  font= ("Arial", 14, "bold"),
                                    foreground= "white",
                                      background= THEME_COLOR
                                      )
        self.score_label.grid(row= 0, column= 1, columnspan= 2)

        check_image = PhotoImage(file= "images/true.png")
        self.check_button = Button(image= check_image, highlightthickness= 0, command= self.correct)
        self.check_button.grid(row= 2, column= 1)

        cross_image = PhotoImage(file= "images/false.png")
        self.cross_button = Button(image= cross_image, highlightthickness= 0, command= self.wrong)
        self.cross_button.grid(row= 2, column= 2)

        self.get_next_ques()


        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg= "white")
        self.score_label.config(text= f"Score :{self.quiz.score}")
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= self.question)
        
        else:
            self.canvas.itemconfig(self.question_text, text= "End oF session")
            self.check_button.config(state= "disabled")
            self.cross_button.config(state= "disabled")

    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")
    
        self.window.after(1000, self.get_next_ques)