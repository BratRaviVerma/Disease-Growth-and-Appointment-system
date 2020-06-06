import mysql.connector as sqlcon
import matplotlib.pyplot as plt


class Dbkon:
    @staticmethod
    def sqlknkt():
        dbcon = sqlcon.connect(host='localhost', user='root', passwd='root', database='clerk')
        return dbcon


def main():
    con = Dbkon.sqlknkt()
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


if __name__ == '__main__':
    main()
