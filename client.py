from socket import *

type = raw_input("HTTP, FTP ou SMTP?\n")
while (not type.upper() in ['HTTP', 'FTP', 'SMTP']):
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
	message = raw_input('Digite seu comando (para sair, q):\n')
	while message != "q":
		clientSocket.send(message + "\r\n")

		# if(message == "LIST"):
		# 	serverPort2 = 20
		# 	dataSocket = socket(AF_INET, SOCK_STREAM)
		# 	dataSocket.connect((serverName,serverPort2))
		# 	reply = dataSocket.recv(65535)

		reply = clientSocket.recv(65535)
		# if not reply:
		# 	break
		# if '220 Only anonymous FTP is allowed here' in reply:
		# 	clientSocket.send(message)
		# 	break
		print reply
		message = raw_input('Digite seu comando (para sair, q):\n')
	print reply
if type.upper() == "SMTP":
	email_from = raw_input('Digite seu email\n')
	email_to = raw_input('Digite o email do destinatario\n')
	email_subject = raw_input('Digite o assunto\n')
	email_message = raw_input('Digite a mensagem\n')
	serverName = "smtp.gmail.com"
	serverPort = 465
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))

	print "CHEGOU AQUI"
	message = raw_input("Digite sua msg para o servidor\n")
	clientSocket.send(message + "\r\n")

	modifiedSentence = clientSocket.recv(1024)
	print modifiedSentence
	# print 'From Server:', modifiedSentence
	clientSocket.close()


