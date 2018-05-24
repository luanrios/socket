from socket import *
import smtplib
import getpass

type = raw_input("HTTP, FTP ou SMTP?\n")
while (not type.upper() in ['HTTP', 'FTP', 'SMTP']):
	type = raw_input("Por favor, coloque um protocolo valido (HTTP, FTP ou STMP)\n")
if type.upper() == "HTTP":
	# PORTA 80
	serverPort = raw_input("Digite a porta:\n")
	serverName = raw_input("Digite o servidor:\n")
	clientSocket = socket(AF_INET, SOCK_STREAM) 
	clientSocket.connect((serverName,int(serverPort)))
	requisicao1 = raw_input('Coloque sua requisicao GET/POST\n')
	#"GET /index.html HTTP/1.1\r\n"
	requisicao2 = raw_input('Coloque sua requisicao hostname\n')
	requisicao1 = requisicao1 + "\r\n" + requisicao2 + "\r\n\r\n"

	#requisicao + "Host: " + serverName + "\r\n\r\n"
	# Host: www.serversmtp.com\r\n\r\n
	clientSocket.send(requisicao1)
	# Host: www.someschool.edu
	serverResponse = clientSocket.recv(1024)
	print serverResponse

	clientSocket.close()
"""
	requisicao = method.upper() + " " + url + " " + "HTTP/1.1\r\n"
	requisicao = requisicao + "Host: " + host + "\r\n\r\n"
	serverName = host
	print requisicao
	clientSocket.send(requisicao)
	modifiedSentence = clientSocket.recv(1024)
	print 'From Server:', modifiedSentence
"""

if type.upper() == "FTP":
	#serverName = 'ftp.cs.brown.edu'
	serverName = raw_input('Digite o servidor\n')
	#serverPort = 21
	serverPort = raw_input('Digite a porta\n')
	serverPort = int(serverPort)

	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName,serverPort))

	# Grab initial message
	reply = clientSocket.recv(65535)
	print reply

	clientSocket.close()
	
	# Anonymous login
"""
	login = "USER anonymous\r\n"
	print("ftp> " + login)
	clientSocket.send(login)
	reply = clientSocket.recv(65535)
	print reply
"""

	# Establish passive connection
"""
	message = "PASV\r\n"
	print("ftp> " + message)
	clientSocket.send(message)
	reply = clientSocket.recv(65535)
	print reply
	ports = re.findall('[\d]+', reply)
	# print(ports)
	# Calculate passive port on server
	data_port = int(ports[5]) * 256 + int(ports[6])
	print("Data Port: " + str(data_port))
	# Connect to PASV port
	dataSocket = socket(AF_INET, SOCK_STREAM)
	dataSocket.connect((serverName, data_port))
"""

"""
	data_commands = ["LIST", "GET"]
	
	while True:
		message = raw_input('ftp> ')
		clientSocket.send(message + "\n")

		if(message in data_commands):
			reply = dataSocket.recv(65535)
		elif message == "QUIT":
			reply = clientSocket.recv(65535)
			print reply
			break
		else:
			reply = clientSocket.recv(65535)
			
		print reply
"""

if type.upper() == "SMTP":

	smtp_server = raw_input('Digite o servidor SMTP\n')
	print smtp_server
	# Conexao SMTP segura (TLS/SSL) - porta:587 e inicia TLS
	print smtplib.SMTP(smtp_server, 587)
	#clientSocket.starttls()

	#Autenticacao e Login
	email_username = raw_input('Digite seu email\n')
	email_password = getpass.getpass('Digite sua senha\n')
	clientSocket.login(email_username,email_password)

	#Mensagem
	email_to = raw_input('Digite o email do destinatario\n')
	email_subject = raw_input('Digite o assunto\n')
	email_body = raw_input('Digite a mensagem\n')

	#Envia o email e encerra a conexao
	message = "From: " + email_username + "\r\n" + "To: " + email_to + "\r\n" + "Subject: " + email_subject + "\r\n\n" + email_body
	clientSocket.sendmail(email_username, email_to, message)
	clientSocket.quit()
	
	#email_username = raw_input('testando.protocolo.smtp@gmail.com')