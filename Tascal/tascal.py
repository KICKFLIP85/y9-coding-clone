# # # # # # # # # # # # # # # # # #
#  _____ _   ___  ___   _   _     #
# |_   _/_\ / __|/ __| /_\ | |    #
#   | |/ _ \\__ \ (__ / _ \| |__  #
#   |_/_/ \_\___/\___/_/ \_\____| #
# # # # # # # # # # # # # # # # # # - Jonathan Huang Y9

"""
ABOUT
Tascal is a task list and calendar prototype, created by a Y9 student at
UCC with the objective of eliminating procrastination from people's lives.
The vision of this program is to be completely accessible to the user.
This goal has only partially been reached due to time constraints,
as explained in the video description.
"""


"""
IMPORT LIBS
Importing needed libraries:
- 'Tkinter' (and associated libs) 
  - Core (widgets, functions, etc)
  - 'messagebox' (pop-up windows)
  - 'canvas' (draws 2D geometrical shapes)
- 'SQLite3' libs for database integration + storage
- 'datetime' to get date-related functions and values
Note: Code below was lengthened to specify which specific packages
were imported for easier understanding from visiting developers.
"""
import tkinter as tk # renaming tkinter as tk
from tkinter import messagebox, Canvas
import sqlite3 as sq # renaming sqlite3 as sq
from datetime import datetime, date, timedelta



"""
INIT DB
Initializes database for task list.
In summary, this uses the SQLite lib that we imported earlier
and creates a .db file in the same folder as this file.
It then uses a SQLite built-in command 'create' to create
a table in the database that stores strings ('text' option in sq)
"""
conn = sq.connect('tascal.db') # filename: tascal.db
cur = conn.cursor() # turns on cursor, which allows for read&write functionality
# SQLite command to create a table called 'tasks',
# with column title "title" (can be anything) and
# input type "text"
cur.execute('create table if not exists tasks (title text)')
cur.close() #closes cursor after use, good practice





"""
INIT ROOT WINDOW
Creates the master window of the application. Performs various commands to
set an alias for the window (root), set a title (Tascal), change the window
size (960x465), lock the window, and finally change the window's background
color.
"""
root = tk.Tk() # 'root' is now the name of the master window
root.title('Tascal') # window title: Tascal (application name)
root.geometry("960x465") # setting window size
root.resizable(width=False, height=False) # disables the ability to resize window
root.configure(background="#23272A") # setting window bkg color






"""
ROOT WINDOW VARIABLE DEFINITIONS
Here we create variables for later use. These include:
- 'task': the future list for tasks in our task list
- 'varToday': gets today's date (default format, very detailed) for use in
upcoming variable
- 'today': gets today's date (formatted, simple) for use in title
- 'month': gets the month (formatted, abbreviated) for use in task subtitle
- 'thisSunday': performs addition and subtraction to calculate the upcoming
Sunday's date (formatted, only shows number) for use in task list title
- 'lastMonday': performs subtraction on 'thisSunday' to derive the previous
Monday
"""

task = [] # setting the var 'task' as an empty list to prepare for task list

# calling multiple variables for different dates and months
varToday = datetime.today() # gets today's date, unformatted
today = datetime.today().strftime("%B %d, %Y") # gets today's date, formatted
month = datetime.today().strftime("%b") # gets today's month, abbreviated
# uses previously defined variable 'varToday' to calculate the closest upcoming
# Sunday. It takes the current day and adds the *sum* of
# the number of days till next sunday (timedelta class) and today. Keep in mind
# the sum isn't a normal mathematical sum - it is to combine to two variables
# together. Finally, the whole equation is formatted to only show the date of
# the upcoming Sunday.
thisSunday = (varToday + timedelta((6-varToday.weekday()) % 7)).strftime("%d")
# uses previously defined variable 'thisSunday'to calculate the date of the previous
# Monday. It turns 'thisSunday' into an integer, subtracts 6 from it (to get the day
# after Sunday which is Monday, then finally turns it back into a string.
lastMonday = datetime.today().strftime(str(int(thisSunday)-6))





