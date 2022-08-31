import datetime
from traceback import print_tb


class Historico:

    __slots__ = ['_data_de_abertura','_transacoes']#'_conta_transacao'
    
    def __init__(self):
        self._data_de_abertura = datetime.datetime.today()
        self._transacoes = []
        # self._conta_transacao = 0

        
    def imprime(self):
        
        for x in self._transacoes:
            print(x)
        























        # print('Data de Abertura: {}'.format(self._data_de_abertura))
        # print("Transacões: ") 
#COMO RETORNAR DIVERSOS VALORES DA LISTA
        # for i in self._transacoes:
        #     print('-', i)
        
    #     if(self._conta_transacao<0):
    #         print('entrou')
    #         return self._transacoes[self.conta_transacao]
    #     else:
    #         self._conta_transacao -= 1
    #         self.imprime()
   
    # @property
    # def conta_transacao(self):
    #     return self._conta_transacao
    # @conta_transacao.setter
    # def conta_transacao(self):
    #     self._conta_transacao +=1
 