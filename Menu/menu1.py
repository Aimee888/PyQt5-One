# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menumenu1 = QtWidgets.QMenu(self.menubar)
        self.menumenu1.setObjectName("menumenu1")
        self.menumenu2 = QtWidgets.QMenu(self.menubar)
        self.menumenu2.setObjectName("menumenu2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionchild1 = QtWidgets.QAction(MainWindow)
        self.actionchild1.setObjectName("actionchild1")
        self.actionchild2 = QtWidgets.QAction(MainWindow)
        self.actionchild2.setObjectName("actionchild2")
        self.actionchild3 = QtWidgets.QAction(MainWindow)
        self.actionchild3.setObjectName("actionchild3")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionchild1_2 = QtWidgets.QAction(MainWindow)
        self.actionchild1_2.setObjectName("actionchild1_2")
        self.actionchild2_2 = QtWidgets.QAction(MainWindow)
        self.actionchild2_2.setObjectName("actionchild2_2")
        self.actionchild3_2 = QtWidgets.QAction(MainWindow)
        self.actionchild3_2.setObjectName("actionchild3_2")
        self.menumenu1.addAction(self.actionchild1)
        self.menumenu1.addAction(self.actionchild2)
        self.menumenu1.addAction(self.actionchild3)
        self.menumenu1.addSeparator()
        self.menumenu1.addAction(self.actionexit)
        self.menumenu2.addAction(self.actionchild1_2)
        self.menumenu2.addAction(self.actionchild2_2)
        self.menumenu2.addAction(self.actionchild3_2)
        self.menubar.addAction(self.menumenu1.menuAction())
        self.menubar.addAction(self.menumenu2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menumenu1.setTitle(_translate("MainWindow", "menu1"))
        self.menumenu2.setTitle(_translate("MainWindow", "menu2"))
        self.actionchild1.setText(_translate("MainWindow", "child1"))
        self.actionchild2.setText(_translate("MainWindow", "child2"))
        self.actionchild3.setText(_translate("MainWindow", "child3"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionchild1_2.setText(_translate("MainWindow", "child1"))
        self.actionchild2_2.setText(_translate("MainWindow", "child2"))
        self.actionchild3_2.setText(_translate("MainWindow", "child3"))