"""
ROOT WINDOW FUNCTIONS
This section defines all functions needed for the master window. This includes:
- 'clearList()': deletes all the entries present in the Listbox but not from the
task list. All the entries which are not deleted are still present in the task list.
- 'listUpdate(): used to update the Listbox every time an entry is added to or
deleted from the task list. It first invokes the clearList() function and it
inserts all the elements present in the task list freshly into the listbox. It also
sets the color of each task based on its order.
- 'delOne()': deletes one task that is selected from the listbox. If no entry is
selected before clicking on the delete button, the application displays a message
box informing to select an entry. If an item is selected from the Listbox, then the
function first removes the item from task list, then it deletes the task from database.
- 'delAll()': deletes all the items in the Listbox as well as in task list. This
function also prompts with a confirmation message.
"""
def clearList():
  t.delete(0,'end') #removes all entries in the listbox (t) which will be defined later


def listUpdate():
  clearList() # calls prev. function, clearing all entries from listbox
  for i in task:        # this repeats and update the listbox every time an 
    t.insert('end', i)  # entry is added to or deleted from the task list

    # checks to see if the length of the first task is not 0 - if it isn't, it sets the text color (fg) to x, y or z
    # it then repeats for the next task; if there is no task (length of task = 0), the pass function stops the code
    # although this looks obnoxiously repetitive, this is the fastest way to do this without compromising the goal
    if len(t.get(0)) != 0: # if the length of the task text entry is not 0...
          t.itemconfig(0, {'fg': 'maroon'}) 
          
          if len(t.get(1)) != 0: # if the length of the task text entry is not 0...
            t.itemconfig(1, {'fg': 'red'}) # set the task's foreground color (text color) to 'some_color'
            
            if len(t.get(2)) != 0: # if the length of the task text entry is not 0...
              t.itemconfig(2, {'fg': 'tomato'}) # set the task's foreground color (text color) to 'some_color'
              
              if len(t.get(3)) != 0: # if the length of the task text entry is not 0...
                t.itemconfig(3, {'fg': 'orange'}) # set the task's foreground color (text color) to 'some_color'
                
                if len(t.get(4)) != 0: # if the length of the task text entry is not 0...
                  t.itemconfig(4, {'fg': 'yellow'}) # set the task's foreground color (text color) to 'some_color'
                  
                  if len(t.get(5)) != 0: # if the length of the task text entry is not 0...
                    t.itemconfig(5, {'fg': 'lime green'}) # set the task's foreground color (text color) to 'some_color'
                    
                    if len(t.get(6)) != 0: # if the length of the task text entry is not 0...
                      t.itemconfig(6, {'fg': 'turquoise'}) # set the task's foreground color (text color) to 'some_color'
                      
                      if len(t.get(7)) != 0: # if the length of the task text entry is not 0...
                        t.itemconfig(7, {'fg': 'RoyalBlue1'}) # set the task's foreground color (text color) to 'some_color'
                        
                        if len(t.get(8)) != 0: # if the length of the task text entry is not 0...
                          t.itemconfig(8, {'fg': 'medium blue'}) # set the task's foreground color (text color) to 'some_color'
                          
                          if len(t.get(9)) != 0: # if the length of the task text entry is not 0...
                            t.itemconfig(9, {'fg': 'blue violet'}) # set the task's foreground color (text color) to 'some_color'
                    
                          else: # if the length of the task text entry IS 0...
                            pass # do nothing
                        
                        else: # if the length of the task text entry IS 0...
                          pass # do nothing

                      else: # if the length of the task text entry IS 0...
                        pass # do nothing

                    else: # if the length of the task text entry IS 0...
                      pass # do nothing

                  else: # if the length of the task text entry IS 0...
                    pass # do nothing

                else: # if the length of the task text entry IS 0...
                  pass # do nothing
                
              else: # if the length of the task text entry IS 0...
                pass # do nothing
            
            else: # if the length of the task text entry IS 0...
              pass # do nothing
            
          else: # if the length of the task text entry IS 0...
            pass # do nothing

    else: # if the length of the task text entry IS 0...
      pass # do nothing



