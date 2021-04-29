import os
import sys
import time
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkscrolledframe import ScrolledFrame

window = tkinter.Tk()
window.state('normal')
window.title('ToDoodles')

# window.wm_iconbitmap(os.path.join(sys.path[0], "plant.ico"))

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

homepage = tk.Frame(window)
view_plant = tk.Frame(window)
add_assignments = tk.Frame(window)
view_assignments = tk.Frame(window)
comp_assigments = tk.Frame(window)

for frame in (homepage, view_plant, add_assignments, view_assignments,
              comp_assigments):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")

    testClock.config(text="Happy " + day + " " + hour + ":" + minute + ":" +
                     second + "")
    testClock.after(1000, clock)


testClock = Label(window,
                  text="",
                  font=("Georgia", 15, "bold italic"),
                  fg="black")
testClock.grid(sticky='E')


def addassignments():
    addassign = Toplevel()
    addassign.title('Add Assignment!')
    # addassign.wm_iconbitmap(os.path.join(sys.path[0], "plant.ico"))
    add_button = Button(addassign,
                        text='Add Assignment!',
                        command=addassign.destroy,
                        bg='light pink',
                        font=("Georgia", "15", "bold italic "))
    add_button.grid(row=5, column=2, padx=10, pady=10)

    Label(addassign,
          text="Title:",
          bg="#B6DFD8",
          font=("Georgia", "15", "bold italic underline")).grid(row=1,
                                                                column=0,
                                                                pady=10,
                                                                padx=10,
                                                                sticky='E')
    title = Entry(addassign).grid(row=1, column=2, sticky='W', padx=20)
    Label(addassign,
          text="Due Date:",
          bg="#B6C2DF",
          font=("Georgia", "15", "bold italic underline")).grid(row=2,
                                                                column=0,
                                                                pady=10,
                                                                padx=10,
                                                                sticky='E')
    due_date = Entry(addassign).grid(row=2, column=2, sticky='W', padx=20)
    Label(addassign,
          text="Subject:",
          bg="#D2B6DF",
          font=("Georgia", "15", "bold italic underline")).grid(row=3,
                                                                column=0,
                                                                pady=10,
                                                                padx=10,
                                                                sticky='E')
    subject = Entry(addassign).grid(row=3, column=2, sticky='W', padx=20)
    Label(addassign,
          text="Type Of Work:",
          bg="#DFB6B6",
          font=("Georgia", "15", "bold italic underline")).grid(row=4,
                                                                column=0,
                                                                pady=10,
                                                                padx=10,
                                                                sticky='E')
    type_work = Entry(addassign).grid(row=4,
                                      column=2,
                                      sticky='W',
                                      padx=20,
                                      pady=20)


def viewassigments():
    frame_top = tk.Frame(view_assignments, width=400, height=250)
    frame_top.pack(side="top", expand=1, fill="both")
    sf = ScrolledFrame(frame_top, width=380, height=240)
    sf.pack(side="right", expand=1, fill="both")
    sf.bind_arrow_keys(frame_top)
    sf.bind_scroll_wheel(frame_top)
    frame = sf.display_widget(tk.Frame)
    l = tk.Label(frame, text="",
                 font=("Georgia", "15", "bold underline")).pack()


#==================Homepage Frame
photo = PhotoImage(file=os.path.join(sys.path[0], "planthomescreen.gif"))
photoimage = photo.subsample(2, 2)

tk.Label(homepage,
         text='ToDoddles!',
         font=("Georgia", "30", "bold italic underline")).pack(fill='both',
                                                               expand=True)
tk.Label(
    homepage,
    image=photoimage,
).pack(side='top', expand=True)

tk.Button(homepage,
          bg='light green',
          text='VIEW PLANT!',
          font=("Georgia", "12", "bold italic underline"),
          command=lambda: show_frame(view_plant)).pack(fill='x', ipady=25)
tk.Button(homepage,
          bg='orange',
          text='ADD ASSIGNMENTS',
          font=("Georgia", "12", "bold italic underline"),
          command=lambda: show_frame(add_assignments)).pack(fill='x', ipady=25)
tk.Button(homepage,
          bg='light blue',
          text='VIEW ASSIGNMENTS!',
          font=("Georgia", "12", "bold italic underline"),
          command=lambda: show_frame(view_assignments)).pack(fill='x',
                                                             ipady=25)
tk.Button(homepage,
          bg='light yellow',
          text='COMPLETED ASSIGNMENTS',
          font=("Georgia", "12", "bold italic underline"),
          command=lambda: show_frame(comp_assigments)).pack(fill='x', ipady=25)
#==================View Plant Frame
tk.Label(view_plant,
         text='View Plant',
         font=("Georgia", "30", "bold italic underline"),
         bg='floral white').pack(fill='both', expand=True)
tk.Button(view_plant,
          text='Back To Homepage',
          command=lambda: show_frame(homepage),
          bg='firebrick2',
          font=("Georgia", "15", "bold italic")).pack(fill='x', ipady=10)
#==================Add Assignments Frame
tk.Button(add_assignments,
          text='Add Assignments! (Click Me!)',
          font=("Georgia", "30", "bold italic underline"),
          command=addassignments,
          bg='pink').pack(fill='both', expand=True)
tk.Button(add_assignments,
          text='Back To Homepage',
          command=lambda: show_frame(homepage),
          bg='firebrick2',
          font=("Georgia", "15", "bold italic")).pack(fill='x', ipady=10)
#==================View Assignments Frame
tk.Label(view_assignments,
         text='View Assignments!',
         font=("Georgia", "30", "bold italic underline"),
         bg='light blue').pack(fill='both', ipady=15)
viewassigments()
tk.Button(view_assignments,
          text='Back To Homepage',
          command=lambda: show_frame(homepage),
          bg='firebrick2',
          font=("Georgia", "15", "bold italic")).pack(side='bottom',
                                                      ipady=10,
                                                      fill=BOTH)
#==================Completed Assignments Frame
tk.Label(comp_assigments,
         text='Completed Assignments!',
         font=("Georgia", "30", "bold italic underline"),
         bg='lavender').pack(fill='both', expand=True)
tk.Button(comp_assigments,
          text='Back To Homepage',
          command=lambda: show_frame(homepage),
          bg='firebrick2',
          font=("Georgia", "15", "bold italic")).pack(fill='x', ipady=10)

clock()
show_frame(homepage)
window.mainloop()
