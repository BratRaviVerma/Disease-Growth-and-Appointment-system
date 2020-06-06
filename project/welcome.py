from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
import sys
import time
from project.login import Mylogin
import pyttsx3 as p


def main():

    app = QApplication(sys.argv)
    pic = QPixmap("login.jpg")
    splash = QSplashScreen(pic)
    splash.showFullScreen()
    font = QtGui.QFont()
    font.setFamily("Monotype Corsiva")
    font.setPointSize(150)
    splash.setFont(font)
    message = "Welcome To YOu"
    splash.showMessage(message, QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter,QtGui.QColor.fromRgb(100, 100, 200,))
    splash.show()
    time.sleep(4)




    engine = p.init()
    print(engine)
    rate = engine.getProperty("rate")
    print(rate)
    engine.setProperty("rate", 100)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say("hii everyone, how r u, welcome to our hospital ")
    engine.runAndWait()
    engine.stop()
    login = Mylogin()
    login.show()
    splash.finish(login)

    app.exec_()


if __name__ == '__main__':
    main()