def delOne():
    try: # tries to do... but if for some reason it doesn't work go to 'except'
      val = t.get(t.curselection()) # sets the variable 'val' as the cursor selection in the listbox
      print('deleting:', val)
      if val in task: # asks if the cursor selection is in the task list
          cur = conn.cursor() # connects the cursor for read&write access
          task.remove(val) # removes task from list (task)
          listUpdate() # runs listUpdate() function
          cur.execute('delete from tasks where title = ?', (val,)) # runs sq command to remove the task that matches 'val'
          conn.commit() # commits all changes
          cur.close() # closes the cursor for good practice
    except: #if 'try' does not work, run...
      messagebox.showinfo('Cannot Delete', 'No task item selected, please try again!')  # show messagebox popup with error

def delAll():
  mb = messagebox.askyesno('Delete All Tasks','Are you sure you want to do this?') # shows special yes/no messagebox for confirmation
  if mb==True: # asks if user hits 'yes'
      while(len(task)!=0): # repeats until the length of the task list is 0
          cur = conn.cursor() # connects the cursor for read&write access
          task.pop() # removes the first item on the task list
          cur.execute('delete from tasks') # runs sq command to delete tasks from databse 'tasks'
          listUpdate() #runs listUpdate() function
          conn.commit() # commits all changes
          cur.close() # closes the cursor for good practice


def retrieveDB():
  cur = conn.cursor() # connects the cursor for read&write access
  while(len(task)!=0): # repeats while the length of the task is not 0 (clearing all tasks)
    task.pop() # removes the first item on the task list
  for row in cur.execute('select title from tasks'): # for every row (task) in 'title' (column header of database 'tasks')...
    cur = conn.cursor() # connects the cursor for read&write access
    task.append(row[0]) # adds each task from the database to the listbox in the application
    conn.commit() # commits all changes
    cur.close() # closes the cursor for good practice









'''
DEFINE AND PLACE ALL WIDGETS + ITEMS
Here we create all our widgets and use (most of) the functions we defined above.
We place them on our application using the .place() class for precision, and
the .pack() class for special functionality (stretch to fit).
Colors Used:
- Dark Gray ('title', 'calLabel'):
- Light Gray (all widgets/items related to task list): #666666
- White (all and ONLY text color): #ffffff
font: Open Sans
'''
# creating widgets and configurating options for LEFT SIDE
title = tk.Label(root, text = ('Tascal:' + " " + today), font = ('Open Sans', 36), bg='#23272A', fg='#ffffff') # creating application title + date ('today' var) 
calLabel = tk.Label(root, text =                                                        # roundabout way for
                    ('Mon.' + "       " + "Tue." + "       " +                          # adding labels for each
                     "Wed." + "     " +"Thurs." + "         " +                         # day of the week;
                     "Fri." + "         " + "Sat." + "         "                        # arguably faster than
                     + "Sun."), font = ('Open Sans', 20), bg='#23272A', fg='#ffffff')   # creating ind. labels
# creating widgets and configurating options for TASK LIST
bkgList = tk.Label(root, width=200, height=200, bg='#666666') # background for list
listTitle = tk.Label(root, text =("This Week's Tasks"), font = ('Open Sans', 28), bg='#666666', fg='#ffffff') # title for list
listSub = tk.Label(root, text =(month, lastMonday + "-" + thisSunday), font = ('Open Sans', 24), bg='#666666', fg='#ffffff') # subtitle for list + week range ('mon.-sun.')
# creating BUTTONS
deleteTask = tk.Button(root, text='Delete', width=10, command=delOne, highlightbackground='#666666', highlightcolor='#666666') # creating delete task button ('delOne' var)
deleteAll = tk.Button(root, text='Delete all', width=12, command=delAll, highlightbackground='#666666', highlightcolor='#666666') # creating delete all button ('delAll' var)

# placing LEFT SIDE widgets
title.place(x=20, y=16) # placing title... PADDING REFERENCE: EVERYTHING goes past 16 pixels from the sides and 20 pixels from the top
calLabel.place(x=35, y=100) # placing calendar labels
# placing TASK LIST items (not the list itself, yet)
bkgList.place(x=640, y=0) # placing list background
listTitle.place(x=675, y=16) # placing list title
listSub.place(x=725, y=50) # placing list subtitle
# placing BUTTONS
deleteTask.place(x=670, y=100) # placing delete task button
deleteAll.place(x=810, y=100) # placing delete all button

    
# CREATE LISTBOX
t = tk.Listbox(root, height=10, width=18, selectmode='SINGLE', # l&w are in characters, therefore max view vertically is 10 tasks, 18 chars length without scrolling
               bd=0, bg='#666666', fg='#ffffff', font = ('Open Sans', 24)) # no border for flat look (success criterion), following appropriate font
