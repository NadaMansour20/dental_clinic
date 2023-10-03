import sqlite3


def addPatient(patient_id,name, age, gender,phoneNumber, diseases):
    con = sqlite3.connect('Dental Clinic.db')
    cursor = con.cursor()
    cursor.execute('insert into Patient values (?,?,?,?,?,?)', (patient_id,name, age, gender,phoneNumber,diseases))
    con.commit()
    con.close()


def showAllpatient():
    con = sqlite3.connect('Dental Clinic.db')
    cursor = con.cursor()
    data = cursor.execute('select * from Patient')
    con.commit()
    return data


def deletepatient(patientID):
    con = sqlite3.connect('Dental Clinic.db')
    cursor = con.cursor()
    cursor.execute(f'delete from Patient where Patient_ID={patientID}')
    con.commit()
    con.close()

def show(patientID):
    con = sqlite3.connect('Dental Clinic.db')
    cursor = con.cursor()
    cursor.execute(f'select * from Patient where Patient_ID={patientID}')
    resualt=cursor.fetchall()
    return resualt



def updatepatient(patientID, name, age, gender,phoneNumber,diseases):
    con = sqlite3.connect('Dental Clinic.db')
    cursor = con.cursor()
    cursor.execute('update Patient set Patient_ID=? ,Name=?,Age=?,Gender=?,Phone_Number=?, Diseases=? ',
                   (patientID, name, age, gender, phoneNumber,diseases))
    con.commit()
    con.close()

