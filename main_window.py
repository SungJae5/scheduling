from cgitb import small
from tkinter import messagebox
from turtle import bgcolor
import tkinter as tk
from functions import *
from sqlalchemy import engine
import MainFunction
import datacontrol

class MainWindow(tk.Tk):
    def __init__(self):
        tk.__init__(self)
        self.title("MAIN WINDOW")
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
        student_list_df = datacontrol.load_
        label2= tk.Label(self.frame1, text='STUDENT LIST')
        tree1 = self.tree()