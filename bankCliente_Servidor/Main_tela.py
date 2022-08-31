import sys
from traceback import extract_tb, print_tb
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from matplotlib.cbook import pts_to_midstep
from cadastro import Cadastro
from pessoa import Pessoa
from tela_de_busca import Tela_de_Busca
from tela_de_cadastro import Tela_de_Cadastro
from tela_de_login import Tela_de_Login
from tela_cliente import Tela_Cliente
from tela_deposito import Tela_Deposito
from tela_extrato import Tela_Extrato
from tela_transferencia import Tela_Transferencia
from historico import Historico
import hashlib
import socket

ip = 'localhost'
port = 8080
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)




class Ui_Main(QtWidgets.QWidget):

    def setupUi(self,Main):
        Main.setObjectName('Main')
        Main.resize(640,480)
        
        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()#Tela_Login
        self.stack1 = QtWidgets.QMainWindow()#Tela_Cadastro
        self.stack2 = QtWidgets.QMainWindow()#Tela_Cliente
        self.stack3 = QtWidgets.QMainWindow()#Tela_busca
        self.stack4 = QtWidgets.QMainWindow()#Tela_Deposito
        self.stack5 = QtWidgets.QMainWindow()#Tela_Extrato
        self.stack6 = QtWidgets.QMainWindow()#Tela_Transferencia

        self.tela_login = Tela_de_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Tela_de_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_cliente = Tela_Cliente()
        self.tela_cliente.setupUi(self.stack2)   

        self.tela_busca = Tela_de_Busca()
        self.tela_busca.setupUi(self.stack3)

        self.tela_deposito = Tela_Deposito()
        self.tela_deposito.setupUi(self.stack4)

        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi(self.stack5)

        self.tela_transferencia = Tela_Transferencia()
        self.tela_transferencia.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        
