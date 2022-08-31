from psutil import cpu_freq
import random
from datetime import date 
from historico import Historico
import hashlib
import mysql.connector


class Pessoa:
    _total_contas = 0
    
    __slots__ = ['_nome','_cpf','_endereco','_nascimento','_senha','_saldo','_limite','_numero_conta','_data_cadastro']
    def __init__(self,nome,cpf,endereco,data_nascimento,senha,numero_conta = str(random.randint(10000,50000)), saldo = float(500.01)):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._nascimento = data_nascimento
        self._senha = senha 
        self._saldo = saldo
        self._numero_conta = numero_conta
        self._limite = float(1000.00)
        self._data_cadastro = date.today().strftime('%d/%m/%Y')
        

    @property
    def nome(self):
        return self._nome
    @property
    def cpf(self):
        return self._cpf
    @property
    def endereco(self):
        return self._endereco
    @property
    def nascimento(self):
        return self._nascimento
    @property
    def senha(self):
        return self._senha
    @property
    def numero_conta(self):
        return self._numero_conta
    @property
    def saldo(self):
        return self._saldo
    @property
    def limite(self):
        return self._limite
    @property
    def data_cadastro(self):
        return self._data_cadastro
    @staticmethod
    def total_contas():
        return Pessoa._total_contas


    def sacar(self, valor):

        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self._historico._transacoes.append('Saque de: R${}'.format(valor))
            return True
  
    def depositar(self, valor):
        self._saldo += valor 
        return self._saldo #ALTEREI AQUI PARA RETORNAR O VALOR ATUALIZADO
        
    def transfere(self, destino, valor):

        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor#TEM QUE ALTERAR O VALOR DESSA VARIÁVEL NO BANCO DE DADOS
            destino._saldo += valor#TEM QUE ALTERAR O VALOR DESSA VARIÁVEL NO BANCO DE DADOS
            return True

    @nome.setter
    def nome(self,Newname):
        self._nome = Newname
        
    @endereco.setter
    def endereco(self,Newendereco):
        self._endereco = Newendereco

    @senha.setter
    def senha(self,Newsenha):
        self._senha = Newsenha
