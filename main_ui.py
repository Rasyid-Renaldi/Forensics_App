# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
    QRadioButton, QSizePolicy, QStatusBar, QToolButton,
    QWidget)
import resource_rc

class Ui_Aplikasi_Forensik(object):
    def setupUi(self, Aplikasi_Forensik):
        if not Aplikasi_Forensik.objectName():
            Aplikasi_Forensik.setObjectName(u"Aplikasi_Forensik")
        Aplikasi_Forensik.resize(931, 615)
        self.actionSave = QAction(Aplikasi_Forensik)
        self.actionSave.setObjectName(u"actionSave")
        icon = QIcon()
        icon.addFile(u":/images/images/folderIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave_As = QAction(Aplikasi_Forensik)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionQuit = QAction(Aplikasi_Forensik)
        self.actionQuit.setObjectName(u"actionQuit")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/quitIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon1)
        self.actionAbout_App = QAction(Aplikasi_Forensik)
        self.actionAbout_App.setObjectName(u"actionAbout_App")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/aboutIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_App.setIcon(icon2)
        self.actionAbout_QT = QAction(Aplikasi_Forensik)
        self.actionAbout_QT.setObjectName(u"actionAbout_QT")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/aboutQtIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_QT.setIcon(icon3)
        self.centralwidget = QWidget(Aplikasi_Forensik)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scanButton = QPushButton(self.centralwidget)
        self.scanButton.setObjectName(u"scanButton")
        self.scanButton.setGeometry(QRect(560, 20, 93, 28))
        self.cekButton = QPushButton(self.centralwidget)
        self.cekButton.setObjectName(u"cekButton")
        self.cekButton.setGeometry(QRect(660, 20, 93, 28))
        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(670, 520, 93, 28))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/checkIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.okButton.setIcon(icon4)
        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setGeometry(QRect(780, 520, 93, 28))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/extractIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.convertButton.setIcon(icon5)
        self.destinationFile = QGroupBox(self.centralwidget)
        self.destinationFile.setObjectName(u"destinationFile")
        self.destinationFile.setGeometry(QRect(220, 80, 511, 201))
        self.fileName = QLabel(self.destinationFile)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setGeometry(QRect(20, 30, 81, 16))
        self.imageType = QLabel(self.destinationFile)
        self.imageType.setObjectName(u"imageType")
        self.imageType.setGeometry(QRect(20, 60, 81, 16))
        self.outputLocation = QLabel(self.destinationFile)
        self.outputLocation.setObjectName(u"outputLocation")
        self.outputLocation.setGeometry(QRect(10, 150, 111, 16))
        self.searchFile = QToolButton(self.destinationFile)
        self.searchFile.setObjectName(u"searchFile")
        self.searchFile.setGeometry(QRect(383, 24, 27, 22))
        self.searchFile.setPopupMode(QToolButton.InstantPopup)
        self.raw = QRadioButton(self.destinationFile)
        self.raw.setObjectName(u"raw")
        self.raw.setGeometry(QRect(110, 60, 101, 16))
        self.storage = QLabel(self.destinationFile)
        self.storage.setObjectName(u"storage")
        self.storage.setGeometry(QRect(260, 60, 81, 16))
        self.internal = QCheckBox(self.destinationFile)
        self.internal.setObjectName(u"internal")
        self.internal.setGeometry(QRect(330, 60, 71, 16))
        self.external = QCheckBox(self.destinationFile)
        self.external.setObjectName(u"external")
        self.external.setGeometry(QRect(330, 80, 81, 16))
        self.browseLocation = QLineEdit(self.destinationFile)
        self.browseLocation.setObjectName(u"browseLocation")
        self.browseLocation.setGeometry(QRect(120, 140, 241, 31))
        self.browse = QPushButton(self.destinationFile)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(400, 160, 93, 28))
        self.examiner = QLabel(self.destinationFile)
        self.examiner.setObjectName(u"examiner")
        self.examiner.setGeometry(QRect(20, 100, 81, 16))
        self.lineEdit = QLineEdit(self.destinationFile)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 100, 241, 31))
        self.search = QLineEdit(self.destinationFile)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(120, 20, 241, 31))
        self.acquisitionBar = QProgressBar(self.centralwidget)
        self.acquisitionBar.setObjectName(u"acquisitionBar")
        self.acquisitionBar.setGeometry(QRect(390, 310, 241, 23))
        self.acquisitionBar.setValue(0)
        self.acquisitionProgress = QLabel(self.centralwidget)
        self.acquisitionProgress.setObjectName(u"acquisitionProgress")
        self.acquisitionProgress.setGeometry(QRect(220, 310, 131, 16))
        self.detailData = QGroupBox(self.centralwidget)
        self.detailData.setObjectName(u"detailData")
        self.detailData.setGeometry(QRect(210, 380, 401, 171))
        self.viewData = QListView(self.detailData)
        self.viewData.setObjectName(u"viewData")
        self.viewData.setGeometry(QRect(10, 20, 381, 141))
        self.detectDevice = QComboBox(self.centralwidget)
        self.detectDevice.addItem("")
        self.detectDevice.addItem("")
        self.detectDevice.setObjectName(u"detectDevice")
        self.detectDevice.setGeometry(QRect(220, 20, 331, 22))
        self.detectDevice.setEditable(False)
        self.resultCek = QLabel(self.centralwidget)
        self.resultCek.setObjectName(u"resultCek")
        self.resultCek.setGeometry(QRect(220, 50, 55, 16))
        self.acquisitionBar_2 = QProgressBar(self.centralwidget)
        self.acquisitionBar_2.setObjectName(u"acquisitionBar_2")
        self.acquisitionBar_2.setGeometry(QRect(390, 340, 241, 23))
        self.acquisitionBar_2.setValue(0)
        self.Int = QLabel(self.centralwidget)
        self.Int.setObjectName(u"Int")
        self.Int.setGeometry(QRect(350, 310, 31, 16))
        self.Ext = QLabel(self.centralwidget)
        self.Ext.setObjectName(u"Ext")
        self.Ext.setGeometry(QRect(350, 340, 31, 16))
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(280, 50, 81, 16))
        Aplikasi_Forensik.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Aplikasi_Forensik)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 931, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        Aplikasi_Forensik.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Aplikasi_Forensik)
        self.statusbar.setObjectName(u"statusbar")
        Aplikasi_Forensik.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout_App)
        self.menuAbout.addAction(self.actionAbout_QT)

        self.retranslateUi(Aplikasi_Forensik)

        QMetaObject.connectSlotsByName(Aplikasi_Forensik)
    # setupUi

    def retranslateUi(self, Aplikasi_Forensik):
        Aplikasi_Forensik.setWindowTitle(QCoreApplication.translate("Aplikasi_Forensik", u"Aplikasi_Forensik", None))
        self.actionSave.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Save As", None))
        self.actionQuit.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Quit", None))
        self.actionAbout_App.setText(QCoreApplication.translate("Aplikasi_Forensik", u"About App", None))
        self.actionAbout_QT.setText(QCoreApplication.translate("Aplikasi_Forensik", u"About QT", None))
        self.scanButton.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Scan", None))
        self.cekButton.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Cek", None))
        self.okButton.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Ok", None))
        self.convertButton.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Convert", None))
        self.destinationFile.setTitle(QCoreApplication.translate("Aplikasi_Forensik", u"Destination File", None))
        self.fileName.setText(QCoreApplication.translate("Aplikasi_Forensik", u"File Name   :", None))
        self.imageType.setText(QCoreApplication.translate("Aplikasi_Forensik", u"File Type    : ", None))
        self.outputLocation.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Output Location :", None))
        self.searchFile.setText(QCoreApplication.translate("Aplikasi_Forensik", u"...", None))
        self.raw.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Text", None))
        self.storage.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Storage : ", None))
        self.internal.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Internal", None))
        self.external.setText(QCoreApplication.translate("Aplikasi_Forensik", u"External", None))
        self.browse.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Browse", None))
        self.examiner.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Examiner    :", None))
        self.acquisitionProgress.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Acquisition Progress :", None))
        self.detailData.setTitle(QCoreApplication.translate("Aplikasi_Forensik", u"Details", None))
        self.detectDevice.setItemText(0, QCoreApplication.translate("Aplikasi_Forensik", u"Redmi Note 4", None))
        self.detectDevice.setItemText(1, QCoreApplication.translate("Aplikasi_Forensik", u"Samsung A10", None))

        self.resultCek.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Result :", None))
        self.Int.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Int :", None))
        self.Ext.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Ext :", None))
        self.result.setText(QCoreApplication.translate("Aplikasi_Forensik", u"Not Root!", None))
        self.menuFile.setTitle(QCoreApplication.translate("Aplikasi_Forensik", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("Aplikasi_Forensik", u"About", None))
    # retranslateUi

