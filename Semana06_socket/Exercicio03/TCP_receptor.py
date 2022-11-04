# Rafael Lins Nobre - 11811EMT002
# Codigo para demonstrar o recebimento de dados atraves do protocolo de comunicacao TCP, com a utilizacao de handshake

import socket  # Modulo socket para trabalho com transmissao de dados

TCP_IP = "127.0.0.1"  # IP do servidor TCP
FILE_PORT = 5005      # Porta de arquivo
DATA_PORT = 5006      # Porta de dados
timeout = 3  # Tempo limite para requisição/solicitação
buf = 1024   # Tamanho do buffer de dados

sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Inicializa objeto socket para transmissao de dados
sock_f.bind((TCP_IP, FILE_PORT))  # Associação do socket com o endereço local
sock_f.listen(1)  # Abertura para solicitação de conexao

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Inicializa objeto socket para transmissao de dados
sock_d.bind((TCP_IP, DATA_PORT))  # Associação do socket com o endereço local
sock_d.listen(1)  # Abertura para solicitação de conexao

while True:
    conn, addr = sock_f.accept()  # Variaveis 'conn' e 'address' recebm o return ao aceitar a conexao com o client
    data = conn.recv(buf)  # Armazena o nome do arquivo
    if data:  # verifica se o nome do arquivo não é nulo ou vazio
        print("File name:", data)  # Printa o nome do arquivo
        file_name = data.strip()  # Remove espaços do nome do arquivo

    f = open(file_name, 'wb')  # Instancia o arquivo em f no método de escrita em binario

    conn, addr = sock_d.accept()  # Variaveis 'conn' e 'address' recebm o return ao aceitar a conexao com o client
    while True:
        data = conn.recv(buf)  # Armazena os dados salvos, com o tamanho do buffer
        if not data:  # Se os dados forem vazios (nulos) sai do laço. Indica que acabaram os dados
            break
        f.write(data)  # Armazena os dados no arquivo

    print("%s Finish!" % file_name)  # Printa a finalização da escrita do arquivo e do codigo
    f.close()  # Fecha o arquivo
