# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeview1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import treeview_data


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(270, 190, 256, 192))
        self.treeWidget.setObjectName("treeWidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(150, 120, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.headerItem().setBackground(0, QtGui.QColor(170, 170, 255))
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget.headerItem().setForeground(0, brush)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeWidget.headerItem().setFont(1, font)
        self.treeWidget.headerItem().setBackground(1, QtGui.QColor(170, 170, 255))
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget.headerItem().setForeground(1, brush)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "key"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "value"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.initial_tree_view(_translate)
        self.treeWidget.expandAll()
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        
    def initial_tree_view(self, _translate):
        list_objects = []
        test1 = treeview_data.DataCollection()
        test1.set_module({"Test1": "waiting"})
        test1.add_item({"a1": "waiting"})
        test1.add_item({"b1": "waiting"})
        test1.add_item({"c1": "waiting"})
        list_objects.append(test1)

        test2 = treeview_data.DataCollection()
        test2.set_module({"Test2": "waiting"})
        test2.add_item({"a2": "waiting"})
        test2.add_item({"b2": "waiting"})
        test2.add_item({"c2": "waiting"})
        test2.add_item({"d2": "waiting"})
        list_objects.append(test2)

        test3 = treeview_data.DataCollection()
        test3.set_module({"Test3": "waiting"})
        test3.add_item({"a2": "waiting"})
        test3.add_item({"b2": "waiting"})
        test3.add_item({"c2": "waiting"})
        test3.add_item({"d2": "waiting"})
        list_objects.append(test3)

        for object_num, object_module in enumerate(list_objects):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
            brush = QtGui.QBrush(QtGui.QColor(176, 165, 172))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item_0.setBackground(0, brush)
            for module_name, module_result in object_module.module.items():
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item_0.setBackground(1, brush)
                self.treeWidget.topLevelItem(object_num).setText(0, _translate("MainWindow", module_name))
                self.treeWidget.topLevelItem(object_num).setText(1, _translate("MainWindow", module_result))
            for item_num, item_dic in enumerate(object_module.items):
                for item_name, item_result in item_dic.items():
                    item_1 = QtWidgets.QTreeWidgetItem(item_0)
                    self.treeWidget.topLevelItem(object_num).child(item_num).setText(0, _translate("MainWindow", item_name))
                    self.treeWidget.topLevelItem(object_num).child(item_num).setText(1, _translate("MainWindow", item_result))

        self.progressBar.setValue(24)
