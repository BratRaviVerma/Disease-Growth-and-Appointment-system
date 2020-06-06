from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dboperation.dbconnection import DatabaseConnection as dbc
import sys


class ViewRecord(QFrame):
    def __init__(self):
        super(ViewRecord, self).__init__()
        loadUi("appointment_update.ui", self)
        self.con = dbc.createconnection()
        self.mycursor = self.con.cursor()
        self.btnsearch.clicked.connect(lambda: self.fetchdata(self.btnsearch))


    def fillTable(self):
        strsql = "select * from appointment"
        self.mycursor.execute(strsql)
        dataset = self.mycursor.fetchall()
        rowcount = len(dataset)
        self.tblview.setRowCount(rowcount)
        rownum = 0
        for row in dataset:
            for column in range(len(row)):
                print(row[column])
                self.tblview.setItem(rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum+1

    def fetchdata(self, btn):

        info = btn.text()
        if info == "SEARCH":
            print("in search")
            self.id = self.txtregistrationid.text()
            print(self.id)
            if len(self.id) == 0:
                self.showMessage("Alert", "Enter Registration ID to be Searched")
            else:
                column = self.search(self.id)
                print(column)
                if column > 0:
                    print("yeah")
                    strsql = "select * from appointment where registrationid=%s"
                    appdata = (self.id,)
                    mycursor = self.con.cursor()
                    mycursor.execute(strsql, appdata)
                    dataset = mycursor.fetchall()
                    for row in dataset:
                        doc = row[1]
                        appo = row[2]
                        Tn = row[3]
                        Td = row[4]
                        sta = row[5]
                    self.txtdoctorid.setText(doc)
                    self.txtappo.setText(appo)
                    self.txttokennumber.setText(Tn)
                    self.txttodaydate.setText(Td)
                    self.txtstatus.setText(sta)
                else:
                    self.showMessage("Alert", "Employee ID doesn't exist")

    def search(self, regid):
        strsql = "select registrationid from appointment where registrationid=%s"
        regdata = (regid,)
        mycursor = self.con.cursor()
        mycursor.execute(strsql, regdata)
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
    vr = ViewRecord()
    vr.fillTable()
    vr.show()
    app.exec_()


if __name__ == '__main__':
    main()
