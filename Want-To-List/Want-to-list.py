#Imports

import pickle
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from playsound import playsound









#Main Window

window = Tk()
window.iconbitmap(r'Images\python_image.ico')
window.title("Tirth's To do List")
window.geometry('1400x700+30+30')
window.config(bg = '#FEC931')









#Variables

variable1 = StringVar()
groupdata = 'Group1'
goodboy = StringVar()










#Functions



def delete():
    selection=list_box.curselection()
    if selection:
        list_box.delete(selection[0])

def renameindata():
    global goodboy
    letsdoit = goodboy.get()
    if groupdata == 'Group1':
        pickle.dump(letsdoit, open('Others\Group1_name.dat','wb'))
    elif groupdata == 'Group2':
        pickle.dump(letsdoit, open('Others\Group2_name.dat','wb'))
    elif groupdata == 'Group3':
        pickle.dump(letsdoit, open('Others\Group3_name.dat','wb'))
    elif groupdata == 'Group4':
        pickle.dump(letsdoit, open('Others\Group4_name.dat','wb'))


def new():
    global variable1
    if variable1.get() == '':
        messagebox.showerror('ERROR','Input is blank -_-')
    else :
        list_box.insert(END,variable1.get())      
        inputer.delete(0,END)

def renamed():
    global goodboy,groupdata
    lol = goodboy.get()
    if groupdata == 'Group1':
        sideframebtn1.config(text = lol)
        renameindata()
    elif groupdata == 'Group2':
        sideframebtn2.config(text = lol)
        renameindata()
    elif groupdata == 'Group3':
        sideframebtn3.config(text = lol)
        renameindata()
    elif groupdata == 'Group4':
        sideframebtn4.config(text = lol)
        renameindata()

def save():
    global groupdata
    if groupdata == 'Group1':
        alltask = list_box.get(0,list_box.size())
        pickle.dump(alltask, open('Others\Group1List.dat','wb'))

    elif groupdata == 'Group2':
        alltask = list_box.get(0,list_box.size())
        pickle.dump(alltask, open('Others\Group2List.dat','wb'))

    elif groupdata == 'Group3':
        alltask = list_box.get(0,list_box.size())
        pickle.dump(alltask, open('Others\Group3List.dat','wb'))
    
    elif groupdata == 'Group4':
        alltask = list_box.get(0,list_box.size())
        pickle.dump(alltask, open('Others\Group4List.dat','wb'))


def load():
    global groupdata
    if groupdata == 'Group1':  
        alltasks = pickle.load(open('Others\Group1List.dat','rb'))
        list_box.delete(0,END)
        for eachtask in alltasks:
            list_box.insert(END,eachtask)

    elif groupdata == 'Group2':  
        alltasks = pickle.load(open('Others\Group2List.dat','rb'))
        list_box.delete(0,END)
        for eachtask in alltasks:
            list_box.insert(END,eachtask)
    
    elif groupdata == 'Group3':  
        alltasks = pickle.load(open('Others\Group3List.dat','rb'))
        list_box.delete(0,END)
        for eachtask in alltasks:
            list_box.insert(END,eachtask)

    elif groupdata == 'Group4':  
        alltasks = pickle.load(open('Others\Group4List.dat','rb'))
        list_box.delete(0,END)
        for eachtask in alltasks:
            list_box.insert(END,eachtask)

def grouper1():
    global groupdata
    groupdata = 'Group1'
    load()

def grouper2():
    global groupdata
    groupdata = 'Group2'
    load()

def grouper3():
    global groupdata
    groupdata = 'Group3'
    load()

def groupe4():
    global groupdata
    groupdata = 'Group4'
    load()

def done():
    selection = list_box.curselection()
    if selection:
        list_box.delete(selection[0])
        playsound('Sound/Done.mp3')

