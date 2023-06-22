import pandas as pd
from openpyxl.utils import column_index_from_string
import sqlite3
import datetime

class Availability:
    def __init__(self, owner_id:str, event_day:str, start_t:str, end_t:str):
        self.event_day = event_day
        self.owner_id = owner_id
        self.start_t = datetime.datetime.strptime(start_t, '%H:%M')
        self.end_t = datetime.datetime.strptime(end_t, '%H:%M')


def create_data(input_file):
    '''
    Last Name, First Name	
    ETA ID	
    Display Name	
    Person Subtype	
    Course	
    Class	
    Team	
    Instructor	Status
'''
    output_file = "output.csv"
    # Define columns that wants to retreived
    col_letters = ['O','P','Q','S','V']
    columns = [l.column_index_from_string for l in col_letters]
    # Load the input Excel file
    df = pd.read_csv(input_file)

    # Create a new workbook for the output file
    output_df = df.iloc[:, columns]
    output_df = output_df.drop_duplicates()

    # File format control
    if output_file.endswith('.csv'):
        output_df.to_csv(output_file, index=False)
    elif output_file.endswith('.xlsx'):
        output_df.to_excel(output_file, index=False)
    else:
        raise ValueError("Output file format not supported.")

    return output_df

def create_instructor_list(input_file_path) -> pd.DataFrame:
    df = pd.read_excel(input_file_path)
    return df

def add_availability(data, owner_id, event_day, start_t, end_t):
    item = [owner_id, event_day,start_t,end_t]
    output_df = pd.read_excel(data)
    output_df.append(item, ignore_index=True)

    now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    output_df.to_excel(now+"updated_availability.xlsx")

def add_many_avb(data, avb_dict:dict):
    '''function avb_dict ={  owner_id: owner's eta_id (unique value),
                    event_day: occruing day (str),
                    start_t: start time (str),
                    end_t: end time (str) }'''
    
    output_df = pd.read_excel(data)
    output_df.append(avb_dict, ignore_index=True)

    now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    output_df.to_excel(now+"updated_availability.xlsx")


# Connect to the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create the STUDENT table
cursor.execute(''' 
CREATE TABLE IF NOT SEXISTS STUDENT (
eta_id TEXT PRIMARY KEY,
name TEXT
display_name TEXT
instructor_id INTEGER,
FOREIGN KEY (instructor_id) REFERENCE INSTRUCTOR (instructor_id)
)''')
               
# Create the INSTRUCTOR table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS INSTRUCTOR (
        instructor_id INTEGER PRIMARY KEY,
        name TEXT,
        display_name PRIMARY KEY,
        seminole_check Boolean,
        intermediate_check Boolean,
        eoc_check Boolean
    )
''')
               
# Create the AVAILABILITY table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS AVAILABILITY (
        availability_id INTEGER PRIMARY KEY,
        event_day TEXT,
        start_time TEXT,
        end_time TEXT,
        eta_id INTEGER,
        FOREIGN KEY (eta_id) REFERENCES STUDENT (eta_id)
    )
''')



