import pandas as pd
from functions import *
from sqlalchemy import create_engine
from dataframeset import schedule_df

a_schedule_df = schedule_df

Tue_df = pd.read_excel(testlist, sheet_name="Tue")
engine = create_engine('sqlite://', echo=False)
ss = Tue_df.to_sql('test_list', con=engine)
'''entry = "O"
result = pd.read_sql_query(f"SELECT * FROM test_list WHERE Name Like '{entry}%' ",engine)
list1 = []
#print(result.iloc[0,0:2].values)
list1.append(result.iloc[0,0:2].values[1])
print(list1)'''

def load_name_list(nameentry):
    namelist=[]
    names = pd.read_sql_query(f"SELECT * FROM test_list WHERE Name Like '{nameentry}%' ",engine)
    namelist.append(names.iloc[0,0:2].values[1])
    return namelist

'''SLpath = '/Users/oseongjae/PythonProject/NewProject/StudentList.xlsx'
AVpath = '/Users/oseongjae/PythonProject/NewProject/Availability.xlsx'

ws = testlist_wb.active
coln = 1
rown = 2
#get names
names = []
for col in ws.iter_cols(min_row= 2, max_col=1):
    for cell in col:
        names.append(cell.value)'''


class DuplicationError(Exception):
    pass

def add_schedule(df, name, day, starttime, endtime): # TODO: time change to datetime # handle conflict
    adf = df.loc[(df["Name"] == name)]
    try:
        for i, r in adf.iterrows():
            if (r['Day'] == day) & (r['StartTime'] == starttime):
                raise DuplicationError("Data is already exist")
    
        d = [name, day, starttime, endtime]
        df.loc[len(df)] = d
        print("New Data Added")
    except DuplicationError as e:
        print(e)



#print(names)

'''
print(f'OLD DATA: \n {a_schedule_df}')
#print(schedule_df.loc[(schedule_df["Name"] == 'Student1')])

add_schedule('Student1', 'Monday', '14:00', '16:00')
print(f'NEW DATA: \n {a_schedule_df}')

add_schedule('Student1', 'Monday', '14:00', '16:00')
print(f'NEW DATA: \n {a_schedule_df}')


add_schedule('Student1', 'Tuesday', '14:00', '16:00')
print(f'NEW DATA: \n {a_schedule_df}')
'''