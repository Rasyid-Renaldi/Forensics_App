from PySide6.QtCore import QStringListModel
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QGraphicsDropShadowEffect
import enum
from pytesseract import pytesseract
from PIL import Image

from main_ui import Ui_Aplikasi_Forensik
from splash_screen_ui import Ui_SplashScreen


# * Mendefinisikan kelas enumerasi OS (Operating System) yang memiliki satu anggota yaitu Windows dengan nilai 1
class OS(enum.Enum):
    Windows = 1

# * Mendefinisikan kelas enumerasi Language yang memiliki satu anggota yaitu IND dengan nilai 'ind'


class Language(enum.Enum):
    IND = 'ind'

# * class untuk menampung sinyal, slot dan fungsi yang berinteraksi dengan antarmuka


class Aplikasi_Forensik (QMainWindow, Ui_Aplikasi_Forensik):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.text_file_path = None

        self.detectDevice.currentIndexChanged.connect(self.dialog_connect)
        self.extractButton.clicked.connect(self.start_extract_image)

        self.actionAbout_App.triggered.connect(self.about)
        self.actionAbout_QT.triggered.connect(self.aboutQt)

        self.searchFile.clicked.connect(self.search_button)
        self.browse.clicked.connect(self.save_locations)

        self.scanButton.clicked.connect(self.dialog_scan)
        self.checkButton.clicked.connect(self.check_button)

        self.activity_model = QStringListModel()
        self.viewData.setModel(self.activity_model)

        self.okButton.clicked.connect(self.exit)

    # * Fungsi untuk menampilkan informasi tentang aplikasi
    def about(self):
        QMessageBox.information(
            self, "Aplikasi Forensik", "Aplikasi ini hanya bisa digunakan untuk kepentingan akuisisi data!")

    # * Fungsi untuk menampilkan informasi tentang QT
    def aboutQt(self):
        QApplication.aboutQt()

    # * Menentukan smartphone yang akan digunakan
    def dialog_scan(self):
        scan = QMessageBox.question(
            self, "Scan Smartphone", "Ingin melakukan Scan Handphone Anda ?")
        if scan == QMessageBox.Yes:
            selected_item = self.detectDevice.currentText()
            self.circular = SplashScreen()
            self.circular.progress
            self.circular.progressBarValue

            if selected_item == self.detectDevice.itemText(2):
                self.result.setText("Not Root!")
            else:
                selected_item = self.detectDevice.currentText()
                self.result.setText("Root!")
        else:
            print("No")

    # * Fungsi cek smartphone agar dilakukan scan terlebih dahulu
    def check_button(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Check Smartphone")
        dlg.setText("Silakan lakukan scan Smartphone anda terlebih dahulu !")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setDefaultButton(QMessageBox.No)

        button_clicked = dlg.exec_()
        if button_clicked == QMessageBox.Yes:
            print("Ok")
        else:
            print("No")

    # * Fungsi untuk membuka folder penyimpanan file image
    def search_button(self):
        search = QFileDialog.getOpenFileName(
            self, "Open File", "D:\Skripsi", "JPG files (*.jpg)")
        self.search.setText(search[0])
        self.add_activity("Path gambar: {}".format(search[0]))

    # * Menentukan folder penyimpanan hasil extract file image
    def save_locations(self):
        selected_location = QFileDialog.getSaveFileName(
            self, "Save File", "D:\Skripsi", "TXT files (*.txt)")
        self.browseLocation.setText(selected_location[0])
        self.text_file_path = selected_location[0]
        self.add_activity("Path penyimpanan: {}".format(selected_location[0]))

    # * Fungsi untuk koneksi smartphone dengan aplikasi forensik
    def dialog_connect(self):
        connect = QMessageBox.question(
            self, "Connect Smartphone", "Ingin melakukan Connect perangkat ini ?")
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

    # * Memanggil fungsi extract_image_to_text() dan Menambahkan kegiatan ke dalam model activity_model (keterangan)
    # * Memulai animasi progressBar acquisitionBar dengan menggunakan QPropertyAnimation.
    def start_extract_image(self):
        self.extractButton.setEnabled(False)

        self.add_activity("======= Mengubah gambar menjadi teks =======")
        self.add_activity("Path gambar: {}".format(self.search.text()))
        self.add_activity("Path penyimpanan: {}".format(self.text_file_path))
        self.add_activity("Nama examiner: {}".format(self.lineEdit.text()))
        self.add_activity("Lokasi file output: {}".format(self.text_file_path))

        animation = QPropertyAnimation(self.acquisitionBar, b"value")
        animation.setDuration(3000)
        animation.setStartValue(0)
        animation.setEndValue(100)
        animation.finished.connect(self.extract_image_to_text)
        animation.start()

        self.extract_image_to_text()

    # * Fungsi untuk menambahkan keterangan
    def add_activity(self, activity):
        act = self.activity_model.stringList()
        act.append(activity)
        self.activity_model.setStringList(act)

    # * Berfungsi untuk melakukan proses ekstrak teks dari gambar
    def extract_image_to_text(self):
        image_path = self.search.text()

        if image_path and self.text_file_path:
            image = Image.open(image_path)
            win_path = r'E:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = win_path
            print('Run on: Windows\n')

            extracted_text = pytesseract.image_to_string(image)

            with open(self.text_file_path, "w", encoding="utf-8") as text_file:
                text_file.write(extracted_text)
            QMessageBox.information(
                self, "Ekstraksi Selesai", "Teks berhasil diekstrak dan disimpan dalam file teks"
            )
        else:
            QMessageBox.warning(
                self, "Error", "Mohon pilih file gambar dan lokasi penyimpanan terlebih dahulu!")

        self.extractButton.setEnabled(True)

    # * Fungsi keluar dari aplikasi
    def exit(self):
        self.app.exit()


# GLOBALS
counter = 0
jumper = 10

# ==> SPLASHSCREEN WINDOW


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

    # DEF TO LOADING
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
    # ENG = 'eng'
