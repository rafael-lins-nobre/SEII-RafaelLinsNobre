# imports necessarios para funcionamento do codigo
import socket  # modulo para sockets
import threading  # modulo para threads


HEADER = 64 # Tamanho fixo que a primeira mensagem deve ter, para comunicar o tamanho da mensagem que ira seguir
PORT = 5050  # Porta de acesso
SERVER_IP = socket.gethostbyname(socket.gethostname())  # Forma padrao para adiquirir IP local, melhor para repeticao do codigo
ADDR = (SERVER_IP, PORT)  # Endereco precisa estar em um tuple com as informacoes do servidor
FORMAT = 'utf-8'  # Formato de decodificacao
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Declarar o socket que permite o servidor transmitir dados
server.bind(ADDR)  # Estabelecendo uma ligacao entre o objeto server e o endereco desejado para ele


def receber_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Cliente de endereço {addr} conectado")

    connected = True
    while connected:  # Loop verdadeiro ate o cliente mandar a mensagem de desconexao
        msg_length = conn.recv(HEADER).decode(FORMAT) # Receber e decdificar a primeira mensagem, com HEADER indicativo do tamanho da mensagem que vira
        if msg_length:
            msg_length = int(msg_length) # Converter a variavel para Int
            msg = conn.recv(msg_length).decode(FORMAT) # Receber e decodificar a mensagem de fato, ja com a informacao do tamanho dela

            if msg == DISCONNECT_MESSAGE: # Condicao de desconexao do cliente do servidor
                connected = False

            print(f"[{addr}] {msg}") # Print da mensagem
            conn.send("Mensagem recebida".encode(FORMAT))

    conn.close()


def start():
    server.listen()  # Atraves desse metodo o socket 'escuta' as solicitacoes do cliente
    print("[INICIANDO] Iniciando Socket")
    print(f"[ESCUTANDO] Servidor escudando no IP {SERVER_IP}")
    while True:  # Loop infinito
        conn, addr = server.accept()  # Aceita a chamada de um cliente tentando conectar e salva a conexao e o endereco do cliente nas variaveis
        thread = threading.Thread(target=receber_clientes(), args=(conn, addr))  # Utilizam-se threads para chamar a funcao Receber_clientes() para cada cliente que conectar em paralelo
        thread.start()  # inicia a thread
        print(f"[CONEXOES ATIVAS] {threading.active_count() - 1}")


print("Servidor iniciando...")
start()
