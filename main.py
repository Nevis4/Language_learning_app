import sys

from PySide2 import QtCore, QtWidgets, QtGui


# class AppWidget inherits from QtWidgets class
class AppWidget(QtWidgets.QWidget):
    # fn init accepts 2 arguments
    # self and dictionary to translate
    def __init__(self, dictionary_translate):
        super().__init__()
        self.dictionary = dictionary_translate
        self.layout = self.initialize()
        self.setLayout(self.layout)

    def initialize(self):
        label_row = 0
        area = QtWidgets.QGridLayout()
        for key in self.dictionary:
            label = QtWidgets.QLabel(key)
            enter = QtWidgets.QLineEdit()
            area.addWidget(label, label_row, 0)
            area.addWidget(enter, label_row, 1)
            label_row += 1

        return area


def main():
    dictionary = {
        'dog': 'pies',
        'cat': 'kot',
        'hello': 'witaj'
    }
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Language learning by Przemyslaw Malara')
    appWidget = AppWidget(dictionary)
    appWidget.resize(800, 600)
    appWidget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
