# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeview3.ui'
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
        self.treeWidget.setGeometry(QtCore.QRect(200, 120, 256, 192))
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeWidget.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeWidget.headerItem().setFont(1, font)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # item_0.setBackground(0, brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # item_0.setBackground(1, brush)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
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
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Key"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Value"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.insert_data_to_tree_view(_translate)
        # self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Test1"))
        # self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "a"))
        # self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "b"))
        # self.treeWidget.topLevelItem(0).child(1).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "c"))
        # self.treeWidget.topLevelItem(0).child(2).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "d"))
        # self.treeWidget.topLevelItem(0).child(3).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Test2"))
        # self.treeWidget.topLevelItem(1).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "a"))
        # self.treeWidget.topLevelItem(1).child(0).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "b"))
        # self.treeWidget.topLevelItem(1).child(1).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "c"))
        # self.treeWidget.topLevelItem(1).child(2).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "d"))
        # self.treeWidget.topLevelItem(1).child(3).setText(1, _translate("MainWindow", "waiting"))
        # self.treeWidget.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "e"))
        # self.treeWidget.topLevelItem(1).child(4).setText(1, _translate("MainWindow", "waiting"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    def insert_data_to_tree_view(self, _translate):
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
