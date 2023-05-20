from PySide6.QtCore import Qt
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLabel, QGraphicsDropShadowEffect, QProgressBar, QComboBox
import time
import os
import pandas as pd

from main_ui import Ui_Aplikasi_Forensik
from splash_screen_ui import Ui_SplashScreen


class Aplikasi_Forensik (QMainWindow, Ui_Aplikasi_Forensik):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.detectDevice.currentIndexChanged.connect(self.dialog_connect)

        self.actionQuit.triggered.connect(self.quit)
        self.actionAbout_App.triggered.connect(self.about)
        self.actionAbout_QT.triggered.connect(self.aboutQt)

        self.searchFile.clicked.connect(self.search_button)
        self.browse.clicked.connect(self.save_locations)

        self.scanButton.clicked.connect(self.dialog_scan)
        self.cekButton.clicked.connect(self.cek_button)

        self.okButton.clicked.connect(self.exit)
        self.convertButton.clicked.connect(self.start)

    def start(self):
        for i in range(101):
            self.acquisitionBar.setValue(i)
            time.sleep(0.03)

    def quit(self):
        self.app.quit()

    def about(self):
        QMessageBox.information(
            self, "Aplikasi Forensik", "Aplikasi ini hanya bisa digunakan untuk kepentingan akuisisi data!")

    def aboutQt(self):
        QApplication.aboutQt()

    def search_button(self):
        search = QFileDialog.getOpenFileName(
            self, "Open File", "D:\Skripsi", "XLSX files (*.xlsx)")
        self.search.setText(search[0])

    def save_locations(self):
        browse = QFileDialog.getSaveFileName(
            self, "Save File", "D:\Skripsi\Data Raw Evidence")
        self.browseLocation.setText(browse[0])

    def dialog_scan(self):
        scan = QMessageBox.question(
            self, "Scan Button", "Ingin melakukan Scan Handphone Anda ?")
        if scan == QMessageBox.Yes:
            self.circular = SplashScreen()
            self.circular.progress
            self.circular.progressBarValue
            self.result.setText("Root!")
        else:
            print("No")

    def dialog_connect(self):
        connect = QMessageBox.question(
            self, "Connect Button", "Ingin melakukan Connect perangkat ini ?")
        self.result.setText("Not Root!")
        if connect == QMessageBox.Yes:
            selected_item = self.detectDevice.currentText()
            print(selected_item)
            dlg = QMessageBox(self)
            dlg.setText('Berhasil terkoneksi dengan perangkat')
            btn = dlg.exec_()
            if btn == QMessageBox.Ok:
                print('OK')
        else:
            print("No")

    def cek_button(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Cek Button")
        dlg.setText("Silakan lakukan scan handphone anda terlebih dahulu !")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setDefaultButton(QMessageBox.No)

        button_clicked = dlg.exec_()
        if button_clicked == QMessageBox.Yes:
            print("Ok")
        else:
            self.result.setText("Not Root!")

    def exit(self):
        self.app.exit()


# GLOBALS
counter = 0
jumper = 10

# ==> SPLASHSCREEN WINDOW

# untuk kebutuhan pada saat demo ketika sidang nanti
# if selected_item == self.result.setText("Root"):
            #     print("Telah root")

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        # ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        # Set background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(20)

        # SHOW ==> MAIN WINDOW
        ########################
        self.show()
        ## ==> END ##

    # DEF TO LOANDING
    ####################
    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100:
            value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 101:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            # self.main = MainWindow()
            # self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

    # DEF PROGRESS BAR VALUE
    #########################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)
