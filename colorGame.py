import tkinter
import random

colors=['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown','silver']  #List of possible colors
score=0

timeleft=60    #Intialize the time left to 60 sec

def startGame(event):  #To start the game
    if timeleft==60:
        countdown()      #To start the count down
    nextColor()          # To choose the next color

def nextColor():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()    # To make text box active
        if e.get().lower()==colors[1].lower():  # To check whether the color typed is equal to color of the text
            score+=1
        e.delete(0,tkinter.END)    #To clear the text entry box
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text="Score: "+str(score))  # To update the score

def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timeLabel.config(text="Time left: "+str(timeleft))
        timeLabel.after(1000,countdown)

# Create GUI Window:-
root=tkinter.Tk()
root.title("COLORGAME")   # Title of the Window
root.geometry("475x300")  # Size of the Window
instructions=tkinter.Label(root,text="Type the color of the words, and not the word text.",font=('Halvetica',12))  # Adding instruction label
instructions.pack()
instructions=tkinter.Label(root,text="So,Let's Play!!!!!!!!!!!!!!!!!",font=('Halvetica',12))                       # Adding instruction label
instructions.pack()
scoreLabel=tkinter.Label(root,text="Press Enter to start",font=('Halvetica',12))                                        # Adding score label
scoreLabel.pack()
timeLabel=tkinter.Label(root,text="Time left: "+str(timeleft),font=('Halvetica',17))                                    # Adding score time left label
timeLabel.pack()
label=tkinter.Label(root,font=('Halvetica',65))                                                                         # Adding a label for displaying the colors
label.pack()
e=tkinter.Entry(root)                                                                                                   # Adding text Entry box
root.bind('<Return>',startGame)                      # To run the startGame function
e.pack()
e.focus_set()                                        # To set focus on Entry box
root.mainloop()                                      # To start the GUI Window

    
