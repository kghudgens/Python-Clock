import time
from tkinter import *
import threading

# Create time variable


ct = time.strftime("%I-%M-%p")

# create tkinter window
root = Tk()
root.title("Pythons Clock")

# Declare Variables


# Create the Frames needed to lay around screen
currentTimeFrame= LabelFrame(root, padx=50, pady=50, bd=0)

timerFrame = LabelFrame(root, padx=50, pady=50, bd=0)

# Create logic for refreshing the clock
def refresh():
    currentTime.destroy()
    newTimeFrame = Label(
    currentTimeFrame, 
    text=ct, 
    font=("Arial", 20, 'bold')
    )
    newTimeFrame.pack()
    
#Create logic for timer
def cd(timer_label_obj,ts):

    while ts > 0:
        timer_label_obj.config(text=ts)
        ts-=1
        timer_label_obj.pack()
        time.sleep(1)
        if ts ==0:
            timer_label_obj.destroy()
            completeTimer = Label(timerFrame, text="Time is complete")
            completeTimer.pack()

def countdown(t):
    timer = Label(timerFrame)
    ts = int(t)
    th = threading.Thread(target=cd,args=[timer,ts])
    th.start()



# Create widget to display current time
currentTimeText= Label(
    currentTimeFrame, 
    text="Current Time", 
    font=("Arial", 20, 'bold')
    )
currentTime= Label(
    currentTimeFrame, 
    text=ct, 
    font=("Arial", 20, 'bold')
    )
refreshTime = Button(
    currentTimeFrame, 
    text="Refresh Time", 
    padx=5, 
    pady=5, 
    command=refresh,
    )
    

# Create widget for countdown timer
timerFrameText = Label(
    timerFrame, 
    text="Enter time in seconds for countdown",
    font=("Arial", 20, "bold")
)
countdownBox= Entry(timerFrame, bd=3)

submitCountdown = Button(
    timerFrame, 
    padx=5, 
    pady=5, 
    text="Submit", 
    font=("Arial", 20),
    command= lambda:countdown(countdownBox.get())
    )

# Place Frames inside root
currentTimeFrame.grid(row=1, column=1)

timerFrame.grid(row=1, column=2)

# Place widgets in Current Time Frame 
currentTimeText.pack()
currentTime.pack()
refreshTime.pack(side="bottom")

# Place widgets in timerFrame 
timerFrameText.pack()
countdownBox.pack()
submitCountdown.pack()

# Close tkinter window
root.mainloop()
