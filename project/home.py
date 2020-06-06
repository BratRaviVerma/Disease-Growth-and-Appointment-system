from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from project.appointment import Appointment
from project.doctordetail import DoctorDetail
from project.patientdetail import PatientDetail
from project.diseasemanage import DiseaseManagement
from project.diseasegrowth import DiseaseGrowing
import sys


class Home(QFrame):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("Home.ui", self)
        self.btnappo.clicked.connect(lambda: self.buttonclicked(self.btnappo))
        self.btndoctordetail.clicked.connect(lambda: self.buttonclicked(self.btndoctordetail))
        self.btnpatientdetail.clicked.connect(lambda: self.buttonclicked(self.btnpatientdetail))
        self.btndiseasemanagement.clicked.connect(lambda: self.buttonclicked(self.btndiseasemanagement))
        self.btndiseasegrowth.clicked.connect(lambda: self.buttonclicked(self.btndiseasegrowth))

    def buttonclicked(self, btn):
        info = btn.text()
        if info == "APPOINTMENT":
            self.appo = Appointment()
            self.appo.show()

        if info == "DOCTOR DETAIL":
            self.dd = DoctorDetail()
            self.dd.show()

        if info == "PATIENT MANAGEMENT":
            self.pd = PatientDetail()
            self.pd.fillTable()
            self.pd.show()

        if info == "DISEASE MANAGEMENT":
            self.d = DiseaseManagement()
            self.d.show()

        if info == "DISEASE GROWTH":
            self.dg = DiseaseGrowing()
            self.dg.show()


def main():
    app = QApplication(sys.argv)
    h = Home()
    h.show()
    app.exec_()


if __name__ == '__main__':
    main()


