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

planner = tkinter.Tk()
planner.configure(background='white')
planner.title('toDoodles')


toDoodles = Label(planner, text="⁽˙̄˟˙̄⁾ toDoodles ⁽˙̄˟˙̄⁾", relief=RAISED,padx = 10, pady =10, bg = "pink", font=("Helvetica", 25))
toDoodles.grid(row=0, columnspan=3, pady = 15)

options = LabelFrame(planner,
                     text="yer options",
                     padx=10,
                     pady=10,
                     bg="light blue")
options.grid(row = 1, column = 4, padx=15, pady=10)

#plant pic
plant = LabelFrame(planner,
                     text="yer plant",
                     padx=10,
                     pady=10,
                     bg="light green")
plant.grid(row = 1, column=0, padx=10, pady=0)
# plant_img = ImageTk.PhotoImage(Image.open('resized-image-Promo.jpeg'))
# plant_pic = Label(plant, image=plant_img)
# plant_pic.grid(row=0, column=0)
image = Image.open('resized.jpeg')
image = image.resize((100, 100))
my_img = ImageTk.PhotoImage(image)
my_pic = Label(plant, image = my_img)
my_pic.grid(row=0, column=0)

upcoming = Label(planner, 
          text="Upcoming Assignments", 
          relief=RAISED,padx = 50, pady =50, 
          bg = "#E8D38B")
upcoming.grid(row=3, column = 4, padx = 10)

#CLOCKS! TIME! AHHHHHHH!!!!
def clock():
  os.environ['TZ'] = 'EST+8PDT,M4.1.0,M10.5.0'
  time.tzset()
  hour = time.strftime("%I")
  minute = time.strftime("%M")
  second = time.strftime("%S")
  day = time.strftime("%A")

  testClock.config(text = "*•̩̩͙✩•̩̩͙*˚howdy!˚*•̩̩͙✩•̩̩͙*˚ \n" + "happy " + day + "\n " + hour + ":" + minute + ":" + second + "")
  testClock.after(1000, clock)

testClock = Label(planner, 
          text = "screaming internally", 
          font=("Helvetica", 25, "italic"), 
          fg="white", 
          bg="#EBA2A2", 
          padx=10)
testClock.grid(row =3, column = 0, padx=10, pady=20)
clock()


#add assignment stuffs
def addassignmentwindow():
  addassign = Toplevel()
  addassign.title('add assignment')
  add_button = Button(addassign, text='add assignment', command=addassign.destroy, bg='light pink')
  add_button.grid(row = 5, column = 2 ,padx=10, pady=10)

  title = Label(addassign, 
          text = "title:", 
          bg= "#B6DFD8").grid(row=1, column = 0, pady = 10, padx =10, sticky = 'E')
  title_input = Entry(addassign).grid(row = 1, column = 2, sticky ='W', padx=10)

  due_date = Label(addassign,
           text = "due date:", 
           bg= "#B6C2DF").grid(row=2, column = 0, pady = 10, padx =10, sticky = 'E')
  due_date_input = Entry(addassign).grid(row = 2, column = 2, sticky ='W', padx=10)
  subject = Label(addassign, 
          text = "subject:",
           bg= "#D2B6DF").grid(row=3, column = 0, pady = 10, padx =10, sticky = 'E')
  subject_input = Entry(addassign).grid(row = 3, column = 2, sticky ='W', padx=10)
  type_of_work = Label(addassign, 
          text = "type of work:", 
          bg= "#DFB6B6").grid(row=4, column = 0, pady = 10, padx =10, sticky = 'E')
  type_input = Entry(addassign).grid(row = 4, column = 2, sticky ='W', padx=10)

add = Button(options, text="Add Assignment!", command=addassignmentwindow)
add.grid(row=0, column=0)



#view assignments stuff
def viewassignmentswindow():
  viewassign = Toplevel()
  viewassign.title('view assignments')
  #valabel = Label(viewassign, text='view assignments').grid()
  closeva = Button(viewassign, text='close window', command=viewassign.destroy, bg='light pink')
  closeva.grid(row=0,column=0,padx=10, pady=10)

  v_title = Label(viewassign, 
          text = "title", 
          bg= "#B6DFD8").grid(row=1, column = 0, pady = 10, padx =10, )

  v_due_date = Label(viewassign,
           text = "due date", 
           bg= "#B6C2DF").grid(row=1, column = 1, pady = 10, padx =10, )
  v_subject = Label(viewassign, 
          text = "subject",
           bg= "#D2B6DF").grid(row=1, column = 2, pady = 10, padx =10, )
  v_type_of_work = Label(viewassign, 
          text = "type of work", 
          bg= "#DFB6B6").grid(row=1, column = 3, pady = 10, padx =10, )

view = Button(options, text="View Assignments!", command=viewassignmentswindow)
view.grid(row=1, column=0)



#view plant stuff
def viewplantwindow():
  vplant = Toplevel()
  vplant.title('view plant')
  vplabel = Label(vplant, text='view plant').grid(row=0, column=0)

view_plant = Button(options, text='view your plant!', command=viewplantwindow)
view_plant.grid(row=2, column=0)

#complete assignment stuff aka checkboxes!
def cassignmentswindow():
  cassign = Toplevel()
  calabel = Label(cassign, text='complete assignments').grid(row=0, column=0)
  

complete_assignments = Button(options, text="Complete Assignments!", command=cassignmentswindow)
complete_assignments.grid(row=3, column=0)




planner.mainloop()
