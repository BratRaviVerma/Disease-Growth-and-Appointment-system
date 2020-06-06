from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dboperation.dbconnection import DatabaseConnection as dbc
import sys


class ViewDiseaseDetail(QFrame):
    def __init__(self):
        super(ViewDiseaseDetail, self).__init__()
        loadUi("viewdisease.ui", self)
        self.con = dbc.createconnection()
        self.mycursor = self.con.cursor()
        self.btnsearch.clicked.connect(lambda: self.fetchdata(self.btnsearch))

    def fillTable(self):
        strsql = "select * from disease"
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
            self.id = self.txtdiseaseid.text()
            print(self.id)
            if len(self.id) == 0:
                self.showMessage("Alert", "Enter Employee ID to be Searched")
            else:
                column = self.search(self.id)
                print(column)
                if column > 0:
                    print("yeah")
                    strsql = "select * from disease where diseaseid=%s"
                    disdata = (self.id,)
                    mycursor = self.con.cursor()
                    mycursor.execute(strsql, disdata)
                    dataset = mycursor.fetchall()
                    for row in dataset:
                        name = row[1]

                    self.txtname.setText(name)


                else:
                    self.showMessage("Alert", "Employee ID doesn't exist")

    def search(self, disid):
        strsql = "select diseaseid from disease where diseaseid=%s"
        disdata = (disid,)
        mycursor = self.con.cursor()
        mycursor.execute(strsql, disdata)
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
    vdd = ViewDiseaseDetail()
    vdd.fillTable()
    vdd.show()
    app.exec_()


if __name__ == '__main__':
    main()
