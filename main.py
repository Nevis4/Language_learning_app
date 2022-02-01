import sys

from PySide2 import QtCore, QtWidgets, QtGui


class AppWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel('Hello World')
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    appWidget = AppWidget()
    appWidget.resize(800, 600)
    appWidget.show()
    sys.exit(app.exec_())
