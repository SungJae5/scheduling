from cgitb import small
import tkinter as tk
import tkinter.ttk as ttk
from sqlalchemy import engine
import datacontrol
import pandas as pd

class MainWindow(tk.Tk):
    def __init__(self):
        self.wm_title("MAIN WINDOW")
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
        
        #load main data
        maindata = datacontrol.create_data_from_csv('input.csv')

        #Entry Frame
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row=0, column=0, columnspan=4, sticky='we')

        #Teams widgets
        label1= tk.Label(self.frame1, text='SCHEDULER TEAM')
        team_options = datacontrol.load_teams_data_to_list('schedulerlist.xlsx')
        selected_team = tk.StringVar(self)
        dropdown1 = tk.OptionMenu(self.frame1, selected_team, *team_options)
        dropdown1.config(font=SmallFont,foreground='black',text=selected_team.get())

        label1.pack(self.frame1)
        dropdown1.pack(self.frame1)

        #SEARCH STUDENT Widgets
        student_list_df = datacontrol.filter_dataframe(maindata,'Team',selected_team,[''])
        s_list = datacontrol.convert_df_to_list(student_list_df)
        label2= tk.Label(self.frame1, text='STUDENT LIST')
        tree_cols = ('Name',
    'ETA ID',
    'Display Name',
    'Course',
    'Team',
    'Instructor')
        tree1 = ttk.Treeview (self.frame1, columns = tree_cols, show='headings')
        tree1.heading('Name', text='Name')
        tree1.heading('ETA ID', text='ETA ID')
        tree1.heading('Display Name', text='Display Name')
        tree1.heading('Course', text='Course')
        tree1.heading('Team', text='Team')
        tree1.heading('Instructor', text='Instructor')
        for s in s_list:
            tree1.insert('','end',values=s)
        def item_selected(event): #TODO: See if this works
            for selected_item in tree1.selection():
                item = tree1.item(selected_item)
                record = item['values']
                tk.showinfo(title='Information',message=','.join(record))
        tree1.bind('<<TreeviewSelect>>', item_selected)

        #TODO: TREEVIEW NEEDS TO BE DYNAMICALLY chagned

        # Edit Button
        def OpenEditWindow(event): #TODO: define the fuction open the new window for editting
            pass
        edit_btn = tk.Button(self, text='Edit', Command=OpenEditWindow)
        edit_btn.grid(row=3, column=4) # TODO: CHECK THE GRID R,C




        
