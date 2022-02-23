# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.temp_graph = PlotWidget(self.centralwidget)
        self.temp_graph.setMinimumSize(QtCore.QSize(500, 300))
        self.temp_graph.setObjectName("temp_graph")
        self.gridLayout.addWidget(self.temp_graph, 0, 0, 1, 1)
        self.humidity_graph = PlotWidget(self.centralwidget)
        self.humidity_graph.setMinimumSize(QtCore.QSize(500, 300))
        self.humidity_graph.setObjectName("humidity_graph")
        self.gridLayout.addWidget(self.humidity_graph, 0, 1, 1, 1)
        self.temperature_btn = QtWidgets.QPushButton(self.centralwidget)
        self.temperature_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.temperature_btn.setObjectName("temperature_btn")
        self.gridLayout.addWidget(self.temperature_btn, 1, 0, 1, 1)
        self.humidity_btn = QtWidgets.QPushButton(self.centralwidget)
        self.humidity_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.humidity_btn.setFlat(False)
        self.humidity_btn.setObjectName("humidity_btn")
        self.gridLayout.addWidget(self.humidity_btn, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.alarm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.alarm_btn.setMinimumSize(QtCore.QSize(500, 50))
        self.alarm_btn.setObjectName("alarm_btn")
        self.horizontalLayout.addWidget(self.alarm_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.temperature_btn.setText(_translate("MainWindow", "Temperature"))
        self.humidity_btn.setText(_translate("MainWindow", "Humidity"))
        self.alarm_btn.setText(_translate("MainWindow", "Fire an Alarm"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
