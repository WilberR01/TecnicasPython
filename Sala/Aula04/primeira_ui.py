# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'primeira.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1063, 665)
        MainWindow.setCursor(QCursor(Qt.OpenHandCursor))
        MainWindow.setStyleSheet(u"background-color: rgb(130, 130, 194);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logar = QPushButton(self.centralwidget)
        self.logar.setObjectName(u"logar")
        self.logar.setGeometry(QRect(540, 180, 141, 41))
        self.logar.setCursor(QCursor(Qt.OpenHandCursor))
        self.logar.setStyleSheet(u"background-color: rgb(148, 101, 176);\n"
"font: 18pt \"Leelawadee UI Semilight\";\n"
"padding-bottom: 2px;\n"
"border-radius: 10px;")
        self.login = QLineEdit(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(350, 160, 151, 31))
        self.login.setStyleSheet(u"background-color: rgb(249,241,241);\n"
"margin: 1px;\n"
"border: 2px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 350, 93, 28))
        self.pushButton.setStyleSheet(u"background-color: rgb(249,241,241);\n"
"font: 8pt \"Leelawadee UI Semilight\";\n"
"padding-bottom: 2px;\n"
"border-radius: 10px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(470, 320, 121, 21))
        self.label.setStyleSheet(u"background-color: rgb(130, 121, 176);\n"
"border-radius: 6px;\n"
"padding: 4px;")
        self.senha = QLineEdit(self.centralwidget)
        self.senha.setObjectName(u"senha")
        self.senha.setGeometry(QRect(350, 210, 151, 31))
        self.senha.setStyleSheet(u"background-color: rgb(249,241,241);\n"
"margin: 1px;\n"
"border: 2px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.erro = QLabel(self.centralwidget)
        self.erro.setObjectName(u"erro")
        self.erro.setGeometry(QRect(480, 250, 101, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1063, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logar.setText(QCoreApplication.translate("MainWindow", u"LOGAR", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastre-se", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o \u00e9 cadastrado?", None))
        self.erro.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

