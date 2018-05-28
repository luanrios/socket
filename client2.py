from socket import *


msg = "\r\n My email's content!"
endmsg = "\r\n.\r\n"

mailserver = ("smtp.aol.com", 25) 

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after connection request:" + recv)