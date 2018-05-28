# Linguagem de estimacao escolhida: Python
from socket import *

type = raw_input("HTTP, FTP ou SMTP?\n")
while (not type.upper() in ['HTTP', 'FTP', 'SMTP']):
	type = raw_input("Por favor, coloque um protocolo valido (HTTP, FTP ou STMP)\n")

# Codigo caso a requisicao seja valida
if (type.upper() == "HTTP" or type.upper() == "FTP" or type.upper() == "SMTP"):
	serverName = raw_input("Digite o servidor:\n")
	serverPort = raw_input("Digite a porta:\n")

	# Cria o socket do cliente
	# AF_INET     => rede utilizando IPv4
	# SOCK_STREAM => socket TCP
	clientSocket = socket(AF_INET, SOCK_STREAM) 

	# Estabelece a conexao TCP com o servidor
	clientSocket.connect((serverName,int(serverPort)))

# Codigo Protocolo HTTP
if type.upper() == "HTTP":
	requisicao = raw_input('Digite sua requisicao: ')
	requisicao = requisicao + "\r\n" + 'Host: ' + serverName + "\r\n\r\n"

	# Envia a requisicao para o servidor
	clientSocket.send(requisicao)
	# Recebe a resposta 
	serverResponse = clientSocket.recv(1024)
	print '\nhttp> ' + serverResponse + '\n'
	# Fecha a conexao TCP entre cliente e o servidor
	clientSocket.close()

# Codigo Protocolo FTP
if type.upper() == "FTP":
	serverResponse = clientSocket.recv(1024)
	print '\nftp> ' + serverResponse + '\n'

	requisicao = raw_input('Digite sua requisicao: ')
	requisicao = requisicao + "\r\n"

	# Envia a requisicao FTP para o servidor
	clientSocket.send(requisicao)
	# Recebe a resposta
	serverResponse = clientSocket.recv(1024)
	print '\nftp> ' + serverResponse + '\n'
	# Fecha a conexao TCP entre cliente e o servidor
	clientSocket.close()

# Codigo Protocolo SMTP
if type.upper() == "SMTP":
	serverResponse = clientSocket.recv(1024)
	print '\nsmtp> ' + serverResponse + '\n'

	requisicao = raw_input('Digite sua requisicao: ')
	requisicao = requisicao + "\r\n"
	# Envia a requisicao SMTP para o servidor
	clientSocket.send(requisicao)
	# Recebe a resposta
	serverResponse = clientSocket.recv(1024)
	print '\nsmtp> ' + serverResponse + '\n'
	# Fecha a conexao TCP entre cliente e o servidor
	clientSocket.close()
