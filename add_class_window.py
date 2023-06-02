import customtkinter as tk
from tkinter import *
from sqlalchemy import engine
from MainFunction import add_schedule
import pandas as pd

#DATAFRAME
#TODO: DATA SHOULD BE LOADED FROM EXCEL FILE!
schedule_col = ['Name', 'Day',
'StartTime', 'EndTime']
schedule_data = [['Student1', 'Monday', '9:00', '9:50'],
['Student1', 'Monday', '10:00', '12:00'],
['Student1', 'Tuesday', '8:00', '9:50'],
['Student2', 'Monday', '10:00', '12:00']]

schedule_df = pd.DataFrame(schedule_data, columns=schedule_col)


###

tk.set_default_color_theme("dark-blue") 
window = tk.CTk()
window.title('ADD CLASS WINDOW')
window.geometry("800x800")
window.configure(bg = "gray")
Bigfont = ('Arial', 25, 'bold')
SmallFont = ('Arial', 18, 'bold')


###
def checkbox_refresh():
    for v in checkbtn_var_list:
        v = 0

def submit_clicked():
    days_dict = {'Monday' : var_M,
    'Tuesday' : var_T,
    'Wednesday' : var_W,
    'Thursday' : var_TH,
    'Friday' : var_F,
    'Saturday' : var_Sat,
    'Sunday' : var_Sun,
    }
    for key in days_dict:
        if days_dict[key].get() == 1:
            add_schedule(schedule_df, student_name, key, starttime_val, endtime_val)
    checkbox_refresh()
    df_label.config(text=f'NEW DATA: \n {schedule_df}')
    print(schedule_df)


#CheckBox
var_M = tk.IntVar()
var_T = tk.IntVar()
var_W = tk.IntVar()
var_TH = tk.IntVar()
var_F = tk.IntVar()
var_Sat = tk.IntVar()
var_Sun = tk.IntVar()


checkbutton_1 = Checkbutton(window, borderwidth = 10, text='M',variable=var_M, onvalue=1, offvalue=0)
checkbutton_2 = Checkbutton(window, borderwidth = 10, text='T',variable=var_T, onvalue=1, offvalue=0)
checkbutton_3 = Checkbutton(window, borderwidth = 10, text='W',variable=var_W, onvalue=1, offvalue=0)
checkbutton_4 = Checkbutton(window, borderwidth = 10, text='Th',variable=var_TH, onvalue=1, offvalue=0)
checkbutton_5 = Checkbutton(window, borderwidth = 10, text='F',variable=var_F, onvalue=1, offvalue=0)
checkbutton_6 = Checkbutton(window, borderwidth = 10, text='Sat',variable=var_Sat, onvalue=1, offvalue=0)
checkbutton_7 = Checkbutton(window, borderwidth = 10, text='Sun',variable=var_Sun, onvalue=1, offvalue=0)
checkbutton_1.pack()
checkbutton_2.pack()
checkbutton_3.pack()
checkbutton_4.pack()
checkbutton_5.pack()
checkbutton_6.pack()
checkbutton_7.pack()

checkbtn_var_list = [var_M,
var_T ,
var_W ,
var_TH ,
var_F ,
var_Sat ,
var_Sun]

#Dropdown
options = ['7:00','8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00']			
start_clicked = StringVar(window)
end_clicked = StringVar(window)

start_clicked.set('7:00')
end_clicked.set('20:00')

dropdown_1 = OptionMenu(window, start_clicked, *options)
dropdown_1.config(font=SmallFont,foreground='black',text=start_clicked.get())
dropdown_1.pack()
label = Label(window, text= f'selected start time: {start_clicked.get()}')
label.pack()

dropdown_2 = OptionMenu(window, end_clicked, *options)
dropdown_2.config(font=SmallFont,foreground='black',text=end_clicked.get())
end_label = Label(window, text= f'selected end time: {end_clicked.get()}')
dropdown_2.pack()
end_label.pack()

submit_btn = Button(window, text='SUBMIT',font=SmallFont, command=submit_clicked,foreground='black')
submit_btn.pack()
starttime_val = start_clicked.get()
endtime_val = end_clicked.get()

#TODO: STUDENT NAME SHOULD BE RETRIVED FROM ENTERED VALUE
student_name = 'Student1'

df_label = Label(window, text=f'CURRENT DATA: \n{schedule_df}')
df_label.pack()




window.resizable(True, True)
window.mainloop()
