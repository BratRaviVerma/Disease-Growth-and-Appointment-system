from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from project.adddisease import AddDiseaseDetail
from project.viewdisease import ViewDiseaseDetail
import sys


class DiseaseManagement(QFrame):
    def __init__(self):
        super(DiseaseManagement, self).__init__()
        loadUi("Diseasemanage.ui", self)
        self.btnadd.clicked.connect(lambda: self.ButtonClick(self.btnadd))
        self.btnview.clicked.connect(lambda: self.ButtonClick(self.btnview))

    def ButtonClick(self, btn):
        info = btn.text()
        if info == "Add Disease":
            self.new = AddDiseaseDetail()
            self.new.show()

        if info == "View Disease":

            self.view = ViewDiseaseDetail()
            self.view.fillTable()
            self.view.show()


def main():
    app = QApplication(sys.argv)
    ap = DiseaseManagement()
    ap.show()
    app.exec_()


if __name__ == '__main__':
    main()
