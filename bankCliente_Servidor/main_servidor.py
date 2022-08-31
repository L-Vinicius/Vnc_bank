from email.policy import default
from http import client
from traceback import print_tb
from cadastro import Cadastro
from pessoa import Pessoa
import socket

host = 'localhost'
port = 8080
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)
print("Aguardando conexao...")
con, cliente = serv_socket.accept()
print("conectado")

#-----------------------VARIAVEIS GLOBAL-----------------------------------#
cadastro = Cadastro()
# pessoa = ''
#--------------------------------------------------------------------------#


def banco(funcao):
    #FUNÇÃO PARA CADASTRAR
    if (funcao == '1'):
        # print('entrei!!!!!')
        dados = con.recv(4096).decode()
        lista = dados.split(',')
        p1 = Pessoa(lista[0], lista[1], lista[2], lista[3], lista[4])
        retorno = cadastro.cadastrar_no_banco(p1)
        if(retorno == True):
            con.send('1'.encode())
        else:
            con.send('0'.encode())
    #FUNÇÃO PARA LOGAR
    elif(funcao == '2'):

        dados = con.recv(4096).decode()#RECEBE CPF E SENHA
        lista = dados.split(',')#TRANSFORMA CPF E SENHA EM UMA LISTA
        pessoa = cadastro.login(lista[0],lista[1])#RECEBE OS DADOS DO CLIENTE SE CONSEGUIR LOGAR
        # print('OQUE O CLIENTE RECEBE',pessoa)
        if(pessoa != False):
            # ENTRA SE O CLIENTE ESTIVER CADASTRADO NO BANCO
            login = []
            login.append(pessoa.nome) 
            login.append(pessoa.cpf) 
            login.append(pessoa.endereco) 
            login.append(pessoa.nascimento) 
            login.append(pessoa.senha) 
            login.append(pessoa.numero_conta) 
            login.append(pessoa.saldo)
            dados = str(login).strip('[]')        
            con.send(dados.encode())
        else:
            con.send('0'.encode())
    #FUNÇÃO PARA DEPOSITO
    elif(funcao == '3'):
        
        dados = con.recv(4096).decode()#RECEBE O CPF E O VALOR DO DEPOSITO(lista[1]) DO CLIENTE LOGADO
        lista = dados.split(',')
        pessoa = cadastro.busca_no_banco(lista[0])#PEGA OS DADOS DO CLIENTE LOGADO 
    
        if (float(lista[1])>0):
            
            valor_alterado = pessoa.depositar(float(lista[1]))
            con.send(str(valor_alterado).encode())
            cadastro.altera_valor(pessoa.cpf,valor_alterado)
            cadastro.salva_historico('deposito',pessoa.cpf,lista[1],'')
           
        else:
            con.send('0'.encode())    
    #FUNÇÃO DE TRANSFERENCIA    
    elif(funcao == '4'):

        dados = con.recv(4096).decode()#RECEBE O CPF_ATUAL[lista[0]],Num_Cont_Destinatario[lista[1] e O VALOR DA TRANSFERENCIA (lista[2])
        lista = dados.split(',')
       
        pessoa1 = cadastro.busca_no_banco(lista[0])#RETORNA O TITULAR DA CONTA QUE ESTÁ ENVIANDO
        pessoa = cadastro.buscaNumeroconta(lista[1])#RETORNAR O DESTINATÁRIO A RECEBER O VALOR ATRAVES DO NUMERO DA CONTA
        if (pessoa1 != False and pessoa != False):
           
            if((pessoa1.transfere(pessoa,float(lista[2])))!= False):

                cadastro.salva_historico('transfer_rea',pessoa1.cpf,lista[2],pessoa.numero_conta)#SALVA O HISTORICO DO CPF LOGADO
                cadastro.salva_historico('transfer_recv',pessoa.cpf,lista[2],pessoa1.numero_conta)#SALVA O HISTORICO DO DESTINATÁRIO
                cadastro.altera_valor(pessoa1.cpf,pessoa1.saldo)
                cadastro.altera_valor(pessoa.cpf,pessoa.saldo)
                con.send(str(pessoa1.saldo).encode())   

            else:
                con.send('1'.encode())        
        else:
            con.send('0'.encode())   
    #FUNÇÃO DE BUSCA DADOS     
    elif(funcao == '5'):

        cpf = con.recv(4096).decode()
        
        pessoa = cadastro.busca_no_banco(cpf)
        print(pessoa.nome)
        if pessoa != False:
            login = []
            login.append(pessoa.cpf) 
            login.append(pessoa.nome) 
            login.append(pessoa.endereco) 
            login.append(pessoa.numero_conta) 
            login.append(pessoa.nascimento) 
            login.append(pessoa.data_cadastro) 
            login.append(pessoa.limite)
            dados = str(login).strip('[]')        
            con.send(dados.encode())
        else:
            con.send('0'.encode())
    elif(funcao  == '6'):

        cpf = con.recv(4096).decode()
        
        extrato = cadastro.busca_historico(cpf)
        if(extrato != False):
            lista = list()
            for x in range (len(extrato)):
                lista.append(extrato[x][0])#TRANSFORMANDO A TUPLA EM UMA LISTA

            lista = ",".join(lista)

            lista = lista.replace(",","\n")
            con.send(lista.encode())
        else:
            con.send('0'.encode())



while(True):#PARTE QUE EXECUTA

    try:
        funcao = con.recv(4096).decode()
        banco(funcao)

    except:
        serv_socket.close()
        break
