type = raw_input("HTTP, FTP ou SMTP?\n")
while (not type.upper() in ['HTTP', 'FTP', 'STMP']):
	type = raw_input("Por favor, coloque um protocolo valido (HTTP, FTP ou STMP)\n")
if type.upper() == "HTTP":
	method = raw_input("Metodo (GET OU POST):\n")
	url = raw_input("Endereco:\n")
	requisicao = method + " " + url + " " + "HTTP/1.1"
	 
