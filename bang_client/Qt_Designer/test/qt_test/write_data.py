import sys
import ui_write_data
import read_data

from PyQt5 import QtWidgets


class write_data_class(QtWidgets.QWidget, ui_write_data.Ui_MainWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.pushButton.clicked.connect(lambda: self.report(mainWindow))

    def report(self, mainWindow):
        rd = read_data.read_data_class(mainWindow, self.textEditUser.toPlainText(), self.textEditPassword.toPlainText())
        # self.rd.show()


if __name__ == '__main__':
    main_form_app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    wd = write_data_class(MainWindow)
    # wd.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(main_form_app.exec_())
