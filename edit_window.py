import tkinter as tk

class Edit_window():
  def __init__(self):
      tk.__init__(self)
      self.title("EDIT WINDOW")
      self.geometry('800x600')
      self.configure(bg='gray')
      SmallFont = ('Arial', 18, 'bold')
      # GRID 5 x 5
      self.grid_columnconfigure(0, weight=0)
      self.grid_columnconfigure(1, weight=0)
      self.grid_columnconfigure(2, weight=0)
      self.grid_columnconfigure(3, weight=0)
      self.grid_columnconfigure(3, weight=0)
      self.grid_rowconfigure(0, weight = 0)
      self.grid_rowconfigure(1, weight= 0)
      self.grid_rowconfigure(2, weight= 0)
      self.grid_rowconfigure(3, weight= 0)
      self.grid_rowconfigure(4, weight= 0)
    #STUDENT'S Availability as DataFrame View?


    '''
    #Function for Refresh Checkbox - setting to 0
def checkbox_refresh():
    for cbtn in checkbutton_list:
        cbtn.set(0)

#SUBMIT THE SCHEDULE IN
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

checkbutton_list = [checkbutton_1,
checkbutton_2,
checkbutton_3,
checkbutton_4,
checkbutton_5,
checkbutton_6,
checkbutton_7]

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
'''

