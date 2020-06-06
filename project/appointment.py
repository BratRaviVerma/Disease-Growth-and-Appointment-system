from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from project.newrecord import NewRecord
from project.viewrecord import ViewRecord
import sys


class Appointment(QFrame):
    def __init__(self):
        super(Appointment, self).__init__()
        loadUi("Appointment_when_click.ui", self)
        self.btnnewrecord.clicked.connect(lambda: self.buttonclicked(self.btnnewrecord))
        self.btnviewrecord.clicked.connect(lambda: self.buttonclicked(self.btnviewrecord))

    def buttonclicked(self, btn):
        info = btn.text()
        if info == "New Record":
            self.new = NewRecord()
            self.new.show()

        if info == "View Record":
            self.view = ViewRecord()
            self.view.fillTable()
            self.view.show()


def main():
    app = QApplication(sys.argv)
    ap = Appointment()
    ap.show()
    app.exec_()


if __name__ == '__main__':
    main()
