from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from project.adddoctordetail import AddDoctorDetail
from project.viewdoctordetail import ViewDoctorDetail
import sys


class DoctorDetail(QFrame):
    def __init__(self):
        super(DoctorDetail, self).__init__()
        loadUi("ddoctordetail.ui", self)
        self.btnadd.clicked.connect(lambda: self.pushbutton(self.btnadd))
        self.btnview.clicked.connect(lambda: self.pushbutton(self.btnview))

    def pushbutton(self, btn):
        info = btn.text()
        if info == "ADD DOCTOR DETAIL":
            self.add = AddDoctorDetail()
            self.add.show()


        if info == "VIEW DOCTOR DETAIL":
            self.view = ViewDoctorDetail()
            self.view.fillTable()
            self.view.show()


def main():
    app = QApplication(sys.argv)
    dd = DoctorDetail()
    dd.show()
    app.exec_()


if __name__ == '__main__':
    main()
