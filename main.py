import sys

from PySide2 import QtCore, QtWidgets, QtGui


# class for elements in area
class Translation:
    def __init__(self, to_translate, input_form, translated, correct_translation):
        self.to_translate = to_translate
        self.input_form = input_form
        self.translated = translated
        self.correct_translation = correct_translation


# class AppWidget inherits from QtWidgets class
class AppWidget(QtWidgets.QWidget):
    # fn init accepts 2 arguments
    # self and dictionary to translate
    def __init__(self, dictionary_translate):
        super().__init__()
        self.points = 0
        self.dictionary = dictionary_translate
        self.state = []
        self.layout = self.initialize()
        self.setLayout(self.layout)

    # btn function
    def btn_click(self):
        self.points = 0
        for inline in self.state:
            if inline.correct_translation == inline.input_form.text():
                self.points += 1
        msg = QtWidgets.QMessageBox()
        msg.setText(f'You have {self.points} points')
        msg.exec_()

    # function for make and return area
    def initialize(self):
        label_row = 0
        area = QtWidgets.QGridLayout()

        # create word_to_translate and input
        for key, correct_translation in self.dictionary.items():
            word_to_translate = QtWidgets.QLabel(key)
            enter = QtWidgets.QLineEdit()
            self.state.append(Translation(key, enter, '', correct_translation))

            area.addWidget(word_to_translate, label_row, 0)
            area.addWidget(enter, label_row, 1)
            label_row += 1

        # button
        btn_check = QtWidgets.QPushButton("Check")
        btn_check.clicked.connect(self.btn_click)
        area.addWidget(
            btn_check,
            label_row,
            1
        )
        return area


def main():
    dictionary = {
        'dog': 'pies',
        'cat': 'kot',
        'hello': 'witaj',
    }
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Language learning by Przemyslaw Malara')
    appWidget = AppWidget(dictionary)
    appWidget.resize(800, 600)
    appWidget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
