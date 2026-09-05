
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
main=None
marks=None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetting():
       
       window.after_cancel(main)
       canvas.itemconfig(timer_text,text='00:00')
       global reps
       reps=0
       global marks
       marks=''
       timer_label.config(text='TIMER')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timermechanism():
       global reps
       reps=reps+1
       if reps%8==0:
              timer(LONG_BREAK_MIN*60)
              timer_label.config(text='LONG_BREAK_MIN')

       elif reps%2==0:
              timer(SHORT_BREAK_MIN*60)
              timer_label.config(text='SHORT_BREAK_MIN')
       else :
              timer(WORK_MIN*60)
              timer_label.config(text='WORK TIME')
        
        
       
        
       
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
'''in general we use to import time module and use time.sleep but in tkinter 
there is a built in mechanism called after function that acts more simple as time.sleep
here after takes millisecond argument'''
def timer(n):
    n=n
    
    
    min=math.floor(n/60)
    sec=n%60
    if sec<10:
           sec=f'0{sec}'
    canvas.itemconfig(timer_text,text=f'0{min}:{sec}')
    if n>0:
                global main
                main=window.after(1000,timer,n-1)
    else:
           timermechanism()
           marks=''
           for _ in range(math.floor(reps/2)):
                  
                  marks+='✔'
                  checkmark.config(text=marks)
                  
    
    
'''def times():
    timer(5*60)'''


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('POMODORO')
window.config(padx=100,pady=100,bg=YELLOW)
canvas=Canvas(width=200,height=200,bg=YELLOW,highlightthickness=0)## padding canvas fails remember

pic=PhotoImage(file='tomato.png')
canvas.create_image(100,100,image=pic)
timer_text=canvas.create_text(100,100,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)
timer_label=Label(text='TIMER',font=(FONT_NAME,60,'bold'),fg=GREEN,bg=YELLOW,highlightthickness=0)
timer_label.grid(column=1,row=0)
startlabel=Button(text='start',padx=5,pady=5,highlightthickness=0,command=timermechanism)
startlabel.grid(column=0,row=2)
resetlabel=Button(text='reset',padx=5,pady=5,highlightthickness=0,command=resetting)
resetlabel.grid(column=3,row=2)
checkmark=Button(fg=GREEN,padx=10,pady=10,highlightthickness=0,bg=YELLOW)
checkmark.grid(column=1,row=3)

window.mainloop()