def rename_group():
    global goodboy
    popup = Toplevel()
    popup.title('Rename Group')
    popup.resizable(0,0)
    entry = Entry(popup,textvariable = goodboy)
    entry.pack()
    btn = Button(popup,text = 'Rename',command = renamed)
    btn.pack()









#Frames

TopFrame = Frame(window,bg = 'orange')
TopFrame.pack(side = TOP,fill = X)
SideFrame = Frame(window,bg = 'Red')
SideFrame.pack(side = LEFT,fill = Y)







#Top Bar Widgets

topbarlbl = Label(TopFrame,text='Tirth - Want To List',bg = 'Orange',font = 'Verdana 20')
topbarlbl.pack()








#Side Frame Buttons

sideframebtn1 = Button(SideFrame,text = 'Group 1',command = grouper1,relief = GROOVE,bg = 'Orange',border = 0,font = 'Verdana 15')
sideframebtn1.place(y = 20)
sideframebtn1.pack(padx = 10,pady = 20)

sideframebtn2 = Button(SideFrame,text = 'Group 2',command = grouper2,relief = GROOVE,bg = 'Orange',border = 0,font = 'Verdana 15')
sideframebtn2.pack(padx = 10,pady = 20)

sideframebtn3 = Button(SideFrame,text = 'Group 3',command = grouper3,relief = GROOVE,bg = 'Orange',border = 0,font = 'Verdana 15')
sideframebtn3.pack(padx = 10,pady = 20)

sideframebtn4 = Button(SideFrame,text = 'Group 4',command = groupe4,relief = GROOVE,bg = 'Orange',border = 0,font = 'Verdana 15')
sideframebtn4.pack(padx = 10,pady = 20)







#List

list_box = Listbox(
    window
)
list_box.pack(expand = True,fill = 'both',pady=10,padx = 10,)

list_box.config(font = ('Bubble Rainbow',15))

inputer = Entry(
    window,
    textvariable = variable1,
    width = 100,
    font = 'Verdana 15 '
)

inputer.pack()








#InList Buttons

Inlistframe = Frame(window,bg = '#FEC931',height = 20)
Inlistframe.pack()

button = Button(
    Inlistframe,
    text = 'Add',
    relief = RAISED,
    bg = '#FFB266',
    font = 'Cooper 15',
    command = new
)
button.pack(side = LEFT,pady = 10)

button2 = Button(
    Inlistframe,
    text = 'Delete',
    relief = RAISED,
    bg = '#FFB266',
    font = 'Cooper 15 ',
    command = delete
)
button2.pack(side = LEFT,pady=10)

button3 = Button(
    Inlistframe,
    text = 'Save',
    relief = RAISED,
    font = 'Cooper 15',
    bg = '#FFB266',
    command = save
)
button3.pack(side = LEFT,pady=10)

button4 = Button(
    Inlistframe,
    text = 'Done',
    relief = RAISED,
    font = 'Cooper 15 ',
    bg = '#FFB266',
    command = done
)
button4.pack(side=LEFT,pady=10)

button5 = Button(
    Inlistframe,
    text = 'Rename Group',
    font = 'Cooper 15',
    relief = RAISED,
    bg = '#FFB266',
    command = rename_group
)
button5.pack(side=LEFT,pady=10)

#ScrollBar









#End Frame

EndFrame = Frame(window,bg = '#FEC931',height = 20)
EndFrame.pack(fill = BOTH)









#Start


def started():
    group1name = pickle.load(open('Others\Group1_name.dat','rb'))
    sideframebtn1.config(text = group1name)
    group2name = pickle.load(open('Others\Group2_name.dat','rb'))
    sideframebtn2.config(text = group2name)
    group3name = pickle.load(open('Others\Group3_name.dat','rb'))
    sideframebtn3.config(text = group3name)
    group4name = pickle.load(open('Others\Group4_name.dat','rb'))
    sideframebtn4.config(text = group4name)
    
    load()

started()

window.mainloop()