class Main(QMainWindow,Ui_Main):
    #-----------------------VARIAVEIS GLOBAL-----------------------------------#
    CPF_atual = str()#VARIÁVEL UTILIZADA PARA ARMAZENAR O CPF DO USUÁRIO LOGADO 
    login = list()
    # pessoa = ''
    #--------------------------------------------------------------------------#

    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        
        #BOTÕES TELA DE LOGIN
        self.tela_login.pushButton_entrar.clicked.connect(self.logar)# botao para abrir a tela Principal após verificar senha e cpf
        
        self.tela_login.pushButton_cadastrar.clicked.connect(self.abrirTelaCadastro)# botao para abrir a tela de Cadastro

        #BOTÕES TELA DE CADASTRO
        self.tela_cadastro.pushButton_voltar.clicked.connect(self.botaoVoltar_cad)# botao para voltar para a tela de login
        self.tela_cadastro.pushButton_cadastrar.clicked.connect(self.botaoCadastra)# botao para cadastrar cliente

        #BOTÕES TELA DE DADOS CLIENTE
        self.tela_busca.pushButton_voltar.clicked.connect(self.botaoVoltar_busca)# botao para voltar para a tela Principal
        self.tela_busca.pushButton_buscar.clicked.connect(self.botaoBusca)# botao para buscar os dados de acordo com o CPF
        
        #BOTÕES TELA DE DEPOSITO
        self.tela_deposito.pushButton_depositar.clicked.connect(self.botaoDepositar)# botao para realizar o depósito
        self.tela_deposito.pushButton_voltar.clicked.connect(self.botaoVoltar_busca)# botao para voltar para a tela Principal 
        
        #BOTÕES TELA EXTRATO
        self.tela_extrato.pushButton_gerar_extrato.clicked.connect(self.botaoGerarExtrato)# botao para gerar extrato
        self.tela_extrato.pushButton_voltar.clicked.connect(self.botaoVoltar_busca)#botao para voltar para a tela principal

        #BOTAO TELA TRANSFERENCIA
        self.tela_transferencia.pushButton_transferir.clicked.connect(self.botaoEfetuarTransferencia)#botao para realizar a transferencia
        self.tela_transferencia.pushButton_voltar.clicked.connect(self.botaoVoltar_busca)#botao para voltar para a tela Principal

        #BOTÕES TELA PRINCIPAL
        self.tela_cliente.pushButton_dados_conta.clicked.connect(self.abrirTelaBusca) # botao para abrir a tela de Dados do Cliente
        self.tela_cliente.pushButton_Sair.clicked.connect(self.botaoVoltar_cad) # botao para voltar para a tela de login
        self.tela_cliente.pushButton_extrato.clicked.connect(self.abrirTelaExtrato) #botao para  abrir a tela de Extrato
        self.tela_cliente.pushButton_saque.clicked.connect(self.abrirTelaDeposito)# botao para abrir a tela de Deposito
        self.tela_cliente.pushButton_transferencia.clicked.connect(self.abrirTelaTransferencia)#botao para abrir a tela de Transferencia
          
    def botaoGerarExtrato(self):

        client_socket.send('6'.encode())
        client_socket.send(Main.CPF_atual.encode())

        lista = client_socket.recv(4096).decode()
        if lista != '0':
            self.tela_extrato.textEdit_extrato.setText(str(lista))
      
    def botaoEfetuarTransferencia(self):
        # Main.CPF_atual#utilizado para referenciar quem está com 

        destinatario = self.tela_transferencia.lineEdit_destinatario.text()
        valor = self.tela_transferencia.lineEdit_valor.text()
        if not(valor == '' or destinatario == ''):
            client_socket.send('4'.encode())
            
            lista_de_dados = []
            lista_de_dados.append(Main.CPF_atual)#CPF DO USUARIO LOGADO
            lista_de_dados.append(destinatario)#NUMERO DA CONTA DO USUARIO DESTINO
            lista_de_dados.append(valor)#VALOR DA TRANSFERENCIA
            dados = ",".join(lista_de_dados)
            
            client_socket.send(dados.encode())

            retorno = client_socket.recv(4096).decode()
            
            if (retorno == '0'):
                QMessageBox.information(None,'VNC Bank','Número da Conta Inválido!')
                self.tela_transferencia.lineEdit_destinatario.setText('')
            else:    
                if (retorno == '1'):
                    print('entrei no 1')
                    QMessageBox.information(None,'VNC Bank','Saldo Insuficiente!')
                    self.tela_transferencia.lineEdit_valor.setText('')
                else:
                    print('entrei no else')
                    Main.login[6] = retorno
                    self.tela_cliente.lineEdit_saldo_cliente.setText('Saldo:'+Main.login[6]+'R$')#PEGA O SALDO DA PESSOA QUE ESTÁ ATUALMENTE LOGADA
                    QMessageBox.information(None,'VNC Bank','Transferencia realizada com sucesso!')
                    self.tela_transferencia.lineEdit_destinatario.setText('')
                    self.tela_transferencia.lineEdit_valor.setText('')
                    self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.information(None,'VNC Bank','Todos os campos precisam ser preenchidos!')

    def botaoDepositar(self):
        valor = self.tela_deposito.lineEdit_valor.text()
        if not(valor == ''):
            client_socket.send('3'.encode())

            lista_de_dados = []
            lista_de_dados.append(Main.CPF_atual)
            lista_de_dados.append(valor)
            dados = ",".join(lista_de_dados)
            client_socket.send(dados.encode())
        
            retorno = client_socket.recv(4096).decode()
            # print('AQ?UI'+retorno)
            if(retorno != '0'):
                Main.login[6] = retorno
                self.tela_cliente.lineEdit_saldo_cliente.setText('Saldo:'+Main.login[6]+ 'R$')#PEGA O SALDO DA PESSOA QUE ESTÁ ATUALMENTE LOGADA DEPOIS DO DEPOSITO
                QMessageBox.information(None,'VNC Bank','Depósito Realizado com Sucesso!')
                self.tela_deposito.lineEdit_valor.setText('')
                self.QtStack.setCurrentIndex(2)
            else:
                
                QMessageBox.warning(None,'VNC Bank','Digite um valor acima de 0!')
                self.tela_deposito.lineEdit_valor.setText('')
        else:
            
            QMessageBox.warning(None,'VNC Bank','Todos os campos precisam ser preenchidos!')
            
    def logar(self):
        

        cpf = self.tela_login.lineEdit_username.text()
        senha = hashlib.md5((self.tela_login.lineEdit_password.text()).encode("utf8")).hexdigest()#TRANSFORMA A SENHA EM UM HASH depois VISUALIZA EM HEXADECIMAL
        if not(cpf == '' or senha == ''):
            client_socket.send('2'.encode())
            # pessoa = self.cad.login(cpf,senha)
            lista_de_dados = []
            lista_de_dados.append(cpf)
            lista_de_dados.append(senha)
            dados = ",".join(lista_de_dados)
            client_socket.send(dados.encode())
            

            pessoa = client_socket.recv(4096).decode()
            

            if (pessoa != '0'):

                Main.login = pessoa.split(',')#TRANSFORMA EM OS DADOS DO CLIENTE EM UMA LISTA

                self.QtStack.setCurrentIndex(2)
                Main.CPF_atual = Main.login[1].strip("' '")
                nome = Main.login[0].strip("' '")
                nome = nome.split(" ",2)
                self.tela_cliente.lineEdit_Welcome.setText('Bem Vindo, '+ nome[0] +'!')
                self.tela_cliente.lineEdit_saldo_cliente.setText('Saldo: R$'+ Main.login[6])#PEGA O SALDO DA PESSOA QUE ESTÁ LOGADA
                self.tela_login.lineEdit_username.setText('')
                self.tela_login.lineEdit_password.setText('')
            else:
                self.tela_login.lineEdit_username.setText('')
                self.tela_login.lineEdit_password.setText('')
                QMessageBox.information(None,'VNC Bank','CPF ou Senha incorreto!')
        else:
            QMessageBox.information(None,'VNC Bank','Todos os campos precisam ser preenchidos!')

    def botaoCadastra(self):


        nome = self.tela_cadastro.lineEdit_nome.text()
        endereco = self.tela_cadastro.lineEdit_endereco.text()
        cpf = self.tela_cadastro.lineEdit_CPF.text()
        nascimento = self.tela_cadastro.dateEdit_nascimento.text()
        senha = self.tela_cadastro.lineEdit_senha.text()

        if not((nome == '' or endereco == '' or cpf == '' or nascimento == '' or senha == '')) :
            if not(nome == cpf or cpf == senha):
                print('entrei')
                client_socket.send('1'.encode())

                self.tela_cadastro.lineEdit_nome.setText('')
                self.tela_cadastro.lineEdit_endereco.setText('')
                self.tela_cadastro.lineEdit_CPF.setText('')
                self.tela_cadastro.lineEdit_senha.setText('')
                # self.QtStack.setCurrentIndex(0)
                
                lista_de_dados = []
                lista_de_dados.append(nome)
                lista_de_dados.append(cpf)
                lista_de_dados.append(endereco)
                lista_de_dados.append(nascimento)
                lista_de_dados.append(senha)
                dados = ",".join(lista_de_dados)

                client_socket.send(dados.encode())

                retorno = client_socket.recv(4096).decode()
                if(retorno == '1'):
                    QMessageBox.information(None,'VNC Bank','Cadastro Realizado!')
                else:
                    QMessageBox.information(None,'VNC Bank','CPF já cadastrado!')
                    client_socket.send('1'.encode())

            else:
                
                self.tela_cadastro.lineEdit_nome.setText('')
                self.tela_cadastro.lineEdit_endereco.setText('')
                self.tela_cadastro.lineEdit_CPF.setText('')
                self.tela_cadastro.lineEdit_senha.setText('')
                QMessageBox.warning(None,'VNC Bank','Não podem existir campos com valores iguais ao CPF')
        else:

            
            self.tela_cadastro.lineEdit_nome.setText('')
            self.tela_cadastro.lineEdit_endereco.setText('')
            self.tela_cadastro.lineEdit_CPF.setText('')
            self.tela_cadastro.lineEdit_senha.setText('')
            QMessageBox.information(None,'VNC Bank','Todos os campos precisam ser preenchidos')

    def botaoBusca(self):
        # cpf = self.tela_busca.lineEdit_CPF_2.text()
        client_socket.send('5'.encode())
        client_socket.send(Main.CPF_atual.encode())

        pessoa = client_socket.recv(4096).decode()
        
        Main.login = pessoa.split(',')#TRANSFORMA EM OS DADOS DO CLIENTE EM UMA LISTA
      
        if(pessoa != None):
            self.tela_busca.lineEdit_CPF_2.setText(Main.login[0].strip("' '"))
            self.tela_busca.lineEdit_nome_2.setText(Main.login[1].strip("' '"))
            self.tela_busca.lineEdit_endereco_2.setText(Main.login[2].strip("' '"))
            self.tela_busca.lineEdit_nascimento_2.setText(Main.login[3].strip("' '"))
            self.tela_busca.lineEdit_data_cadastro.setText(Main.login[4].strip("' '"))
            self.tela_busca.lineEdit_limite.setText(Main.login[5].strip("' '"))
            self.tela_busca.lineEdit_numero_conta.setText(Main.login[6].strip("' '"))
        else:
            self.tela_busca.lineEdit_CPF_2.setText('')
            self.tela_busca.lineEdit_nome_2.setText('')
            self.tela_busca.lineEdit_endereco_2.setText('')
            self.tela_busca.lineEdit_nascimento_2.setText('')
            self.tela_busca.lineEdit_limite.setText('')
            self.tela_busca.lineEdit_data_cadastro.setText('')
            self.tela_busca.lineEdit_numero_conta.setText('')
            QMessageBox.information(None,'VNC Bank','CPF não localizado!')

    def botaoVoltar_cad(self):
       
        self.QtStack.setCurrentIndex(0)
           
    def botaoVoltar_busca(self):
        self.tela_busca.lineEdit_CPF_2.setText('')
        self.tela_busca.lineEdit_nome_2.setText('')
        self.tela_busca.lineEdit_endereco_2.setText('')
        self.tela_busca.lineEdit_nascimento_2.setText('')
        self.tela_busca.lineEdit_limite.setText('')
        self.tela_busca.lineEdit_data_cadastro.setText('')
        self.tela_busca.lineEdit_numero_conta.setText('')
        self.tela_transferencia.lineEdit_destinatario.setText('')
        self.tela_transferencia.lineEdit_valor.setText('')
        self.tela_deposito.lineEdit_valor.setText('')

        self.tela_extrato.textEdit_extrato.setText('')
       
        

        self.QtStack.setCurrentIndex(2)

    def abrirTelaCadastro(self):
        self.tela_login.lineEdit_password.setText('')
        self.tela_login.lineEdit_username.setText('')
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBusca(self):
        self.QtStack.setCurrentIndex(3)
    
    def abrirTelaDeposito(self):
        self.QtStack.setCurrentIndex(4)

    def abrirTelaExtrato(self):
        self.QtStack.setCurrentIndex(5)
    
    def abrirTelaTransferencia(self):
        self.QtStack.setCurrentIndex(6)
    
    @staticmethod
    def sair():
        
        Cadastro.fechar()
        sys.exit(app.exec_())

if __name__ == '__main__':  
    app = QApplication(sys.argv)
    show_main = Main()
    app.exec_()
    