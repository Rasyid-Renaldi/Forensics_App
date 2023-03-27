from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
                               QLabel, QLineEdit, QListView, QMainWindow,
                               QMenu, QMenuBar, QProgressBar, QPushButton,
                               QRadioButton, QSizePolicy, QStatusBar, QTextBrowser,
                               QToolButton, QWidget)
import rc_resource


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(931, 615)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon = QIcon()
        icon.addFile(u":/images/images/folderIcon.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/quitIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon1)
        self.actionAbout_App = QAction(MainWindow)
        self.actionAbout_App.setObjectName(u"actionAbout_App")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/aboutIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_App.setIcon(icon2)
        self.actionAbout_QT = QAction(MainWindow)
        self.actionAbout_QT.setObjectName(u"actionAbout_QT")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/aboutQtIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_QT.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scanButton = QPushButton(self.centralwidget)
        self.scanButton.setObjectName(u"scanButton")
        self.scanButton.setGeometry(QRect(560, 50, 93, 28))
        self.cekButton = QPushButton(self.centralwidget)
        self.cekButton.setObjectName(u"cekButton")
        self.cekButton.setGeometry(QRect(660, 30, 93, 28))
        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setGeometry(QRect(660, 70, 93, 28))
        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(670, 520, 93, 28))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/checkIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.okButton.setIcon(icon4)
        self.extractButton = QPushButton(self.centralwidget)
        self.extractButton.setObjectName(u"extractButton")
        self.extractButton.setGeometry(QRect(780, 520, 93, 28))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/extractIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.extractButton.setIcon(icon5)
        self.destinationFile = QGroupBox(self.centralwidget)
        self.destinationFile.setObjectName(u"destinationFile")
        self.destinationFile.setGeometry(QRect(210, 110, 601, 181))
        self.fileName = QLabel(self.destinationFile)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setGeometry(QRect(20, 30, 81, 16))
        self.imageType = QLabel(self.destinationFile)
        self.imageType.setObjectName(u"imageType")
        self.imageType.setGeometry(QRect(16, 60, 81, 16))
        self.outputLocation = QLabel(self.destinationFile)
        self.outputLocation.setObjectName(u"outputLocation")
        self.outputLocation.setGeometry(QRect(20, 130, 111, 16))
        self.searchFile = QToolButton(self.destinationFile)
        self.searchFile.setObjectName(u"searchFile")
        self.searchFile.setGeometry(QRect(383, 24, 27, 22))
        self.searchFile.setPopupMode(QToolButton.InstantPopup)
        self.search = QTextBrowser(self.destinationFile)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(109, 20, 261, 31))
        self.raw = QRadioButton(self.destinationFile)
        self.raw.setObjectName(u"raw")
        self.raw.setGeometry(QRect(110, 60, 101, 16))
        self.enCase = QRadioButton(self.destinationFile)
        self.enCase.setObjectName(u"enCase")
        self.enCase.setGeometry(QRect(110, 90, 101, 16))
        self.storage = QLabel(self.destinationFile)
        self.storage.setObjectName(u"storage")
        self.storage.setGeometry(QRect(260, 60, 81, 16))
        self.internal = QCheckBox(self.destinationFile)
        self.internal.setObjectName(u"internal")
        self.internal.setGeometry(QRect(330, 60, 81, 20))
        self.external = QCheckBox(self.destinationFile)
        self.external.setObjectName(u"external")
        self.external.setGeometry(QRect(330, 89, 81, 20))
        self.browseLocation = QLineEdit(self.destinationFile)
        self.browseLocation.setObjectName(u"browseLocation")
        self.browseLocation.setGeometry(QRect(130, 121, 241, 31))
        self.browse = QPushButton(self.destinationFile)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(390, 120, 93, 28))
        self.acquisitionBar = QProgressBar(self.centralwidget)
        self.acquisitionBar.setObjectName(u"acquisitionBar")
        self.acquisitionBar.setGeometry(QRect(370, 310, 241, 23))
        self.acquisitionBar.setValue(50)
        self.acquisitionProgress = QLabel(self.centralwidget)
        self.acquisitionProgress.setObjectName(u"acquisitionProgress")
        self.acquisitionProgress.setGeometry(QRect(220, 310, 131, 16))
        self.detailData = QGroupBox(self.centralwidget)
        self.detailData.setObjectName(u"detailData")
        self.detailData.setGeometry(QRect(220, 360, 401, 151))
        self.viewData = QListView(self.detailData)
        self.viewData.setObjectName(u"viewData")
        self.viewData.setGeometry(QRect(10, 20, 381, 121))
        self.detectDevice = QComboBox(self.centralwidget)
        self.detectDevice.addItem("")
        self.detectDevice.addItem("")
        self.detectDevice.setObjectName(u"detectDevice")
        self.detectDevice.setGeometry(QRect(210, 50, 331, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 931, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout_App)
        self.menuAbout.addAction(self.actionAbout_QT)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.actionSave.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(
            QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionQuit.setText(
            QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout_App.setText(
            QCoreApplication.translate("MainWindow", u"About App", None))
        self.actionAbout_QT.setText(
            QCoreApplication.translate("MainWindow", u"About QT", None))
        self.scanButton.setText(
            QCoreApplication.translate("MainWindow", u"Scan", None))
        self.cekButton.setText(
            QCoreApplication.translate("MainWindow", u"Cek", None))
        self.connectButton.setText(
            QCoreApplication.translate("MainWindow", u"Connect", None))
        self.okButton.setText(
            QCoreApplication.translate("MainWindow", u"Ok", None))
        self.extractButton.setText(
            QCoreApplication.translate("MainWindow", u"Extract", None))
        self.destinationFile.setTitle(QCoreApplication.translate(
            "MainWindow", u"Destination File", None))
        self.fileName.setText(QCoreApplication.translate(
            "MainWindow", u"File Name   :", None))
        self.imageType.setText(QCoreApplication.translate(
            "MainWindow", u"Image Type : ", None))
        self.outputLocation.setText(QCoreApplication.translate(
            "MainWindow", u"Output Location :", None))
        self.searchFile.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.raw.setText(QCoreApplication.translate(
            "MainWindow", u"Raw dd", None))
        self.enCase.setText(QCoreApplication.translate(
            "MainWindow", u"EnCase E01", None))
        self.storage.setText(QCoreApplication.translate(
            "MainWindow", u"Storage : ", None))
        self.internal.setText(QCoreApplication.translate(
            "MainWindow", u"Internal", None))
        self.external.setText(QCoreApplication.translate(
            "MainWindow", u"External", None))
        self.browse.setText(QCoreApplication.translate(
            "MainWindow", u"Browse", None))
        self.acquisitionProgress.setText(QCoreApplication.translate(
            "MainWindow", u"Acquisition Progress :", None))
        self.detailData.setTitle(QCoreApplication.translate(
            "MainWindow", u"Details", None))
        self.detectDevice.setItemText(0, QCoreApplication.translate(
            "MainWindow", u"Redmi Note 4", None))
        self.detectDevice.setItemText(1, QCoreApplication.translate(
            "MainWindow", u"Redmi Note 8", None))

        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(
            QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi
