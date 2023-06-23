# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
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
        Aplikasi_Forensik.resize(897, 486)
        self.actionSave = QAction(Aplikasi_Forensik)
        self.actionSave.setObjectName(u"actionSave")
        icon = QIcon()
        icon.addFile(u":/images/images/folderIcon.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave_As = QAction(Aplikasi_Forensik)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionQuit = QAction(Aplikasi_Forensik)
        self.actionQuit.setObjectName(u"actionQuit")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/quitIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon1)
        self.actionAbout_App = QAction(Aplikasi_Forensik)
        self.actionAbout_App.setObjectName(u"actionAbout_App")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/aboutIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_App.setIcon(icon2)
        self.actionAbout_QT = QAction(Aplikasi_Forensik)
        self.actionAbout_QT.setObjectName(u"actionAbout_QT")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/aboutQtIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_QT.setIcon(icon3)
        self.centralwidget = QWidget(Aplikasi_Forensik)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scanButton = QPushButton(self.centralwidget)
        self.scanButton.setObjectName(u"scanButton")
        self.scanButton.setGeometry(QRect(290, 17, 93, 28))
        self.cekButton = QPushButton(self.centralwidget)
        self.cekButton.setObjectName(u"cekButton")
        self.cekButton.setGeometry(QRect(410, 17, 93, 28))
        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(650, 400, 93, 28))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/checkIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.okButton.setIcon(icon4)
        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setGeometry(QRect(770, 400, 93, 28))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/extractIcon.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.convertButton.setIcon(icon5)
        self.Input = QGroupBox(self.centralwidget)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(30, 100, 401, 221))
        self.fileName = QLabel(self.Input)
        self.fileName.setObjectName(u"fileName")
        self.fileName.setGeometry(QRect(40, 42, 81, 16))
        self.search = QLineEdit(self.Input)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(130, 35, 171, 31))
        self.searchFile = QToolButton(self.Input)
        self.searchFile.setObjectName(u"searchFile")
        self.searchFile.setGeometry(QRect(320, 45, 27, 22))
        self.searchFile.setPopupMode(QToolButton.InstantPopup)
        self.examiner = QLabel(self.Input)
        self.examiner.setObjectName(u"examiner")
        self.examiner.setGeometry(QRect(40, 80, 81, 16))
        self.lineEdit = QLineEdit(self.Input)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 75, 171, 31))
        self.outputLocation = QLabel(self.Input)
        self.outputLocation.setObjectName(u"outputLocation")
        self.outputLocation.setGeometry(QRect(15, 120, 111, 16))
        self.browseLocation = QLineEdit(self.Input)
        self.browseLocation.setObjectName(u"browseLocation")
        self.browseLocation.setGeometry(QRect(130, 114, 171, 31))
        self.browse = QPushButton(self.Input)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(310, 117, 81, 28))
        self.acquisitionBar = QProgressBar(self.centralwidget)
        self.acquisitionBar.setObjectName(u"acquisitionBar")
        self.acquisitionBar.setGeometry(QRect(390, 350, 251, 23))
        self.acquisitionBar.setValue(0)
        self.acquisitionProgress = QLabel(self.centralwidget)
        self.acquisitionProgress.setObjectName(u"acquisitionProgress")
        self.acquisitionProgress.setGeometry(QRect(244, 353, 141, 16))
        self.detectDevice = QComboBox(self.centralwidget)
        self.detectDevice.addItem("")
        self.detectDevice.addItem("")
        self.detectDevice.addItem("")
        self.detectDevice.setObjectName(u"detectDevice")
        self.detectDevice.setGeometry(QRect(30, 20, 241, 22))
        self.detectDevice.setEditable(False)
        self.resultCek = QLabel(self.centralwidget)
        self.resultCek.setObjectName(u"resultCek")
        self.resultCek.setGeometry(QRect(30, 54, 55, 16))
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(93, 55, 61, 16))
        self.destinationFile_2 = QGroupBox(self.centralwidget)
        self.destinationFile_2.setObjectName(u"destinationFile_2")
        self.destinationFile_2.setGeometry(QRect(460, 100, 421, 221))
        self.imageType = QLabel(self.destinationFile_2)
        self.imageType.setObjectName(u"imageType")
        self.imageType.setGeometry(QRect(50, 30, 151, 20))
        self.text = QRadioButton(self.destinationFile_2)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(203, 33, 51, 16))
        self.internal = QCheckBox(self.destinationFile_2)
        self.internal.setObjectName(u"internal")
        self.internal.setGeometry(QRect(271, 31, 61, 20))
        self.detailData = QGroupBox(self.destinationFile_2)
        self.detailData.setObjectName(u"detailData")
        self.detailData.setGeometry(QRect(40, 63, 371, 141))
        self.viewData = QListView(self.detailData)
        self.viewData.setObjectName(u"viewData")
        self.viewData.setGeometry(QRect(11, 20, 351, 111))
        Aplikasi_Forensik.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Aplikasi_Forensik)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 897, 26))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        Aplikasi_Forensik.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Aplikasi_Forensik)
        self.statusbar.setObjectName(u"statusbar")
        Aplikasi_Forensik.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionAbout_App)
        self.menuAbout.addAction(self.actionAbout_QT)

        self.retranslateUi(Aplikasi_Forensik)

        QMetaObject.connectSlotsByName(Aplikasi_Forensik)
    # setupUi

    def retranslateUi(self, Aplikasi_Forensik):
        Aplikasi_Forensik.setWindowTitle(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Aplikasi_Forensik", None))
        self.actionSave.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Save As", None))
        self.actionQuit.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Quit", None))
        self.actionAbout_App.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"About App", None))
        self.actionAbout_QT.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"About QT", None))
        self.scanButton.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Scan", None))
        self.cekButton.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Check", None))
        self.okButton.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Oke", None))
        self.convertButton.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Extract", None))
        self.Input.setTitle(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Input", None))
        self.fileName.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"File Name   :", None))
        self.searchFile.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"...", None))
        self.examiner.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Examiner    :", None))
        self.outputLocation.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Output Location :", None))
        self.browse.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Browse", None))
        self.acquisitionProgress.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Acquisition Progress    :", None))
        self.detectDevice.setItemText(0, QCoreApplication.translate(
            "Aplikasi_Forensik", u"Redmi Note 4", None))
        self.detectDevice.setItemText(1, QCoreApplication.translate(
            "Aplikasi_Forensik", u"Samsung Galaxy J1 Ace", None))
        self.detectDevice.setItemText(2, QCoreApplication.translate(
            "Aplikasi_Forensik", u"Redmi Note 8", None))

        self.resultCek.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Result :", None))
        self.result.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Not Root!", None))
        self.destinationFile_2.setTitle(
            QCoreApplication.translate("Aplikasi_Forensik", u"Output", None))
        self.imageType.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"File Type and Storage  : ", None))
        self.text.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u".txt", None))
        self.internal.setText(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Local", None))
        self.detailData.setTitle(QCoreApplication.translate(
            "Aplikasi_Forensik", u"Details", None))
        self.menuAbout.setTitle(QCoreApplication.translate(
            "Aplikasi_Forensik", u"About", None))
    # retranslateUi
