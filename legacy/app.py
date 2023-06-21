from cgitb import small
from tkinter import messagebox
from turtle import bgcolor
import customtkinter as tk
from tkinter import *
from functions import *
from sqlalchemy import engine
import MainFunction


# load names from excel file




# TKINTER

tk.set_default_color_theme("dark-blue") 
app = tk.CTk()
app.title('Data Entry')
app.geometry("800x800")
app.configure(bg = "gray")
Bigfont = ('Arial', 25, 'bold')
SmallFont = ('Arial', 18, 'bold')
###

# POP UP WINDOW
def open_popup():
    top = Toplevel(app)
    top.geometry("500x500")
    top.configure(bg = 'gray')
    namevariable = listbox1.get(listbox1.curselection())
    top.title(f"{namevariable}'s Schedule")
    top.grid_columnconfigure(0, weight=2)
    top.grid_columnconfigure(1, weight=1)
    top.grid_columnconfigure(2, weight=1)
    top.grid_columnconfigure(3, weight=1)
    top.grid_rowconfigure(0, width = 0)
    top.grid_rowconfigure(1, weight= 0)
    top.grid_rowconfigure(2, weight= 0)
    top.grid_rowconfigure(3, weight= 0)
    top.grid_rowconfigure(4, weight= 0)
    top.grid_rowconfigure(5, weight= 0)
    top.grid_rowconfigure(6, weight= 0)
    pop_up_frame1 = Frame(top)




def helloCallBack():
    messagebox.showinfo(message='Button Clicekd!')
    app.destroy()

#def show():
    #label.config(text = clicked.get() )
###
canvas = Canvas(
    app,
    bg = "gray",
    height = 800,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


button_1 = Button(
    borderwidth=0,
    highlightthickness=0,
    command=helloCallBack,
    relief="flat",
    text = "Back", font=SmallFont, fg='#000000'
)

button_1.place(
    x=582.0,
    y=463.0,
    width=100.0,
    height=25.0
)
###
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()


checkbutton_1 = Checkbutton(app, borderwidth = 10, text='M',variable=var1, onvalue=1, offvalue=0)
checkbutton_2 = Checkbutton(app, borderwidth = 10, text='T',variable=var2, onvalue=1, offvalue=0)
checkbutton_3 = Checkbutton(app, borderwidth = 10, text='W',variable=var3, onvalue=1, offvalue=0)
checkbutton_4 = Checkbutton(app, borderwidth = 10, text='Th',variable=var4, onvalue=1, offvalue=0)
checkbutton_5 = Checkbutton(app, borderwidth = 10, text='F',variable=var5, onvalue=1, offvalue=0)
checkbutton_6 = Checkbutton(app, borderwidth = 10, text='Sat',variable=var6, onvalue=1, offvalue=0)
checkbutton_7 = Checkbutton(app, borderwidth = 10, text='Sun',variable=var7, onvalue=1, offvalue=0)
checkbutton_1.pack()
checkbutton_2.pack()
checkbutton_3.pack()
checkbutton_4.pack()
checkbutton_5.pack()
checkbutton_6.pack()
checkbutton_7.pack()

options = ['7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00']			
clicked = StringVar(app)
clicked.set('7:00')

dropdown_1 = OptionMenu(app, clicked, *options)
dropdown_1.config(font=SmallFont,foreground='black',text=clicked.get())
dropdown_1.pack()
label = Label(app, text= clicked.get())
drop_button_1 = Button(app, text='Start Time',font=SmallFont, command=label.pack,foreground='black')
drop_button_1.pack()


frame = tk.CTkFrame(app, border_color='#FFFFFF', width= 800, height= 800)




###
def name_search():
    value = namevariable.get()
    label2.config(text=value)

def refresh_list():
    name_search()
    count = 0
    listbox1.delete(0, END)
    newlist = MainFunction.load_name_list(namevariable.get())
    for n in newlist:
        listbox1.insert(count, n)
        count += 1


#DONE
def entry_button_1_click():
    name_search()
    refresh_list()


canvas.place(x = 0, y = 0)

namevariable = tk.StringVar()
nameentry = tk.CTkEntry(app,width=100, height= 40, textvariable=namevariable)
entry_button_1 = Button(app,text='Search',font=SmallFont, command = entry_button_1_click, foreground='black')
label2=Label(app, text=namevariable.get())
nameentry.pack()
entry_button_1.pack()
label2.pack()


submit_button_1 = Button(app, text='Submit', font=SmallFont, command=open_popup,fg="black" )
submit_button_1.pack()

name_list = MainFunction.load_name_list("")
label3 = Label(app, text='Select List')
listbox1 = Listbox(app)
label3.pack()
listbox1.pack()
#selection = listbox1.curselection()
#label4 = Label(app, text=listbox1.get(selection))
#label4.pack()


app.resizable(True, True)
app.mainloop()


#TODO
#List Box Selection save to variable
#new popup window
#pop up window - table view Names, Course, Instructor, lastdate edited on the top frame
#Days, StarTime, Endtime
# find the names 