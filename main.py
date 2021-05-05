''''
Project goal is to create a planner application in which the user can add assignments/tasks, view all assignments, set timers (maybe) for studying/productivity, and grow a plant by completing assignments.

If there is enough time, might add a game after completing assignments?? one of the one's we've already made
'''
import tkinter
import time
from tkinter import *
from PIL import ImageTk, Image
# import TkMessageBox
from tkinter import messagebox
import os
import sys

planner = tkinter.Tk()
planner.configure(background='white')
planner.title('toDoodles')

def aa_buttonClicked():
    file = open("assignments.txt", 'a')
    dict_keys = [title_var.get(), due_date_var.get(), subject_var.get(), type_var.get()]
    file.write(dict_keys[0]+"\t"+dict_keys[1]+"\t"+dict_keys[2]+"\t"+dict_keys[3]+"\n")
    file.close()
    add_assignment.destroy()

toDoodles = Label(planner,
                  text="⁽˙̄˟˙̄⁾ toDoodles ⁽˙̄˟˙̄⁾",
                  relief=RAISED,
                  padx=10,
                  pady=10,
                  bg="#C0B9E2",
                  font=("Helvetica", 25),
                  fg="white")
toDoodles.grid(row=0, column=0, columnspan=3, pady=15)

options = LabelFrame(planner,
                     text="yer options",
                     padx=10,
                     pady=10,
                     bg="light blue")
options.grid(row=1, column=4, padx=15, pady=10)

#plant pic
plant = LabelFrame(planner,
                   text="yer plant",
                   padx=10,
                   pady=10,
                   bg="light green")
plant.grid(row=1, column=0, padx=10, pady=0)
image = Image.open('resized.jpeg')
image = image.resize((200, 200))
my_img = ImageTk.PhotoImage(image)
my_pic = Label(plant, image=my_img)
my_pic.grid(row=0, column=0)

upcoming = LabelFrame(planner,
                 text="Take a break!",
                 #relief=RAISED,
                 padx=10,
                 pady=10,
                 bg="#FFFA90")
upcoming.grid(row=3, column=4, padx=15, pady=10)


#CLOCKS! TIME! AHHHHHHH!!!!
def clock():
    os.environ['TZ'] = 'EST+8PDT,M4.1.0,M10.5.0'
    time.tzset()
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")

    testClock.config(text="*•̩̩͙✩•̩̩͙*˚howdy!˚*•̩̩͙✩•̩̩͙*˚ \n" + "happy " +
                     day + "\n " + hour + ":" + minute + ":" + second + "")
    testClock.after(1000, clock)


testClock = Label(planner,
                  text="screaming internally",
                  font=("Helvetica", 25, "italic"),
                  fg="white",
                  bg="#EBA2A2",
                  padx=10)
testClock.grid(row=3, column=0, padx=10, pady=20)
clock()


#add assignment stuffs
def addassignmentwindow():
    global title_var
    global due_date_var
    global subject_var
    global type_var

    title_var = StringVar()
    due_date_var = StringVar()
    subject_var = StringVar()
    type_var = StringVar()
    global add_assignment
    add_assignment = Toplevel()
    add_assignment.title("add assignment")

    title_label = Label(add_assignment, text="title", bg="#B6DFD8")
    title_entry = Entry(add_assignment, textvariable=title_var)

    due_date_label = Label(add_assignment, text="due date:", bg="#B6C2DF")
    due_date_entry = Entry(add_assignment, textvariable=due_date_var)

    subject_label = Label(add_assignment, text="subject", bg="#D2B6DF")
    subject_entry = Entry(add_assignment, textvariable=subject_var)

    type_label = Label(add_assignment, text="type of work", bg="#DFB6B6")
    type_entry = Entry(add_assignment, textvariable=type_var)

    add_button = Button(add_assignment, text='add assignment', command=aa_buttonClicked, bg='light pink')

    title_label.grid(row=1, column=0, pady=10, padx=10, sticky='E')
    title_entry.grid(row=1, column=2, sticky='W', padx=10)

    subject_label.grid(row=3, column=0, pady=10, padx=10, sticky='E')
    subject_entry.grid(row=3, column=2, sticky='W', padx=10)

    due_date_label.grid(row=2, column=0, pady=10, padx=10, sticky='E')
    due_date_entry.grid(row=2, column=2, sticky='W', padx=10)

    type_label.grid(row=4, column=0, pady=10, padx=10, sticky='E')
    type_entry.grid(row=4, column=2, sticky='W', padx=10)

    add_button.grid(row=5, column=2, padx=10, pady=10)

