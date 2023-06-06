import sqlite3
from uuid import uuid4

connection = sqlite3.connect("user_details.db", check_same_thread=False)
cur = connection.cursor()

#A function that builds the database if not exists
def build_DB():
    command = """CREATE TABLE IF NOT EXISTS doctors_details_db(full_name TEXT NOT NULL, email TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, doctor_id TEXT NOT NULL) """
    command_2 = """CREATE TABLE IF NOT EXISTS patients_details_db(full_name TEXT NOT NULL, ID INTEGER NOT NULL, email TEXT NOT NULL, gender TEXT NOT NULL, birth_date TEXT NOT NULL, case_description TEXT NOT NULL, visit_date TEXT NOT NULL, doctor_id TEXT NOT NULL, x_ray_detection TEXT) """
    cur.execute(command)
    connection.commit()
    cur.execute(command_2)
    connection.commit()

#A function that receives a username and password. The function checks if the details exists in the database.
#The function returns False and None if it doesn't exist \ True and doctor_id if it does.
def find_username_and_password(username, password):
    cur.execute("SELECT rowid FROM doctors_details_db WHERE username = ? AND password = ?", (username, password,))
    db_result = cur.fetchall()
    print(type(db_result))
    if len(db_result) == 0:
        return False, None
    else:
        cur.execute("SELECT doctor_id FROM doctors_details_db WHERE username = ? AND password = ?", (username, password,))
        doctor_id_tuple = cur.fetchall()
        doctor_id_tuple = doctor_id_tuple[0]
        return True, str(doctor_id_tuple[0])

#A function that receuves name, email, username, password. The function adds the user details to the database.
#Returns True if succeeded and False if not.
def add_user(full_name, email, username, password):
    # check if a row is already exist
    cur.execute("SELECT rowid FROM doctors_details_db WHERE username = ?", (username,))
    db_result = cur.fetchall()
    if len(db_result) == 0:
        doctor_id = str(uuid4())
        connection.execute(
            "INSERT INTO doctors_details_db (full_name, email, username, password, doctor_id) VALUES (?,?,?,?,?)",(full_name, email, username, password, doctor_id))
        connection.commit()
        return True, doctor_id
    else:
        return False, None

#A function that receives full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id. The function add the details into a new patient. If the patient is already exists the function deletes the patient and then add the updated details as a new patient
def add_patient(full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id):
    try:
        # check if the patient is already exists
        cur.execute("SELECT rowid FROM patients_details_db WHERE ID = ?", (patient_id,))
        db_result = cur.fetchall()
        if len(db_result) != 0:
            connection.execute("DELETE FROM patients_details_db WHERE  ID = '" + patient_id + "'")
            connection.commit()
        connection.execute("INSERT INTO patients_details_db (full_name, ID, email, gender, birth_date, case_description, visit_date, doctor_id) VALUES (?,?,?,?,?,?,?,?)",(full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

#A function that receives full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id, x_ray_detection. The function add the details into a new patient. If the patient is already exists the function deletes the patient and then add the updated details as a new patient
def add_patient_with_photo(full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id, x_ray_detection):
    try:
        # check if the patient is already exists
        cur.execute("SELECT rowid FROM patients_details_db WHERE ID = ?", (patient_id,))
        db_result = cur.fetchall()
        if len(db_result) != 0:
            connection.execute("DELETE FROM patients_details_db WHERE  ID = '" + patient_id + "'")
            connection.commit()
        connection.execute("INSERT INTO patients_details_db (full_name, ID, email, gender, birth_date, case_description, visit_date, doctor_id, x_ray_detection) VALUES (?,?,?,?,?,?,?,?,?)",(full_name, patient_id, email, gender, birth_date, case_description, visit_date, doctor_id, x_ray_detection))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

#A function that receives patient_id. The function gets specific patient and returns it as a string (the details are seperated with '#').
def get_specific_patient(patient_id):
    cur.execute('SELECT * FROM patients_details_db')
    data = cur.fetchall()
    patient = ''
    for row in data:
        id = str(row[1])
        if id == patient_id:
            if row[-1] == None:
                row = row[:-1]
            patient += '#'.join(str(s) for s in row) + '\r\n'
            break
    if patient == '':
        return False, None
    else:
        return True, patient

#A function that receives doctor_id. The function gets all the patients that are belong to the doctor. The function returns all the patients as a list.
def get_patients_list(doctor_id):
    cur.execute('SELECT * FROM patients_details_db')
    data = cur.fetchall()
    patient_list = ''
    for row in data:
        if row[7] == doctor_id:
            patient_list += '#'.join(str(s) for s in row) + '\r\n'
    if patient_list == '':
        return False, None
    else:
        return True, patient_list