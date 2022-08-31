# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_de_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_de_Cadastro(object):
    def setupUi(self, TeladeCadastro):
        TeladeCadastro.setObjectName("TeladeCadastro")
        TeladeCadastro.resize(640, 480)
        TeladeCadastro.setStatusTip("")
        TeladeCadastro.setStyleSheet("background-color:rgba(145, 40, 109,0.9)")
        TeladeCadastro.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(TeladeCadastro)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 190, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 270, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cadastrar.setGeometry(QtCore.QRect(250, 360, 141, 31))
        self.pushButton_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastrar.setToolTip("")
        self.pushButton_cadastrar.setStyleSheet("QPushButton{\n"
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
        self.pushButton_cadastrar.setAutoDefault(True)
        self.pushButton_cadastrar.setDefault(True)
        self.pushButton_cadastrar.setFlat(False)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 230, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(220, 150, 231, 20))
        self.lineEdit_nome.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_nome.setTabletTracking(False)
        self.lineEdit_nome.setStyleSheet("color:rgb(255,255,255)")
        self.lineEdit_nome.setText("")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_endereco = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_endereco.setGeometry(QtCore.QRect(220, 190, 231, 20))
        self.lineEdit_endereco.setStyleSheet("color:rgb(255,255,255)")
        self.lineEdit_endereco.setText("")
        self.lineEdit_endereco.setObjectName("lineEdit_endereco")
        self.lineEdit_CPF = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_CPF.setGeometry(QtCore.QRect(220, 230, 231, 20))
        self.lineEdit_CPF.setStyleSheet("color:rgb(255,255,255)")
        self.lineEdit_CPF.setObjectName("lineEdit_CPF")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(530, 420, 75, 23))
        self.pushButton_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_voltar.setAutoFillBackground(False)
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
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setGeometry(QtCore.QRect(220, 310, 231, 20))
        self.lineEdit_senha.setStatusTip("")
        self.lineEdit_senha.setStyleSheet("color:rgb(255,255,255)")
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 310, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Icon_Login = QtWidgets.QLabel(self.centralwidget)
        self.Icon_Login.setEnabled(True)
        self.Icon_Login.setGeometry(QtCore.QRect(220, 30, 51, 51))
        self.Icon_Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Icon_Login.setStyleSheet("background-color:rgb(241, 241, 241)rgb(253, 253, 253)")
        self.Icon_Login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Icon_Login.setText("")
        self.Icon_Login.setPixmap(QtGui.QPixmap("bank\img\Formulario.png"))
        self.Icon_Login.setScaledContents(True)
        self.Icon_Login.setWordWrap(False)
        self.Icon_Login.setObjectName("Icon_Login")
        self.dateEdit_nascimento = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_nascimento.setGeometry(QtCore.QRect(220, 270, 110, 22))
        self.dateEdit_nascimento.setStyleSheet("color:rgb(255,255,255)")
        self.dateEdit_nascimento.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit_nascimento.setCalendarPopup(True)
        self.dateEdit_nascimento.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_nascimento.setObjectName("dateEdit_nascimento")
        TeladeCadastro.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TeladeCadastro)
        self.statusbar.setObjectName("statusbar")
        TeladeCadastro.setStatusBar(self.statusbar)

        self.retranslateUi(TeladeCadastro)
        QtCore.QMetaObject.connectSlotsByName(TeladeCadastro)
        TeladeCadastro.setTabOrder(self.lineEdit_nome, self.lineEdit_endereco)
        TeladeCadastro.setTabOrder(self.lineEdit_endereco, self.lineEdit_CPF)
        TeladeCadastro.setTabOrder(self.lineEdit_CPF, self.dateEdit_nascimento)
        TeladeCadastro.setTabOrder(self.dateEdit_nascimento, self.lineEdit_senha)
        TeladeCadastro.setTabOrder(self.lineEdit_senha, self.pushButton_cadastrar)
        TeladeCadastro.setTabOrder(self.pushButton_cadastrar, self.pushButton_voltar)

    def retranslateUi(self, TeladeCadastro):
        _translate = QtCore.QCoreApplication.translate
        TeladeCadastro.setWindowTitle(_translate("TeladeCadastro", "MainWindow"))
        self.label_4.setText(_translate("TeladeCadastro", "<html><head/><body><p><span style=\" color:#ffffff;\">Endereço</span></p></body></html>"))
        self.label.setText(_translate("TeladeCadastro", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"> Cadastro</span></p></body></html>"))
        self.label_5.setText(_translate("TeladeCadastro", "<html><head/><body><p><span style=\" color:#ffffff;\">Nascimento</span></p></body></html>"))
        self.pushButton_cadastrar.setText(_translate("TeladeCadastro", "Cadastrar "))
        self.label_3.setText(_translate("TeladeCadastro", "<html><head/><body><p><span style=\" color:#ffffff;\">CPF</span></p></body></html>"))
        self.label_2.setText(_translate("TeladeCadastro", "<html><head/><body><p><span style=\" color:#ffffff;\">Nome</span></p></body></html>"))
        self.pushButton_voltar.setText(_translate("TeladeCadastro", "Voltar"))
        self.label_6.setText(_translate("TeladeCadastro", "<html><head/><body><p><span style=\" color:#ffffff;\">Senha</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeladeCadastro = QtWidgets.QMainWindow()
    ui = Tela_de_Cadastro()
    ui.setupUi(TeladeCadastro)
    TeladeCadastro.show()
    sys.exit(app.exec_())