add = Button(options, text="Add Assignment!", bg='#E4F7FF', command=addassignmentwindow)
add.grid(row=0, column=0)

#view assignments stuff
def viewassignmentswindow():
    viewassign = Toplevel()
    viewassign.title('view assignments')
    #valabel = Label(viewassign, text='view assignments').grid()
    closeva = Button(viewassign,
                     text='close window', 
                     command=viewassign.destroy,
                     bg='light pink')
    closeva.grid(row=0, column=0, padx=10, pady=10)

    v_title = Label(viewassign, text="title", bg="#B6DFD8").grid(
        row=1,
        column=0,
        pady=10,
        padx=10,
    )

    v_due_date = Label(viewassign, text="due date", bg="#B6C2DF").grid(
        row=1,
        column=1,
        pady=10,
        padx=10,
    )
    v_subject = Label(viewassign, text="subject", bg="#D2B6DF").grid(
        row=1,
        column=2,
        pady=10,
        padx=10,
    )
    v_type_of_work = Label(viewassign, text="type of work", bg="#DFB6B6").grid(
        row=1,
        column=3,
        pady=10,
        padx=10,
    )

    file = open("assignments.txt", 'r')
    contents = file.read().split('\n')
    for i in range(len(contents)-1):
        newcontents = contents[i].split('\t')
        print(newcontents)
        for n in range(len(newcontents)):

            t_text = Label(viewassign, text=newcontents[0]).grid(row=i+2, column=0, pady=10, padx=10)
            d_text = Label(viewassign, text=newcontents[1]).grid(row=i+2, column=1, pady=10, padx=10)
            s_text = Label(viewassign, text=newcontents[2]).grid(row=i+2, column=2, pady=10, padx=10)
            ty_text = Label(viewassign, text=newcontents[3]).grid(row=i+2, column=3, pady=10, padx=10)


view = Button(options, text="View Assignments!", bg='#E4F7FF', command=viewassignmentswindow)
view.grid(row=1, column=0)


#view plant stuff
def viewplantwindow():
    vplant = Toplevel()
    #vplant.title('view plant')
    vplabel = Label(vplant, text='view plant').grid(row=0, column=0)
    image1 = Image.open('resized.jpeg')
    image1 = image1.resize((200, 200))
    my_img1 = ImageTk.PhotoImage(image1)
    my_pic1 = Label(vplant, image=my_img1)
    my_pic1.grid(row=1, column=0)
    


view_plant = Button(options, text='View your plant!', bg='#E4F7FF', command=viewplantwindow)
view_plant.grid(row=2, column=0)


#complete assignment stuff aka checkboxes!
def cassignmentswindow():
    cassign = Toplevel()
    calabel = Label(cassign, text='complete assignments').grid(row=0, column=0)

def openSnake():
  os.system('python snake.py')

snake_game = Button(upcoming,
                              text="Snake Game", fg='white', bg='#BBEECF',
                              command=openSnake)
                              #command=cassignmentswindow)
snake_game.grid(row=0, column=0,padx=10,pady=10)

def openTetris():
  os.system('python notTetris.py')

tetris_game = Button(upcoming,
                              text="Tetris", fg='white', bg='#F5B9FF',
                              command=openTetris)
                              #command=cassignmentswindow)
tetris_game.grid(row=1, column=0,padx=10,pady=10)

def add_checkbox():
    var = IntVar()
    c = Checkbutton(viewassign, text="test", variable=var).grid(row=2,
    column=1)


planner.mainloop()
