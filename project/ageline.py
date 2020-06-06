import matplotlib.pyplot as plt
from dboperation.dbconnection import DatabaseConnection as dbc


class Ageline():
    def __init__(self):
        super(Ageline, self).__init__()


def main():
    con = dbc.createconnection()
    dbcursor = con.cursor()
    str1 = 'select count(appointment.registrationid) from patient, appointment where age between 0 and 5 ' \
           'and appointment.registrationid = patient.registrationid;'
    str2 = 'select count(appointment.registrationid) from patient, appointment where age between 6 and 10 ' \
           'and appointment.registrationid = patient.registrationid;'
    str3 = 'select count(appointment.registrationid) from patient, appointment where age between 11 and 15 ' \
           'and appointment.registrationid = patient.registrationid;'
    str4 = 'select count(appointment.registrationid) from patient, appointment where age between 16 and 20 ' \
           'and appointment.registrationid = patient.registrationid;'
    str5 = 'select count(appointment.registrationid) from patient, appointment where age between 21 and 25 ' \
           'and appointment.registrationid = patient.registrationid;'
    str6 = 'select count(appointment.registrationid) from patient, appointment where age between 26 and 30 ' \
           'and appointment.registrationid = patient.registrationid;'
    str7 = 'select count(appointment.registrationid) from patient, appointment where age between 31 and 35 ' \
           'and appointment.registrationid = patient.registrationid;'
    str8 = 'select count(appointment.registrationid) from patient, appointment where age between 36 and 40 ' \
           'and appointment.registrationid = patient.registrationid;'
    str9 = 'select count(appointment.registrationid) from patient, appointment where age between 41 and 45 ' \
           'and appointment.registrationid = patient.registrationid;'
    str10 = 'select count(appointment.registrationid) from patient, appointment where age between 46 and 50 ' \
            'and appointment.registrationid = patient.registrationid;'
    str11 = 'select count(appointment.registrationid) from patient, appointment where age between 51 and 55 ' \
            'and appointment.registrationid = patient.registrationid;'
    str12 = 'select count(appointment.registrationid) from patient, appointment where age between 56 and 60 ' \
            'and appointment.registrationid = patient.registrationid;'
    str13 = 'select count(appointment.registrationid) from patient, appointment where age between 61 and 65 ' \
            'and appointment.registrationid = patient.registrationid;'
    str14 = 'select count(appointment.registrationid) from patient, appointment where age between 66 and 70 ' \
            'and appointment.registrationid = patient.registrationid;'
    str15 = 'select count(appointment.registrationid) from patient, appointment where age between 71 and 75 ' \
            'and appointment.registrationid = patient.registrationid;'
    str16 = 'select count(appointment.registrationid) from patient, appointment where age between 76 and 80 ' \
            'and appointment.registrationid = patient.registrationid;'
    dbcursor.execute(str1)
    y1 = dbcursor.fetchone()
    dbcursor.execute(str2)
    y2 = dbcursor.fetchone()
    dbcursor.execute(str3)
    y3 = dbcursor.fetchone()
    dbcursor.execute(str4)
    y4 = dbcursor.fetchone()
    dbcursor.execute(str5)
    y5 = dbcursor.fetchone()
    dbcursor.execute(str6)
    y6 = dbcursor.fetchone()
    dbcursor.execute(str7)
    y7 = dbcursor.fetchone()
    dbcursor.execute(str8)
    y8 = dbcursor.fetchone()
    dbcursor.execute(str9)
    y9 = dbcursor.fetchone()
    dbcursor.execute(str10)
    y10 = dbcursor.fetchone()
    dbcursor.execute(str11)
    y11 = dbcursor.fetchone()
    dbcursor.execute(str12)
    y12 = dbcursor.fetchone()
    dbcursor.execute(str13)
    y13 = dbcursor.fetchone()
    dbcursor.execute(str14)
    y14 = dbcursor.fetchone()
    dbcursor.execute(str15)
    y15 = dbcursor.fetchone()
    dbcursor.execute(str16)
    y16 = dbcursor.fetchone()
    y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16]
    x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
    plt.xlabel('Age')
    plt.ylabel('Patients')
    plt.title('Age Vs Patients')
    plt.plot(x, y, marker='o', color='red')
    plt.show()


if __name__ == '__main__':
    main()
