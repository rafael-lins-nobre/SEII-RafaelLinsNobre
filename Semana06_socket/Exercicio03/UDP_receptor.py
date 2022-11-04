# Rafael Lins Nobre - 11811EMT002
# Codigo para demonstrar o recebimento de dados atraves do protocolo de comunicacao UDP, sem handshake, ou seja, de forma mais rapida porém menos confiavel

import socket  # Modulo socket para trabalho com transmissao de dados
import select  # Modulo select para recepcao de dados em multiplos sockets

UDP_IP = "127.0.0.1"  # IP do servidor UDP
IN_PORT = 5005        # Porta do servidor
timeout = 3           # Tempo limite para requisição/solicitação

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Inicializa objeto socket para transmissao de dados
sock.bind((UDP_IP, IN_PORT))  # Associação do socket com o endereço local

while True:
    data, addr = sock.recvfrom(1024)  # Variaveis armazenam os dados enviados pelo emissor (client)
    if data:  # Verifica se os dados não são nulos
        print("File name:", data)  # Printa o nome do arquivo
        file_name = data.strip()   # Remove espaços do nome do arquivo

    f = open(file_name, 'wb')  # Abre/cria um arquivo para escrita em binário

    while True:
        ready = select.select([sock], [], [], timeout)  # Utiliza o método select para multiplexar a entrada e saída
        if ready[0]:
            data, addr = sock.recvfrom(1024)  # Variaveis armazenam os dados enviados pelo emissor (client)
            f.write(data)  # Escreve/salve os dados lidos no arquivo
        else:
            print("%s Finish!" % file_name)  # Printa a indicacao que o codigo finalizou
            f.close()  # Fecha o arquivo
            break      # Sai do laço infinito
