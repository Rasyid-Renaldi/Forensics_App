from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

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

        # self.searchFile.triggered.connect(self.search)
      #   self.scanButton.triggered.connect(self.scan)
      #   self.resultLabel

    def quit(self):
        self.app.quit()

    def about(self):
        QMessageBox.information(
            self, "Aplikasi Forensik", "Aplikasi ini hanya bisa digunakan untuk kepentingan akuisisi data!")

    def aboutQt(self):
        QApplication.aboutQt()

    def search_button(self):
        search = QFileDialog.getOpenFileName(
            self, "Open File", "D:\Skripsi", "JPG files (*.jpg) ;; PNG files (*.png)" )
        self.search.setText(search[0])

    def browse_locations(self):
        browse = QFileDialog.getSaveFileName(
            self, "Save File", "D:\Skripsi\Data Raw Evidence")
        self.browseLocation.setText(browse[0])

    # def search_button(self):
    #     fileDialog = QtWidgets.QFileDialog(self)
    #     fileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
    #     fileDialog.setNameFilter("Text files (*.txt);;All files (*.*)")
    #     if fileDialog.exec_():
    #         selected_file = fileDialog.selectedFiles()[0]
    #         print("Selected file:", selected_file)
