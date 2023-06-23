
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

