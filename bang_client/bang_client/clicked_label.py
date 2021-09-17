from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QLabel, pyqtSignal
from PyQt5.QtCore import QMimeData, Qt

# Реализация Qlabel для обработки события нажатия на кнопку
class ClickedLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()