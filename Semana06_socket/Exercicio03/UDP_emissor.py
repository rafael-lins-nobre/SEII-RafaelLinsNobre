# Rafael Lins Nobre - 11811EMT002
# Codigo para demonstrar o envio de dados atraves do protocolo de comunicacao UDP, sem handshake, ou seja, de forma mais rapida porém menos confiavel

import socket   # Modulo socket para trabalho com transmissao de dados
import time     # Modulo para trabalho com tempo
import sys

UDP_IP = "127.0.0.1"    # IP do servidor UDP
UDP_PORT = 5005         # Porta do servidor
buf = 1024              # Tamanho do buffer
file_name = sys.argv[1] # Preenche a variavel file_name com a string passada no terminal

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializa objeto socket para transmissao de dados
sock.sendto(file_name, (UDP_IP, UDP_PORT))  # Envia o nome do arquivo para o endereco do argumento (Sem handshake)
print("Sending %s ..." % file_name)  # Printa o nome do arquivo enviado

f = open(file_name, "r")  # Abre o arquivo para leitura
data = f.read(buf)  # Armazena os dados lidos em uma variavel

while (data):
    if sock.sendto(data, (UDP_IP, UDP_PORT)):  # Envia os dados do arquivo para o endereco atribuido (Sem handshake)
        data = f.read(buf)  # Leitura do arquivo, linha a linha
        time.sleep(0.02)    # Delay

sock.close()  # Finaliza conexão do socket
f.close()     # Fecha o arquivo
