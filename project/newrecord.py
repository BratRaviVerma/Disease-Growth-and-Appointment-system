from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dboperation.dbconnection import DatabaseConnection as dbc
import sys


class NewRecord(QFrame):
    def __init__(self):
        super(NewRecord, self).__init__()
        loadUi("Appont_newrecord.ui", self)
        self.con = dbc.createconnection()
        self.btnsubmit.clicked.connect(lambda: self.Add(self.btnsubmit))

    def Add(self, btn):
        info = btn.text()

        if info == "SUBMIT":
            self.id = self.txtregistrationid.text()
            self.doctor = self.txtdoctorid.text()
            self.date = self.txtappointmentdate.text()
            self.token = self.txttokennumber.text()
            self.Tdate = self.txttodaydate.text()
            self.status = self.txtstatus.text()

            if len(self.id) == 0:
                self.showMessage("Error", "Enter Something")
            else:
                column = self.search(self.id)
                if column < 0:
                    self.showMessage("Alert", "Please Complete Patient Registration")
                else:
                    column1 = self.search1(self.doctor)
                    if column1 < 0:
                        self.showMessage("Alert", "Doctor is Not Present")
                    else:
                        self.insertData()

    def search(self, appid):
        strsql = "select registrationid from patient where registrationid=%s"
        appdata = (appid,)
        mycursor = self.con.cursor()
        mycursor.execute(strsql, appdata)
        mycursor.fetchone()
        self.data = mycursor.rowcount
        return self.data

    def search1(self, appid):
        strsql = "select doctorid from doctor where doctorid=%s"
        appdata = (appid,)
        mycursor = self.con.cursor()
        mycursor.execute(strsql, appdata)
        mycursor.fetchone()
        self.data = mycursor.rowcount
        return self.data

    def insertData(self):
        strinsert = "insert into appointment values(%s,%s,%s,%s,%s,%s)"
        dbcursor = self.con.cursor()
        dbcursor.execute(strinsert, (self.id, self.doctor, self.date, self.token, self.Tdate, self.status))
        self.con.commit()
        self.showMessage("Valid Data", "record added successfully")

    def showMessage(self, tt, msg):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(tt)
        msgbox.setText(msg)
        msgbox.show()
        msgbox.exec_()


def main():
    app = QApplication(sys.argv)
    nr = NewRecord()
    nr.show()
    app.exec_()


if __name__ == '__main__':
    main()
