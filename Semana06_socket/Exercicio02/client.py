import socket

HEADER = 64  # Tamanho fixo que a primeira mensagem deve ter, para comunicar o tamanho da mensagem que ira seguir
PORT = 5050  # Porta de acesso
SERVER_IP = "192.168.1.26"  # Forma padrao para adiquirir IP local, melhor para repeticao do codigo
ADDR = (SERVER_IP, PORT)  # Endereco precisa estar em um tuple com as informacoes do servidor
FORMAT = 'utf-8'  # Formato de decodificacao
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)  # Declarar o socket que permite que o cliente transmitia dados
client.connect(ADDR)  # Conecta o cliente no endereco passado como argumento


def send(msg):
    message = msg.encode(FORMAT)  # Codifica a mensagem no formato especificado
    msg_length = len(message)     # Tamanho da mensagem
    send_length = str(msg_length).encode(FORMAT)        # Pega o tamanho da mensagem enviada
    send_length += b' ' * (HEADER - len(send_length))   # Envia o numero com o tamanho da mensagem, mais um 'enchimento' para o HEADER ter tamanho 64
    client.send(send_length)  # Envia mensagem com o tamnho da mensagem seguinte
    client.send(message)      # Envia a mensagem propriamente dita
    print(client.recv(2048).decode(FORMAT))  # Recebe a mensagem de confirmação do servidor


#  Enviando mensagens
send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Rafael!")

send(DISCONNECT_MESSAGE)