t.place(x=660, y = 135) # placing listbox in appropriate position
# SCROLLBAR CONFIGURATION
scrollbary=tk.Scrollbar(root) # creates vertical scrollbar
scrollbary.pack(side='right', fill='y') # packs scrollbar to the right side, filling the y axis (.pack() feature)
scrollbarx=tk.Scrollbar(root, orient="horizontal") # creates horizontal scrollbar
scrollbarx.pack(side='bottom', fill='x') # packs scrollbar to the bottom, filling the x axis (.pack() feature)
# connecting scrollbars with listbox: NOTE this can be in the listbox configuration (t = (options...)), but is put here for clarity
t.config(yscrollcommand = scrollbary.set) # sets vertical scrollbar...
scrollbary.config(command = t.yview) # to scroll listbox vertically
t.config(xscrollcommand = scrollbarx.set) # sets horizontal scrollbar...
scrollbarx.config(command = t.xview) # to scroll listbox horizontally


# not done yet!





#-----------------------------START OF TOPLEVEL WINDOW-------------------------------#


"""
TASK CREATION WINDOW/POPUP
Using the Toplevel() function provided by Tkinter, we can
create another 'window' or popup that can run exactly like
our root window, but provides better user experience. Here
we add widgets that will allow users to graphically insert
their own tasks right back to the task list in the root
window. Functions/widgets/lists/variables include:
- Toplevel (alias taskCreator)
- DOW (list of abbreviated Days Of the Week)
- dowVar, dowVar2 (returns the two entries' (defined later) inputs as strings)
- addTask (adds tasks and saves to database (tascal.db))
"""
def openTaskCreator(): # defines the new window as 'openTaskCreator()' - Toplevel objects are treated as a new window 
    taskCreator = tk.Toplevel(root)  # sets window alias to 'taskCreator'
    taskCreator.configure(bg="white") # change taskCreator window bg colour
    taskCreator.title("Create a Task") # create title
    taskCreator.geometry("350x290") # set window size
    

    DOW = [         # defines list used for the two entrieds (start day, end day)
        'Mon',
        'Tue',
        'Wed',
        'Thurs',
        'Fri',
        'Sat',
        'Prev',
        'Later'
        ]

    dowVar = tk.StringVar(taskCreator) # returns the option into a string
    dowVar.set(DOW[0]) # sets default option
    dowVar2 = tk.StringVar(taskCreator) # returns the option into a string
    dowVar2.set(DOW[0]) # sets default option

    
    def addTask(event=None): # note: event=None so this function can be run on no direct event
      word = (dowVar.get()+"-"+dowVar2.get()+":"+" "+taskEntry.get()) # set the variable 'word' as the whole task entry, including the variables we assigned above to specify
                                                                      # the start + end date
      print(word) # prints the entry right after in case something goes wrong (you have a log of your added task in the console)
      if len(taskEntry.get())==0: # checks if the length of the entry is 0
        messagebox.showinfo('Empty Entry', 'Enter your task!') # shows a messagebox displaying error
      else: # if the length of the entry is not 0...
        cur = conn.cursor() # connects the cursor for read&write access
        task.append(word) # adds the new task (word) to the task list (task)
        cur.execute('insert into tasks values (?)', (word,)) # runs sq command to insert the new task (word) into chart 'tasks'
        listUpdate() # runs the listUpdate() function to refresh the list with the new task
        taskEntry.delete(0,'end') #removes entry in the box because it's now in the list
        conn.commit() # commits all changes
        cur.close() # closes the cursor for good practice
        taskCreator.destroy() # closes window
        
    
    taskCreator.bind('<Return>', addTask) # bind 'return' key to addTask function for improved UX
      

    # CREATING AND PLACING WIDGETS

    # creating new widgets, utilizing variables/lists/functions defined before
    taskLabel = tk.Label(taskCreator, text='Enter task title: ') # creating task entry prefix
    taskEntry = tk.Entry(taskCreator, width=21) # creating task entry, where users input their tasks
    fromLabel = tk.Label(taskCreator, text='From: ') # creating the start date label
    startDate = tk.OptionMenu(taskCreator, dowVar, *DOW) # creating the start date option menu, storing choice in 'dowVar' and choosing from list 'DOW'
    toLabel = tk.Label(taskCreator, text='To: ') # creating the end date label
    endDate = tk.OptionMenu(taskCreator, dowVar2, *DOW) # creating the start date option menu, storing choice in 'dowVar2' and choosing from list 'DOW' (same list)
    createTask = tk.Button(taskCreator, text='Add task', width=20, command=addTask) # adding the task creation button




    # placing widgets
    taskLabel.place(x=115, y=50) # placing task entry prefix
    taskEntry.place(x=70, y=80) # placing task entry
    fromLabel.place(x=77, y=130) # placing start date label
    startDate.place(x=65, y=150) # placing start date option menu
    toLabel.place(x=225, y=130) # placing end date label
    endDate.place(x=207, y=150) # placing end date option menu
    createTask.place(x=75, y=200) # placing task 

    
    taskCreator.mainloop() # start the main events loop (very similar to root window mainloop())


