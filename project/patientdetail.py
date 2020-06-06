from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dboperation.dbconnection import DatabaseConnection as dbc
import sys


class PatientDetail(QFrame):
    def __init__(self):
        super(PatientDetail, self).__init__()
        loadUi("patientdetail.ui", self)
        self.con = dbc.createconnection()
        self.mycursor = self.con.cursor()
        self.btnsearch.clicked.connect(lambda: self.fetchdata(self.btnsearch))

    def fillTable(self):
        strsql = "select * from patient"
        self.mycursor.execute(strsql)
        dataset = self.mycursor.fetchall()
        rowcount = len(dataset)
        self.tableWidget.setRowCount(rowcount)
        rownum = 0
        for row in dataset:
            for column in range(len(row)):
                print(row[column])
                self.tableWidget.setItem(rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum+1

    def fetchdata(self, btn):

        info = btn.text()
        if info == "SEARCH":
            print("in search")
            self.id = self.txtregistrationid.text()
            print(self.id)
            if len(self.id) == 0:
                self.showMessage("Alert", "Enter Employee ID to be Searched")
            else:
                column = self.search(self.id)
                print(column)
                if column > 0:
                    print("yeah")
                    strsql = "select * from patient where registrationid=%s"
                    patdata = (self.id,)
                    mycursor = self.con.cursor()
                    mycursor.execute(strsql, patdata)
                    dataset = mycursor.fetchall()
                    for row in dataset:
                        name = row[1]
                        age = row[2]
                        gender = row[3]
                        ph = row[4]
                        de = row[5]
                        his = row[6]
                        date = row[7]
                        pro = row[8]


                    self.txtname.setText(name)
                    self.txtage.setText(str(age))
                    self.txtgender.setText(gender)
                    self.txtphone.setText(ph)
                    self.txtdiseaseid.setText(de)
                    self.txthistory.setText(his)
                    self.txtdate.setText(str(date))
                    self.txtproblem.setText(pro)

                else:
                    self.showMessage("Alert", "Employee ID doesn't exist")
    def search(self, patid):
        strsql = "select registrationid from patient where registrationid=%s"
        patdata = (patid,)
        mycursor = self.con.cursor()
        mycursor.execute(strsql, patdata)
        mycursor.fetchone()
        self.data = mycursor.rowcount
        return self.data

    def showMessage(self, tt, msg):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(tt)
        msgbox.setText(msg)
        msgbox.show()
        msgbox.exec_()

def main():
    app = QApplication(sys.argv)
    pd = PatientDetail()
    pd.fillTable()
    pd.show()
    app.exec_()


if __name__ == '__main__':
    main()
