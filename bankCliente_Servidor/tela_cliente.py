# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Cliente(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(612, 479)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 71))
        self.label.setStyleSheet("background-color: rgb(118, 0, 88)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(0, 410, 641, 71))
        self.label_2.setStyleSheet("background-color: rgb(118, 0, 88)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(-10, 70, 651, 341))
        self.label_3.setStyleSheet("background-color:rgba(145, 40, 109,0.9)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit_saldo_cliente = QtWidgets.QLineEdit(Form)
        self.lineEdit_saldo_cliente.setEnabled(False)
        self.lineEdit_saldo_cliente.setGeometry(QtCore.QRect(40, 110, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_saldo_cliente.setFont(font)
        self.lineEdit_saldo_cliente.setStyleSheet("QLineEdit{\n"
"    color: rgb(255, 255, 255) ;\n"
"    background-color:rgb(145, 40, 109);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_saldo_cliente.setText("")
        self.lineEdit_saldo_cliente.setFrame(True)
        self.lineEdit_saldo_cliente.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_saldo_cliente.setObjectName("lineEdit_saldo_cliente")
        self.lineEdit_Welcome = QtWidgets.QLineEdit(Form)
        self.lineEdit_Welcome.setEnabled(False)
        self.lineEdit_Welcome.setGeometry(QtCore.QRect(20, 430, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_Welcome.setFont(font)
        self.lineEdit_Welcome.setStyleSheet("background-color: rgb(118, 0, 88);\n"
"color : rgb(255,255,255)")
        self.lineEdit_Welcome.setText("")
        self.lineEdit_Welcome.setFrame(False)
        self.lineEdit_Welcome.setObjectName("lineEdit_Welcome")
        self.pushButton_Sair = QtWidgets.QPushButton(Form)
        self.pushButton_Sair.setGeometry(QtCore.QRect(470, 430, 101, 31))
        self.pushButton_Sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Sair.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0) ;\n"
"    background-color : rgba(255,255,255,0.5);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255,255,255) ;\n"
"    background-color : rgb(0,0,0);\n"
"}")
        self.pushButton_Sair.setObjectName("pushButton_Sair")
        self.pushButton_dados_conta = QtWidgets.QPushButton(Form)
        self.pushButton_dados_conta.setGeometry(QtCore.QRect(130, 180, 131, 51))
        self.pushButton_dados_conta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_dados_conta.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0) ;\n"
"    background-color : rgba(255,255,255,0.5);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bank\img\Account_activity.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_dados_conta.setIcon(icon)
        self.pushButton_dados_conta.setIconSize(QtCore.QSize(50, 40))
        self.pushButton_dados_conta.setObjectName("pushButton_dados_conta")
        self.pushButton_extrato = QtWidgets.QPushButton(Form)
        self.pushButton_extrato.setGeometry(QtCore.QRect(130, 300, 131, 51))
        self.pushButton_extrato.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_extrato.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_extrato.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0) ;\n"
"    background-color : rgba(255,255,255,0.5);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bank\img\Extrato.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_extrato.setIcon(icon1)
        self.pushButton_extrato.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_extrato.setCheckable(False)
        self.pushButton_extrato.setAutoDefault(False)
        self.pushButton_extrato.setDefault(False)
        self.pushButton_extrato.setFlat(False)
        self.pushButton_extrato.setObjectName("pushButton_extrato")
        self.pushButton_transferencia = QtWidgets.QPushButton(Form)
        self.pushButton_transferencia.setGeometry(QtCore.QRect(390, 180, 131, 51))
        self.pushButton_transferencia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_transferencia.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0) ;\n"
"    background-color : rgba(255,255,255,0.5);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("bank\img\Transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_transferencia.setIcon(icon2)
        self.pushButton_transferencia.setIconSize(QtCore.QSize(40, 50))
        self.pushButton_transferencia.setObjectName("pushButton_transferencia")
        self.pushButton_saque = QtWidgets.QPushButton(Form)
        self.pushButton_saque.setGeometry(QtCore.QRect(390, 300, 131, 51))
        self.pushButton_saque.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_saque.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0) ;\n"
"    background-color : rgba(255,255,255,0.5);\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("bank\img\saque.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_saque.setIcon(icon3)
        self.pushButton_saque.setIconSize(QtCore.QSize(40, 50))
        self.pushButton_saque.setObjectName("pushButton_saque")
        self.VNCBank = QtWidgets.QLabel(Form)
        self.VNCBank.setGeometry(QtCore.QRect(260, 10, 171, 61))
        self.VNCBank.setStyleSheet("background-color:rgb(241, 241, 241)rgb(253, 253, 253)")
        self.VNCBank.setObjectName("VNCBank")
        self.Icon_Login = QtWidgets.QLabel(Form)
        self.Icon_Login.setEnabled(True)
        self.Icon_Login.setGeometry(QtCore.QRect(200, 10, 61, 51))
        self.Icon_Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Icon_Login.setStyleSheet("background-color:rgb(241, 241, 241)rgb(253, 253, 253)")
        self.Icon_Login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Icon_Login.setText("")
        self.Icon_Login.setPixmap(QtGui.QPixmap("bank\img\Bank.png"))
        self.Icon_Login.setScaledContents(True)
        self.Icon_Login.setWordWrap(False)
        self.Icon_Login.setObjectName("Icon_Login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.pushButton_dados_conta, self.pushButton_transferencia)
        Form.setTabOrder(self.pushButton_transferencia, self.pushButton_extrato)
        Form.setTabOrder(self.pushButton_extrato, self.pushButton_saque)
        Form.setTabOrder(self.pushButton_saque, self.pushButton_Sair)
        Form.setTabOrder(self.pushButton_Sair, self.lineEdit_Welcome)
        Form.setTabOrder(self.lineEdit_Welcome, self.lineEdit_saldo_cliente)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Sair.setText(_translate("Form", "Sair"))
        self.pushButton_dados_conta.setText(_translate("Form", "Dados da Conta"))
        self.pushButton_extrato.setText(_translate("Form", "Extrato"))
        self.pushButton_transferencia.setText(_translate("Form", "Transferencia"))
        self.pushButton_saque.setText(_translate("Form", "Depositar"))
        self.VNCBank.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">VNC BANK</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Tela_Cliente()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