#-------------------------END OF TOPLEVEL WINDOW----------------------#


'''
EXTRA CALENDAR GEOMETRY AND DURATION VISUALIZER (not working) PROTOTYPE
Here is where the calendar bars are added, written below the Toplevel window
just to follow logical order. We create 7 different column bars for the 7 different
days of the week, and set the colors to alternating between the default gray and the
dark gray (same as background color, success criterion). Unfortunately, MacOSX messes
with some functions Tkinter provides, and there is no stable way to color buttons on a
Macintosh.
There is also an example of a task duration visualizer using the Canvas function that
tkinter provides (as an addon lib), but it is non-functional due to (reasons in video)
'''

# create 7 column bars for calendar (following color scheme)
monCol = tk.Button(root, height=18, width = 8, relief='flat', borderwidth=0, command = openTaskCreator, highlightbackground='#666666', bd=5) 
monCol.place(x=20, y=140)
tueCol = tk.Button(root, height=18, width = 8, relief='flat', borderwidth=0, command = openTaskCreator, highlightbackground='#23272A', bd=5)
tueCol.place(x=96, y=140)
wedCol = tk.Button(root, height=18, width = 8, relief='flat', borderwidth=0, command = openTaskCreator, highlightbackground='#666666', bd=5)
wedCol.place(x=172, y=140)
thursCol = tk.Button(root, height=18, width = 8, relief='flat', borderwidth=0, command = openTaskCreator, highlightbackground='#23272A', bd=5)
thursCol.place(x=248, y=140)
friCol = tk.Button(root, height=18, width = 8, relief='flat', borderwidth=0, command = openTaskCreator, highlightbackground='#666666', bd=5)
friCol.place(x=324, y=140)
satCol = tk.Button(root, height=18, width = 8, relief='flat', borderwidth=0, command = openTaskCreator, highlightbackground='#23272A', bd=5)
satCol.place(x=400, y=140)
sunCol = tk.Button(root, height=18, width = 8, relief='flat', borderwidth=0, command = openTaskCreator, highlightbackground='#666666', bd=5)
sunCol.place(x=476, y=140)



#TASK DURATION VISUALIZER (lines) using Canvas (unfinished)
#next steps: most feasible way to do this is to redo the task list by making fixed input boxes... (explain in video)
canvas = Canvas(root, width=475, height=10, borderwidth=0, highlightthickness=0, bg="maroon") # creating canvas shaped as line with thickness 10, length 45, colored maroon
canvas.place(x=50, y=150) # places line 



retrieveDB() # retrieves database
listUpdate() # updates 
conn.commit() # commits all unsaved changes to the database (tascal.db)
cur.close() # closes the cursor to finalize code
root.mainloop() # loops the program to initiate code



# end of code - no seriously, this is the end
