from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dboperation.dbconnection import DatabaseConnection as dbc
import sys


class AddDiseaseDetail(QFrame):
    def __init__(self):
        super(AddDiseaseDetail, self).__init__()
        loadUi("Disease_management.ui", self)
        self.con = dbc.createconnection()
        self.btnsubmit.clicked.connect(lambda: self.Add(self.btnsubmit))

    def Add(self, btn):
        info = btn.text()
        if info == "Submit":
            self.id = self.txtdiseaseid.text()
            self.name = self.txtname.text()
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

    def search(self, disid):
        strsql = "select diseaseid from disease where diseaseid=%s"
        disdata = (disid,)
        mycursor = self.con.cursor()
        mycursor.execute(strsql, disdata)
        mycursor.fetchone()
        self.data = mycursor.rowcount
        return self.data

    def insertData(self):
        strinsert = "insert into disease values(%s,%s)"
        dbcursor = self.con.cursor()
        dbcursor.execute(strinsert, (self.id, self.name))
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
    add = AddDiseaseDetail()

    add.show()
    app.exec_()


if __name__ == '__main__':
    main()
