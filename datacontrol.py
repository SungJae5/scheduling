import pandas as pd
from openpyxl.utils import column_index_from_string
import sqlite3
import csv

def create_data(input_file):
    output_file = "output.csv"
    # Define columns that wants to retreived
    col_letters = ['O','P','Q','S','V']
    columns = [l.column_index_from_string for l in col_letters]
    # Load the input Excel file
    df = pd.read_csv(input_file)

    # Create a new workbook for the output file
    output_df = df.iloc[:, columns]

    # File format control
    if output_file.endswith('.csv'):
        output_df.to_csv(output_file, index=False)
    elif output_file.endswith('.xlsx'):
        output_df.to_excel(output_file, index=False)
    else:
        raise ValueError("Output file format not supported.")

    return output_df

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



