CREATE TABLE IF NOT SEXISTS STUDENT (
    eta_id TEXT PRIMARY KEY,
    name TEXT
    display_name TEXT
    instructor_id INTEGER,
    FOREIGN KEY (instructor_id) REFERENCE INSTRUCTOR (instructor_id)
);

CREATE TABLE IF NOT EXISTS INSTRUCTOR (
    instructor_id INTEGER PRIMARY KEY,
    name TEXT,
    display_name PRIMARY KEY,
    seminole_check Boolean,
    intermediate_check Boolean,
    eoc_check Boolean
);

CREATE TABLE IF NOT EXISTS AVAILABILITY (
    availability_id INTEGER PRIMARY KEY,
    event_day TEXT,
    start_time TIME,
    end_time TIME,
    eta_id INTEGER,
    FOREIGN KEY (eta_id) REFERENCES STUDENT (eta_id)
);