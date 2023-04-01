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

# import PySide6.QtCore as QtCore
# import PySide6.QtGui as QtGui
# import PySide6.QtWidgets as QtWidgets

# class ScanDevice(QtWidgets.QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
 
#         # UI setup
#         layout = QtWidgets.QVBoxLayout(self)
#         self.textbox = QtWidgets.QLineEdit(self)
#         self.textbox.setPlaceholderText('Insert device name')
#         layout.addWidget(self.textbox)
#         button = QtWidgets.QPushButton('Scan', self)
#         button.clicked.connect(self.scan_device)
#         layout.addWidget(button)
 
#     def scan_device(self):
#         device_name = self.textbox.text()
 
#         # Scan for device
#         device_found = False
#         devices = QtCore.QBluetoothDeviceDiscoveryAgent()
#         devices.deviceDiscovered.connect(lambda device: self.device_discovered(device, device_name))
#         devices.start()
#         devices.finished.connect(self.scan_finished)
 
#         # Show scanning progress
#         self.progress = QtWidgets.QProgressBar(self)
#         self.progress.setRange(0, 0)
#         self.progress.setValue(0)
#         self.progress.show()
 
#     def device_discovered(self, device_info, device_name):
#         if device_info.name() == device_name:
#             self.progress.close()
#             self.textbox.clear()
#             QtWidgets.QMessageBox.information(self, 'Device Found', f'{device_name} found at {device_info.address().toString()}')
#             self.accept()
 
#     def scan_finished(self):
#         self.progress.close()
#         QtWidgets.QMessageBox.warning(self, 'Error', 'Device not found')
#         self.reject()
