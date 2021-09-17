import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from PyQt5.QtWidgets import QMessageBox

import windows.base_windows.callback

import windows.main_menu

import sys
from PyQt5 import QtWidgets

class callback_class(QtWidgets.QWidget, windows.base_windows.callback.Ui_CallbackWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.buttonBack.clicked.connect(lambda: self.buttonBackClicked(mainWindow))
        self.buttonSend.clicked.connect(lambda: self.buttonSendClicked())

    def buttonBackClicked(self, mainWindow):
        main_menu = windows.main_menu.main_menu_class(mainWindow)

    def buttonSendClicked(self):
        if((self.plainTextEdit.toPlainText() != "") and (self.textEditMessage.toPlainText() != "")):
            try:
                from_email = 'dima040998@yandex.ru'
                from_password = 'bankaixex238040998'

                to_email = 'dima040998@yandex.ru'
                message = self.textEditMessage.toPlainText() + '\n'
                message += self.plainTextEdit.toPlainText()

                msg = MIMEMultipart()
                msg['From'] = from_email
                msg['To'] = to_email
                msg['Subject'] = 'Отзыв об игре Бэнг'

                msg.attach(MIMEText(message, 'plain'))

                server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
                server.login(from_email, from_password)
                server.send_message(msg)
                server.quit()
            except Exception:
                message = QMessageBox()
                message.setWindowTitle("Информация об отправке")
                message.setText("Письмо не отправлено")
                message.setIcon(QMessageBox.Warning)
                message.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)

                message.exec_()
            else:
                message = QMessageBox()
                message.setWindowTitle("Информация об отправке")
                message.setText("Письмо успешно отправлено")
                message.setIcon(QMessageBox.Warning)
                message.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)

                message.exec_()

                self.plainTextEdit.setPlainText("")
                self.textEditMessage.setPlainText("")
        else:
            message = QMessageBox()
            message.setWindowTitle("Предупреждение")
            message.setText("Не все поля заполнены")
            message.setIcon(QMessageBox.Warning)
            message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            message.exec_()