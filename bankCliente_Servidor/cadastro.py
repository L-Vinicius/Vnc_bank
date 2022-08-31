from genericpath import exists
from pickle import NONE
from pessoa import Pessoa
import mysql.connector
import hashlib 
from datetime import date 

class Cadastro:
   
    __slots__ = ['_conexao','_cursor','_sql']
    def __init__(self):
        self._conexao = mysql.connector.connect(host = 'localhost',user = 'root', password = 'Vnc@bank5428', database = 'VNC_bank')#Nome do banco de dados
        self._cursor = self._conexao.cursor()                                                                                                                                                               
        self._sql = """CREATE TABLE IF NOT EXISTS usuarios(nome varchar(30) NOT NULL,cpf varchar(11) PRIMARY KEY,endereco varchar(30) NOT NULL, nascimento varchar(10) NOT NULL, senha varchar(15) NOT NULL, numero_conta varchar(6) NOT NULL, saldo varchar(10) NOT NULL, limite varchar(10) NOT NULL, data_cadastro varchar(10) NOT NULL);"""
        self._cursor.execute(self._sql)#executa ou cria a tabela estanciada na variavel _sql 
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS historico(id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, users_CPF VARCHAR(11) NOT NULL, operacao VARCHAR(100000) NOT NULL,  FOREIGN KEY (users_CPF) REFERENCES vnc_bank.usuarios(cpf));""")
        self._conexao.commit()
# Cadastra uma nova pessoa se não houver outra pessoa com o mesmo CPF
    def cadastrar_no_banco(self,pessoa):
        existe = self.busca_no_banco(pessoa.cpf)
        if(existe == False):                                                       
            self._cursor.execute('INSERT INTO usuarios(nome,cpf,endereco,nascimento,senha,numero_conta,saldo,limite,data_cadastro) VALUES(%s,%s,%s,%s,MD5(%s),%s,%s,%s,%s)',(pessoa.nome,pessoa.cpf,pessoa.endereco,pessoa.nascimento,pessoa.senha,pessoa.numero_conta,pessoa.saldo,pessoa.limite,pessoa.data_cadastro))
            self._conexao.commit()
            # self._conexao.close()
            return True
        else:
            return False
# Verifica se existe alguém com o CPF cadastrado   
    def busca_no_banco(self,cpf):
        self._cursor.execute('SELECT * from usuarios WHERE cpf = %s',(cpf,))
        existe = self._cursor.fetchone() #Retorna None caso não encontre nenhum usuário com o cpf cadastrado OU retorna uma tupla com todos os valores do usuario
        if(existe == None):#Só entra se a pessoa buscada não estiver cadastrada
            return False
        else:
            # print(list(existe))#Transformando os valores retornados do BD em lista
            pessoa = Pessoa(existe[0],existe[1],existe[2],existe[3],existe[4],existe[5],float(existe[6]))#Seta os valores da Tupla em uma variável Pessoa para retornar
            return pessoa #Retorna a Pessoa relacionada ao CPF
# Verifica o CPF e Senha para efetuar o Login da conta
    def login(self,cpf,senha):
        self._cursor.execute('SELECT * from usuarios WHERE cpf = %s and senha = %s',(cpf,senha,))#ALTERAÇÃO FEITA PARA SABER SE EXISTE ALGUEM COM O CPF E SENHA EQUIVALENTES
        existe = self._cursor.fetchone() #Retorna None caso não encontre nenhum usuário com o cpf cadastrado OU retorna uma tupla com todos os valores do usuario  
        if(existe == None):#Só entra se a pessoa buscada não estiver cadastrado
            return False
        else:
            pessoa = Pessoa(existe[0],existe[1],existe[2],existe[3],existe[4],existe[5],float(existe[6]))#Seta os valores da Tupla em uma variável Pessoa para retornar
            return pessoa
# Busca o número da conta no banco de dados
    def buscaNumeroconta(self,numero):

        self._cursor.execute('SELECT * from usuarios WHERE numero_conta = %s',(numero,))#ALTERAÇÃO FEITA PARA SABER SE EXISTE ALGUEM COM O NUMERO DA CONTA EQUIVALENTE
        existe = self._cursor.fetchone() #Retorna None caso não encontre nenhum usuário com o cpf cadastrado OU retorna uma tupla com todos os valores do usuario
        if(existe == None):#Só entra se a pessoa buscada não estiver cadastrada
            return False
        else:
            pessoa = Pessoa(existe[0],existe[1],existe[2],existe[3],existe[4],existe[5],float(existe[6]))#Seta os valores da Tupla em uma variável Pessoa para retornar
            return pessoa

# Altera o valor do saldo no banco de dados
    def altera_valor(self,cpf,valor):     
        self._cursor.execute('UPDATE usuarios SET saldo = %s WHERE cpf = %s',(valor,cpf,))
        self._conexao.commit()

# Retorna o saldo atualizado após uma operação
    def valor_alterado(self,cpf):
        self._cursor.execute('SELECT * from usuarios WHERE cpf = %s',(cpf,))#ALTERAÇÃO FEITA PARA SABER SE EXISTE ALGUEM COM O NUMERO DA CONTA EQUIVALENTE
        existe = self._cursor.fetchone() #Retorna None caso não encontre nenhum usuário com o cpf cadastrado OU retorna uma tupla com todos os valores do usuario
        if(existe == None):#Só entra se a pessoa buscada não estiver cadastrada
            return False
        else:
            return existe[6]

# Salva e fecha o banco de dados
    def fechar(self):
        self._conexao.commit()
        self._conexao.close()
        
# Salva o historico de operações realizadas
    def salva_historico(self,info,cpf,valor,numero_conta):
        data = date.today().strftime('%d/%m/%Y')
        if info == 'transfer_rea':
            print(info)
            print(cpf)
            print(numero_conta)
            print(valor)
        #   ESTA EFETUANDO A TRANSFERENCIA SÓ NAO SALVA AQUI
            print('ENTREI NO PRIMEIRO SAVE')
            info = "Transferência realizada de R$ {} para a conta {} dia {}".format(valor,numero_conta,data)
            self._cursor.execute("INSERT INTO vnc_bank.historico(users_CPF,operacao) VALUES (%s, %s)", (cpf,info))
            self._conexao.commit()

        elif info == 'transfer_recv':
            print('valor type')
            info = "Transferência recebida de R$ {} da conta {} dia {}".format(valor,numero_conta,data)
            self._cursor.execute("INSERT INTO vnc_bank.historico(users_CPF,operacao) VALUES (%s, %s)", (cpf,info))
            self._conexao.commit()
            
        elif info == 'deposito':
    
            info = "Deposito realizado de R$ {} dia {}".format(valor,data)
            self._cursor.execute("INSERT INTO vnc_bank.historico(users_CPF,operacao) VALUES (%s, %s)", (cpf,info))
            self._conexao.commit()

   
    def busca_historico(self,cpf):
        self._cursor.execute('SELECT operacao FROM historico WHERE users_CPF = %s',(cpf,))
        existe = self._cursor.fetchall()
        if (existe == None):
            return False
        else:
            return existe