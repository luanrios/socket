from socket import *

type = raw_input("HTTP, FTP ou SMTP?\n")
while (not type.upper() in ['HTTP', 'FTP', 'STMP']):
	type = raw_input("Por favor, coloque um protocolo valido (HTTP, FTP ou STMP)\n")
if type.upper() == "HTTP":
	method = raw_input("Metodo (GET OU POST):\n")
	host = raw_input("Nome do Hospedeiro:\n")
	url = raw_input("Nome do Caminho:\n")
	requisicao = method.upper() + " " + url + " " + "HTTP/1.1\r\n"
	requisicao = requisicao + "Host: " + host + "\r\n\r\n"
	serverName = host
	serverPort = 80
	clientSocket = socket(AF_INET, SOCK_STREAM) 
	clientSocket.connect((serverName,serverPort))
	print requisicao
	clientSocket.send(requisicao)
	modifiedSentence = clientSocket.recv(1024)
	print 'From Server:', modifiedSentence
	clientSocket.close()
if type.upper() == "FTP":
	serverName = 'ftp.rediris.es'
	serverPort = 21
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))
	reply = ''
	message = "LIST\r\n"
	while True:
		reply = reply + clientSocket.recv(1024)
		if not reply:
			break
		if '220 Only anonymous FTP is allowed here' in reply:
			clientSocket.send(message)
			break
	reply = reply + clientSocket.recv(65535)
	print reply