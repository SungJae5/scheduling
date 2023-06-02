import pandas as pd

schedule_col = ['Name', 'Day',
    'StartTime', 'EndTime']
schedule_data = [['Student1', 'Monday', '9:00', '9:50'],
    ['Student1', 'Monday', '10:00', '12:00'],
    ['Student1', 'Tuesday', '8:00', '9:50'],
    ['Student2', 'Monday', '10:00', '12:00']]

schedule_df = pd.DataFrame(schedule_data, columns=schedule_col)