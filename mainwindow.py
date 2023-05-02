from PySide6.QtCore import Qt
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLabel, QGraphicsDropShadowEffect

from ui_main import Ui_MainWindow
from splash_screen_ui import Ui_SplashScreen


class MainWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.actionQuit.triggered.connect(self.quit)
        self.actionAbout_App.triggered.connect(self.about)
        self.actionAbout_QT.triggered.connect(self.aboutQt)

        self.searchFile.clicked.connect(self.search_button)
        self.browse.clicked.connect(self.browse_locations)

        self.scanButton.clicked.connect(self.dialog_scan)
        self.connectButton.clicked.connect(self.dialog_connect)
        self.cekButton.clicked.connect(self.clicked)
        
        self.okButton.clicked.connect(self.exit)
        # self.extractButton.clicked.connect(self.extract)

    def quit(self):
        self.app.quit()

    def about(self):
        QMessageBox.information(
            self, "Aplikasi Forensik", "Aplikasi ini hanya bisa digunakan untuk kepentingan akuisisi data!")

    def aboutQt(self):
        QApplication.aboutQt()

    def search_button(self):
        search = QFileDialog.getOpenFileName(
            self, "Open File", "D:\Skripsi", "JPG files (*.jpg) ;; PNG files (*.png)")
        self.search.setText(search[0])

    def browse_locations(self):
        browse = QFileDialog.getSaveFileName(
            self, "Save File", "D:\Skripsi\Data Raw Evidence")
        self.browseLocation.setText(browse[0])

    def dialog_scan(self):
        scan = QMessageBox.question(
            self, "Scan Button", "Yakin ingin melakukan Scan Handphone Anda!!")
        if scan == QMessageBox.Yes:
            # message = QtWidgets.QLabel(self)
            # self.message.setText('Anda Berhasil Terhubung..')
            self.circular_progress = SplashScreen()
            self.circular_progress.progress
            self.circular_progress.progressBarValue
            # print("Yes")
        else:
            # self.message.setText('Anda Belum Terhubung..')
            print("No")

    def dialog_connect(self):
        connect = QMessageBox.question(
            self, "Connect Button", "Yakin ingin melakukan Connect Handphone Anda!!")
        if connect == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")

    def cek_button(self):
        self.result = QtWidgets.QLabel(self)
        self.result.setText("Not Root!")

    def clicked(self):
        self.result.setText("Root!")

    def exit(self):
        self.app.exit()

    # def extract(self):

# GLOBALS
counter = 0
jumper = 10

## ==> SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(20)

        ## SHOW ==> MAIN WINDOW
        ########################
        self.show()
        ## ==> END ##

    ## DEF TO LOANDING
    ####################
    def progress (self):
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
        if value >= 100: value = 1.000
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

    ## DEF PROGRESS BAR VALUE
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
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)