from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    start_button.config(state="normal")
    window_label.config(text= "Timer", fg= GREEN)
    canvas.itemconfig(timer_text, text= "00:00")
    tick_label.config(text="")
    reps= 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mechanism():
    global reps
    start_button.config(state="disabled")   
    reps+=1
    work_sec = WORK_MIN     * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 == 0:

        if reps % 8 == 0:
            window_label.config(text= "Long Break", fg= RED)
            countdown(long_break)

        else:
            window_label.config(text= "Break", fg= GREEN)
            countdown(short_break)
             
    else:
        window_label.config(text= "Timer", fg= GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_minute = floor(count/60)
    count_sec= count % 60   

    if count_minute < 10:
        count_minute = f"0{count_minute}"

    if count_sec< 10 :
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer= window.after(1000, countdown, count-1)
    else:
        timer_mechanism()
        marks= ""
        work_sessions= floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"

        if work_sessions == 5:
            timer_reset()

        tick_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas=Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_png= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_png)
timer_text= canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


window_label=Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 35, "bold"))
window_label.grid(row=0, column=1)   

tick= "✔"
tick_label= Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"), highlightthickness=0)
tick_label.grid(row=3, column=1)

start_button= Button(text="Start", command= timer_mechanism, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button= Button(text="Reset", command= timer_reset, highlightthickness=0)
reset_button.grid(row=2, column=2)

















window.mainloop()