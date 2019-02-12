import socket 
import threading 
import sys

class Servidor():
	
	def __init__(self, host = "192.168.25.95", port = 3022):

		self.clientes = []
		self.result = []
		self.x = 0
	
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host),int(port)))
		self.sock.listen(2)
		self.sock.setblocking(False)
		
		concordar = threading.Thread(target = self.aceitar)
		processar = threading.Thread(target = self.processando)

		concordar.daemon = True
		concordar.start()
		
		processar.daemon = True
		processar.start()
		
		while True:
			msg = input("[*]")
			if msg == "sair":
				self.sock.close()
				sys.exit()
			else:
				pass

	def msg_to_client(self,cliente):
		for c in self.clientes:
			try:	
				if c == cliente:
					c.send(str.encode("Vc venceu"))
				if c!= cliente:
					if cliente == "empate":
						c.send(str.encode("Empate"))
					else:
						c.send(str.encode("Vc perdeu"))
			except:
				self.clientes.remove(c)

	def aceitar(self):
		print("aceitar iniciado")
		while True:
			try:
				cnx, addr = self.sock.accept()
				cnx.setblocking(False)
				self.clientes.append(cnx)
			except:
				pass
		
	def processando(self):
		print("Processando inciado")
		while True:
			if len(self.clientes)>1:
				for c in self.clientes:
					try:
						data = c.recv(1024)
						if data:
							self.result.append(bytes.decode(data))
						if len(self.result) == 2:
							if self.result[0] == "Pedra" and self.result[1] == "Papel":
								self.msg_to_client(c)
							if self.result[0] == "Tesoura" and self.result[1] == "Pedra":
								self.msg_to_client(c)
							if self.result[0] == "Papel" and self.result[1] == "Tesoura":
								self.msg_to_client(c)
							if self.result[0] == "Papel" and self.result[1] == "Pedra":
								self.msg_to_client(self.clientes[0])
							if self.result[0] == "Tesoura" and self.result[1] == "Papel":
								self.msg_to_client(self.clientes[0])	
							if self.result[0] == "Pedra" and self.result[1] == "Tesoura":
								self.msg_to_client(self.clientes[0])
							if self.result[0] == self.result[1]:
								self.msg_to_client("empate")
								
							self.result = []
					except:
						pass

s = Servidor()
