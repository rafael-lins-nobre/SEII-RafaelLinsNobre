# Rafael Lins Nobre - 11811EMT002
# Codigo para demonstrar o envio de dados atraves do protocolo de comunicacao TCP, com a utilizacao de handshake

import socket  # Modulo socket para trabalho com transmissao de dados
import sys

TCP_IP = "127.0.0.1"  # IP do servidor TCP
FILE_PORT = 5005      # Porta de arquivo
DATA_PORT = 5006      # Porta de dados
buf = 1024            # Tamanho do buffer (No codigo emissor nao eh utilizado, mas estava no codigo)
file_name = sys.argv[1]  # Preenche a variavel file_name com a string passada no terminal

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Inicializa objeto socket para transmissao de dados
    sock.connect((TCP_IP, FILE_PORT))  # Conexao do socket o endereco desejado (ENDERECO, PORTA)(Deve ser tuple, como no exercicio2)
    sock.send(file_name)  # Envia o nome do arquivo por mensagem
    sock.close()  # Finaliza o socket instanciado

    print("Sending %s ..." % file_name)  # Printa o nome do arquivo enviado

    f = open(file_name, "rb")  # Abre o arquivo para leitura em binário
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Inicializa objeto socket para transmissao de dados
    sock.connect((TCP_IP, DATA_PORT))  # Conexao do socet com o endereco desejado (ENDERECO, PORTA)
    data = f.read()  # armazena os dados lidos no arquivo em uma variavel
    sock.send(data)  # Envia os dados presentes no arquivo
finally:
    sock.close()  # Encerra a conexão mais uma vez
    f.close()     # Fecha o arquivo
