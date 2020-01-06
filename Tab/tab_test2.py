import sys
from PySide2 import QtCore, QtGui, QtWidgets

class MainWindow():
  def __init__(self):
      self.window = QtWidgets.QMainWindow()
      self.initSize(0.6)

      self.mainWidget = QtWidgets.QWidget()
      self.mainLayout = QtWidgets.QVBoxLayout()
      self.mainWidget.setLayout(self.mainLayout)
      self.window.setCentralWidget(self.mainWidget)
      self.mainLayout.addWidget(self.loadTabWidgets())

  def initSize(self, rate):
      desktop = QtWidgets.QApplication.desktop()
      self.screenWidth = desktop.width() * rate
      self.screenHeight = desktop.height() * rate
      print("screen width is %d height is %d"%(self.screenWidth, self.screenHeight))
      self.window.resize(self.screenWidth, self.screenHeight)

  def loadTabWidgets(self):
      tabWidgets = QtWidgets.QTabWidget()
      widget = QtWidgets.QWidget()
      layout = QtWidgets.QVBoxLayout()
      label = QtWidgets.QLabel()
      label.setText("test one QVBoxLayout item one")
      layout.addWidget(label)
      label = QtWidgets.QLabel()
      label.setText("test one QVBoxLayout item one")
      layout.addWidget(label)
      label = QtWidgets.QLabel()
      label.setText("test one QVBoxLayout item one")
      layout.addWidget(label)
      widget.setLayout(layout)
      tabWidgets.addTab(widget, "test one")

      label = QtWidgets.QLabel()
      label.setText("test tab two")
      tabWidgets.addTab(label, "test two")
      tabWidgets.show()
      return tabWidgets

  def show(self):
      self.window.show()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())