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


def filter_dataframe(targetdata:pd.DataFrame, target_col, target_val, filter_col:list) -> pd.DataFrame:
    filtered_df = targetdata[targetdata[target_col] == target_val]
    if filter_col is not None:
        result_df = filtered_df[filter_col]
    else:
        result_df = filtered_df
    return result_df

def load_teams_data_to_list(input_file) -> list:
    df = pd.read_excel(input_file)
    result = [i for i in df['teams']]
    return result



def create_data_from_csv(input_file)->pd.DataFrame:
    '''
    input data needs to be csv file
    Last Name, First Name	O
    ETA ID	P
    Display Name	Q
    Person Subtype	 R
    Course	S
    Class	T
    Team	U
    Instructor	V
    Status W
    '''

    output_file = "output.csv"
    # Define columns that wants to retreived
    col_letters = ['O','P','Q','S','V']
    columns = [l.column_index_from_string for l in col_letters]
    headings = ['Name',
    'ETA ID',
    'Display Name',
    'Course',
    'Team',
    'Instructor']
    # Load the input Excel file
    df = pd.read_csv(input_file)


    # Create a new workbook for the output file
    output_df = df.iloc[:, columns]
    output_df = output_df.drop_duplicates(keep='first')
    result_df = pd.DataFrame(output_df, columns=headings)

    # File format control
    if output_file.endswith('.csv'):
        result_df.to_csv(result_df, index=False)
    elif output_file.endswith('.xlsx'):
        result_df.to_excel(result_df, index=False)
    else:
        raise ValueError("Output file format not supported.")

    return result_df

def create_instructor_list(input_file_path) -> pd.DataFrame:
    df = pd.read_excel(input_file_path)
    return df

def add_availability(data, owner_id, event_day, start_t, end_t):
    item = [owner_id, event_day,start_t,end_t]
    output_df = pd.read_excel(data)
    output_df.append(item, ignore_index=True)

    now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    output_df.to_excel(now+"updated_availability.xlsx")

def add_many_avb(data, avb_dict:dict) -> pd.DataFrame:
    '''function avb_dict ={ owner_id: owner's eta_id (unique value),
                            event_day: occruing day (str),
                            start_t: start time (str),
                            end_t: end time (str) }'''
    
    output_df = pd.read_excel(data)
    output_df.append(avb_dict, ignore_index=True)

    return output_df

def save_avbdata_to_excel(data) -> None:
    now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    data.to_excel(now+"updated_availability.xlsx")

def select_target(avb_data:pd.DataFrame, eta_id) -> pd.DataFrame:
    filtered_df = avb_data[avb_data['owner_id'] == eta_id]
    output_df = filtered_df['id','start_t','end_t']
    return output_df

def convert_df_to_list(data: pd.DataFrame) -> list:
    result = data.values.tolist()
    return result


