from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import boj

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

class MainWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(640, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 100, 40))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 30, 640, 130))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(128)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 160, 640, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(230, 200, 180, 30))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsddjd = QtWidgets.QAction(MainWindow)
        self.actionsddjd.setObjectName("actionsddjd")
        self.actionvdmns = QtWidgets.QAction(MainWindow)
        self.actionvdmns.setObjectName("actionvdmns")

        self.retranslateUI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BOJ.GG"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.label.setText(_translate("MainWindow", "BOJ.GG"))
        self.label_2.setText(_translate("MainWindow", "Beakjoon Online Judge 전적검색 프로그램"))
        self.actionsddjd.setText(_translate("MainWindow", "sddjd"))
        self.actionvdmns.setText(_translate("MainWindow", "vdmns"))


class UserInfoWindow(object):
    def setupUI(self, MainWindow, userID):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 640)

        self.userID = userID

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.statusTable = QtWidgets.QTableWidget(self.centralwidget)
        self.statusTable.setGeometry(QtCore.QRect(220, 40, 611, 331))
        self.statusTable.setShowGrid(False)
        self.statusTable.setObjectName("statusTable")

        self.statusTableTitle = ["문제 번호", "문제 이름", "결과", "메모리", "시간", "언어", "코드 길이", "제출한 시간"]
        self.statusTable.setColumnCount(len(self.statusTableTitle))
        for i in range(len(self.statusTableTitle)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("MainWindow", self.statusTableTitle[i]))
            self.statusTable.setHorizontalHeaderItem(i, item)
        self.statusTable.setSortingEnabled(False)
        self.statusTable.verticalHeader().setVisible(False)

        self.infoTable = QtWidgets.QTableWidget(self.centralwidget)
        self.infoTable.setGeometry(QtCore.QRect(10, 40, 201, 331))
        self.infoTable.setShowGrid(False)
        self.infoTable.setObjectName("infoTable")
        self.infoTable.setColumnCount(2)
        self.infoTable.setRowCount(12)
        for i in range(self.infoTable.rowCount()):
            for j in range(self.infoTable.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                self.infoTable.setItem(i, j, item)
        self.infoTable.horizontalHeader().setVisible(False)
        self.infoTable.verticalHeader().setVisible(False)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 380, 821, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.figure = plt.figure()
        self.graphView = FigureCanvas(self.figure)
        self.verticalLayout.addWidget(self.graphView)

        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(740, 580, 50, 50))
        self.refreshButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/1024px-OOjs_UI_icon_reload.svg.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon)
        self.refreshButton.setIconSize(QtCore.QSize(32, 32))
        self.refreshButton.setObjectName("refreshButton")

        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.infoLabel.setObjectName("infoLabel")

        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(220, 10, 101, 21))
        self.statusLabel.setObjectName("statusLabel")

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(780, 580, 50, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/close-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon1)
        self.exitButton.setIconSize(QtCore.QSize(32, 32))
        self.exitButton.setObjectName("exitButton")
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setWindowTitle(_translate("MainWindow", "BOJ.GG"))
        self.infoLabel.setText(_translate("MainWindow", self.userID + " 정보"))
        self.statusLabel.setText(_translate("MainWindow", "채점 현황"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setupUserInfo(MainWindow)
        self.setupStatus(MainWindow)
        self.setupGraph(MainWindow)


    def setupUserInfo(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.infoTable.isSortingEnabled()
        self.infoTable.setSortingEnabled(False)
        data = boj.getUserInfo(self.userID)
        for i in range(len(data)):
            for j in range(len(data[i])):
                item = self.infoTable.item(i, j)
                item.setText(_translate("MainWindow", data[i][j]))
        self.infoTable.setSortingEnabled(__sortingEnabled)

    def setupStatus(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.statusTable.isSortingEnabled()
        data = boj.getStatus(self.userID)
        self.statusTable.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(data[i])):
                item = QtWidgets.QTableWidgetItem()

                if j == 2:
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                    brush.setStyle(QtCore.Qt.NoBrush)
                    item.setBackground(brush)
                    if data[i][j] == "맞았습니다!!":
                        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                    else:
                        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                    brush.setStyle(QtCore.Qt.NoBrush)
                    item.setForeground(brush)

                item.setText(_translate("MainWindow", data[i][j]))
                self.statusTable.setItem(i, j, item)
        self.statusTable.setSortingEnabled(__sortingEnabled)

    def setupGraph(self, MainWindow):
        data = boj.getAcceptedData(self.userID)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # ax.bar(reversed(list(data.keys())), reversed(list(data.values())), color='g')
        ax.bar(list(reversed(list(data.keys()))), list(reversed(list(data.values()))), color='g')
        # ax.hist(list(data.keys()), data.values())
        self.graphView.draw()

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.mainWindow = MainWindow()
        self.userInfoWindow = UserInfoWindow()
        self.startMainWindow()
        # self.startUserInfoWindow('sunjbs98')

    def startMainWindow(self):
        self.mainWindow.setupUI(self)
        self.mainWindow.pushButton.clicked.connect(lambda: self.startUserInfoWindow(self.mainWindow.lineEdit.text()))
        self.show()

    def startUserInfoWindow(self, userID):
        if boj.isBOJUser(userID):
            self.userInfoWindow.setupUI(self, userID)
            self.userInfoWindow.exitButton.clicked.connect(self.startMainWindow)
            self.show()
        else:
            self.mainWindow.statusbar.showMessage("존재하지 않는 아이디입니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
