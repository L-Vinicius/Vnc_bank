# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_extrato.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Extrato(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 475)
        Form.setStyleSheet("background-color:rgba(145, 40, 109,0.9)")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 20, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_gerar_extrato = QtWidgets.QPushButton(Form)
        self.pushButton_gerar_extrato.setGeometry(QtCore.QRect(250, 440, 111, 21))
        self.pushButton_gerar_extrato.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_gerar_extrato.setStyleSheet("QPushButton{\n"
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
        self.pushButton_gerar_extrato.setAutoDefault(True)
        self.pushButton_gerar_extrato.setDefault(True)
        self.pushButton_gerar_extrato.setObjectName("pushButton_gerar_extrato")
        self.pushButton_voltar = QtWidgets.QPushButton(Form)
        self.pushButton_voltar.setGeometry(QtCore.QRect(540, 440, 75, 21))
        self.pushButton_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_voltar.setStyleSheet("QPushButton{\n"
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
        self.pushButton_voltar.setAutoDefault(True)
        self.pushButton_voltar.setDefault(True)
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.Icon_Login = QtWidgets.QLabel(Form)
        self.Icon_Login.setEnabled(True)
        self.Icon_Login.setGeometry(QtCore.QRect(150, 20, 61, 61))
        self.Icon_Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Icon_Login.setStyleSheet("background-color:rgb(241, 241, 241)rgb(253, 253, 253)")
        self.Icon_Login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Icon_Login.setText("")
        self.Icon_Login.setPixmap(QtGui.QPixmap("bank\img\historico2.png"))
        self.Icon_Login.setScaledContents(True)
        self.Icon_Login.setWordWrap(False)
        self.Icon_Login.setObjectName("Icon_Login")
        self.textEdit_extrato = QtWidgets.QTextEdit(Form)
        self.textEdit_extrato.setEnabled(False)
        self.textEdit_extrato.setGeometry(QtCore.QRect(80, 110, 511, 291))
        self.textEdit_extrato.setStyleSheet("QTextEdit{\n"
"    color: rgb(0, 0, 0) ;\n"
"    background-color : rgba(205,205,205,0.7);\n"
"    border-radius: 10px\n"
"}")
        self.textEdit_extrato.setObjectName("textEdit_extrato")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Hist??rico de Transa????es</span></p></body></html>"))
        self.pushButton_gerar_extrato.setText(_translate("Form", "Gerar Extrato"))
        self.pushButton_voltar.setText(_translate("Form", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Tela_Extrato()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
