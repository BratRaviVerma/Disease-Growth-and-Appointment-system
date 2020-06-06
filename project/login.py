from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
from project.home import Home
import secrets
import sys


class Mylogin(QFrame):
    def __init__(self):
        super(Mylogin, self).__init__()
        loadUi("login.ui", self)
        self.btnsubmit.clicked.connect(self.fetchdata)
        img = QtGui.QPixmap("home1.jpg")
        self.txt.setPixmap(img)

    def fetchdata(self):
        self.userid = self.txtuserid.text()


        self.userid = self.userid.strip()
        self.userpass = self.txtuserpass.text()
        if len(self.userid) == 0 or self.userpass == "":
            self.showMessage("Data Validation", "Data Needed")
        else:
            if self.userid == 'ravi' and self.userpass == '123':
                self.admin = Home()
                self.admin.show()
                self.close()

            else:
                self.showMessage("Error", "Invalid User Id/Password")

    def showMessage(self, tt, msg):
            msgbox = QMessageBox()
            msgbox.setWindowTitle(tt)
            msgbox.setText(msg)
            msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            #msgbox.setStandardButtons(QMessageBox.Cancel)
            msgbox.setDefaultButton(QMessageBox.Ok)
            msgbox.setDetailedText("Give Correct Information")
            #msgbox.buttonClicked.connect(self.checkbutton)
            msgbox.show()
            msgbox.exec_()




def main():
    app = QApplication(sys.argv)
    myloginframe = Mylogin()
    myloginframe.show()
    app.exec_()


if __name__ == '__main__':
    main()
