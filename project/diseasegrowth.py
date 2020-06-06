from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from project import ageline
from project.genderage import *
from project.genderpie import *
from project.diseasemanage import DiseaseManagement
from dboperation.dbconnection import DatabaseConnection as dbc
import sys


class DiseaseGrowing(QFrame):
    def __init__(self):
        super(DiseaseGrowing, self).__init__()
        loadUi("DiseaseGrowing.ui", self)
        self.btnagewisedisease.clicked.connect(lambda: self.buttonclicked(self.btnagewisedisease))
        self.btngenderwisedisease.clicked.connect(lambda: self.buttonclicked(self.btngenderwisedisease))
        self.btngenderandagewisedisease.clicked.connect(lambda: self.buttonclicked(self.btngenderandagewisedisease))
        self.btnregularbasisdisease.clicked.connect(lambda: self.buttonclicked(self.btnregularbasisdisease))
        self.btnfastestgrowingdisease.clicked.connect(lambda: self.buttonclicked(self.btnfastestgrowingdisease))

    def buttonclicked(self, btn):
        info = btn.text()
        if info == "Age wise Disease":
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

        if info == "Gender wise disease":
            con = dbc.createconnection()
            dbcursor = con.cursor()
            str1 = "select count(registrationid) from patient where gender = 'M';"
            dbcursor.execute(str1)
            m_pat = dbcursor.fetchall()
            str2 = "select count(registrationid) from patient where gender = 'F';"
            dbcursor.execute(str2)
            f_pat = dbcursor.fetchall()
            graphlabels = ('Male Patients', 'Female Patients')
            sizes = [m_pat, f_pat]
            clr = ['green', 'red']
            plt.pie(sizes, labels=graphlabels, colors=clr)
            plt.title('Gender Vs Disease')
            plt.show()

        if info == "Gender And Age Wise Disease":
            con = dbc.createconnection()
            dbcursor = con.cursor()
            strym1 = 'select count(a.registrationid) from patient p, appointment a where gender="M" and age between 0 and 10 and p.registrationid=a.registrationid;'
            strym2 = 'select count(a.registrationid) from patient p, appointment a where gender="M" and age between 11 and 20 and p.registrationid=a.registrationid;'
            strym3 = 'select count(a.registrationid) from patient p, appointment a where gender="M" and age between 21 and 30 and p.registrationid=a.registrationid;'
            strym4 = 'select count(a.registrationid) from patient p, appointment a where gender="M" and age between 31 and 40 and p.registrationid=a.registrationid;'
            strym5 = 'select count(a.registrationid) from patient p, appointment a where gender="M" and age between 41 and 50 and p.registrationid=a.registrationid;'
            strym6 = 'select count(a.registrationid) from patient p, appointment a where gender="M" and age between 51 and 60 and p.registrationid=a.registrationid;'
            strym7 = 'select count(a.registrationid) from patient p, appointment a where gender="M" and age between 61 and 70 and p.registrationid=a.registrationid;'
            strym8 = 'select count(a.registrationid) from patient p, appointment a where gender="M" and age between 71 and 80 and p.registrationid=a.registrationid;'
            stryf1 = 'select count(a.registrationid) from patient p, appointment a where gender="F" and age between 0 and 10 and p.registrationid=a.registrationid;'
            stryf2 = 'select count(a.registrationid) from patient p, appointment a where gender="F" and age between 11 and 20 and p.registrationid=a.registrationid;'
            stryf3 = 'select count(a.registrationid) from patient p, appointment a where gender="F" and age between 21 and 30 and p.registrationid=a.registrationid;'
            stryf4 = 'select count(a.registrationid) from patient p, appointment a where gender="F" and age between 31 and 40 and p.registrationid=a.registrationid;'
            stryf5 = 'select count(a.registrationid) from patient p, appointment a where gender="F" and age between 41 and 50 and p.registrationid=a.registrationid;'
            stryf6 = 'select count(a.registrationid) from patient p, appointment a where gender="F" and age between 51 and 60 and p.registrationid=a.registrationid;'
            stryf7 = 'select count(a.registrationid) from patient p, appointment a where gender="F" and age between 61 and 70 and p.registrationid=a.registrationid;'
            stryf8 = 'select count(a.registrationid) from patient p, appointment a where gender="F" and age between 71 and 80 and p.registrationid=a.registrationid;'
            dbcursor.execute(strym1)
            ym1 = dbcursor.fetchone()
            dbcursor.execute(strym2)
            ym2 = dbcursor.fetchone()
            dbcursor.execute(strym3)
            ym3 = dbcursor.fetchone()
            dbcursor.execute(strym4)
            ym4 = dbcursor.fetchone()
            dbcursor.execute(strym5)
            ym5 = dbcursor.fetchone()
            dbcursor.execute(strym6)
            ym6 = dbcursor.fetchone()
            dbcursor.execute(strym7)
            ym7 = dbcursor.fetchone()
            dbcursor.execute(strym8)
            ym8 = dbcursor.fetchone()
            dbcursor.execute(stryf1)
            yf1 = dbcursor.fetchone()
            dbcursor.execute(stryf2)
            yf2 = dbcursor.fetchone()
            dbcursor.execute(stryf3)
            yf3 = dbcursor.fetchone()
            dbcursor.execute(stryf4)
            yf4 = dbcursor.fetchone()
            dbcursor.execute(stryf5)
            yf5 = dbcursor.fetchone()
            dbcursor.execute(stryf6)
            yf6 = dbcursor.fetchone()
            dbcursor.execute(stryf7)
            yf7 = dbcursor.fetchone()
            dbcursor.execute(stryf8)
            yf8 = dbcursor.fetchone()
            ym = [ym1, ym2, ym3, ym4, ym5, ym6, ym7, ym8]
            yf = [yf1, yf2, yf3, yf4, yf5, yf6, yf7, yf8]
            x = [10, 20, 30, 40, 50, 60, 70, 80]
            plt.plot(x, yf, marker='o', color='red', label='Female')
            plt.plot(x, ym, marker='o', color='green', label='Male')
            plt.xlabel('Age')
            plt.ylabel('Patients')
            plt.title('Gender & Age Vs Patients')
            plt.legend()
            plt.show()

        if info == "Regular Basis Disease":
            pass

        if info == "Fastest Growing Disease":
            pass


def main():
    app = QApplication(sys.argv)
    h = DiseaseGrowing()
    h.show()
    app.exec_()


if __name__ == '__main__':
    main()


