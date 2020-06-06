from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dboperation.dbconnection import DatabaseConnection as dbc
import sys


class AddDoctorDetail(QFrame):
    def __init__(self):
        super(AddDoctorDetail, self).__init__()
        loadUi("adddoctordetail.ui", self)
        self.con = dbc.createconnection()
        self.btnsubmit.clicked.connect(lambda: self.Add(self.btnsubmit))

    def Add(self, btn):
        info = btn.text()
        if info == "SUBMIT":
            self.id = self.txtdoctorid.text()
            self.name = self.txtname.text()
            self.address = self.txtaddress.text()
            self.email = self.txtemail.text()
            self.phone = self.txtphonenumber.text()
            self.days = self.txtdays.text()
            self.timing = self.txttiming.text()
            self.experience = self.txtexperience.text()
            self.special = self.txtspecial.text()

            if len(self.id) == 0:
                self.showMessage("Error", "Enter Something")
            else:
                row = self.search(self.id)
                print(row)
                if row > 0:
                    self.showMessage("Valid Data", "id already exist")
                    print("id i ")
                else:
                    self.insertData()

    def search(self, docid):
        strsql = "select doctorid from doctor where doctorid=%s"
        docdata = (docid,)
        mycursor = self.con.cursor()
        mycursor.execute(strsql, docdata)
        mycursor.fetchone()
        self.data = mycursor.rowcount
        return self.data

    def insertData(self):
        strinsert = "insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dbcursor = self.con.cursor()
        dbcursor.execute(strinsert, (self.id, self.name, self.address, self.email, self.phone, self.days, self.timing, self.experience, self.special))
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
    add = AddDoctorDetail()

    add.show()
    app.exec_()


if __name__ == '__main__':
    main()
