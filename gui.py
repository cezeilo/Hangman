from tkinter import *
from tkinter import Canvas
import string
import tkinter.messagebox
from code import *

# ~ Choose a topic ~ #
Topic_Of_The_Game = ""

start = Tk()

topic_label = Label(start, text="Choose your topic!")
topic_label.pack()

button_frame = Frame(start)
button_frame.pack(side="left")

topic_counter = 1


def select_word(buttontext):
    global Topic_Of_The_Game
    Topic_Of_The_Game = buttontext
    start.destroy()



with open("Topics")as f:
    for line in f:
        choice = Button(button_frame, text=line,
                  command=lambda text=line: select_word(text))
        choice.grid(row=0, column=topic_counter, padx=5)
        topic_counter = topic_counter + 1



start.wm_maxsize(width=500, height=300)
start.wm_minsize(width=500, height=300)

start.mainloop()
# ~ Start the main game ~ #

root = Tk()
test = TheCode(Topic_Of_The_Game)
canvas = Canvas(root)
topic = Label(root, text="Your Topic is: " + Topic_Of_The_Game)
topic.pack()

# ~ The Answer to the Topic ~ #
label = Label(root, text=test.encrypt_word(), font="Verdana 20")
label.pack(side="bottom")

# ~ Creating the Pole structure ~ #
pole_base = canvas.create_line(0, 250, 100, 250, width=5)
pole = canvas.create_line(50, 250, 50, 40, width=5)
pole_horiz = canvas.create_line(50, 40, 150, 40, width=5)
pole_down = canvas.create_line(125, 40, 125, 100, width=5)
pole_diag = canvas.create_line(50, 100, 100, 40, width=5)


# ~ Creating the Man figure ~ #
man_head = canvas.create_oval(150, 150, 100, 100, fill="black", state=HIDDEN)
man_body = canvas.create_line(125, 150, 125, 200, width=4, state=HIDDEN)
man_right_arm = canvas.create_line(125, 150, 160, 180, width=4, state=HIDDEN)
man_left_arm = canvas.create_line(125, 150, 90, 180, width=4, state=HIDDEN)
man_right_leg = canvas.create_line(125, 200, 160, 240, width=4, state=HIDDEN)
man_left_leg = canvas.create_line(125, 200, 90, 240, width=4, state=HIDDEN)

# ~ Creating the Words to choose from ~  + ~ Disappear Button ~ + Win Check and Draw ~ #
frame = Frame(root)
alphabet = list(string.ascii_uppercase)
counter = 0
row = 0
letters = []


def draw(component):
    if component == 0:
        canvas.itemconfig(man_head, state=NORMAL)
    elif component == 1:
        canvas.itemconfig(man_body, state=NORMAL)
    elif component == 2:
        canvas.itemconfig(man_left_arm, state=NORMAL)
    elif component == 3:
        canvas.itemconfig(man_right_arm, state=NORMAL)
    elif component == 4:
        canvas.itemconfig(man_left_leg, state=NORMAL)
    elif component == 5:
        canvas.itemconfig(man_right_leg, state=NORMAL)




def disappearAndCheck(index, letter):
    letters[index].config(state='disabled')
    draw(test.word_check(letter))
    label.config(text=" ".join(test.letters_found))
    loss_check()
    win_check()

while(counter < len(alphabet)):

    char = Button(frame, text=str(alphabet[counter]), relief=FLAT, state='normal',
                  command=lambda index=counter, n=str(alphabet[counter]): disappearAndCheck(index, n))


    if(counter >= len(alphabet)/2):
        char.grid(row=1, column=row)
        row = row + 1

    else:
        char.grid(row=0, column=counter)
    counter = counter +1
    letters.append(char)

# ~Check if the player won ~#
def win_check():
    if test.mystery_word == "".join(test.letters_found):
        tkinter.messagebox.showinfo('Hangman', 'You Won!')
        root.destroy()

def loss_check():
    if test.component_counter == 5:
        tkinter.messagebox.showinfo('Hangman', 'You lose!' + ' The word was: ' + test.mystery_word)
        root.destroy()


frame.pack(side="right")
canvas.pack(side="left")



root.wm_maxsize(width=500, height=300)
root.wm_minsize(width=500, height=300)
root.mainloop()

