from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLabel

from ui_main import Ui_MainWindow


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
            print("Yes")
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