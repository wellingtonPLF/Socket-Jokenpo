import socket 
import threading
import sys
from time import sleep

print("Inicializando...")
sleep(5)
print("Faça sua Escolha: [ >>> Pedra <<<|>>> Papel <<<| >>> Tesoura <<< ]\n")

class Cliente():
	def __init__(self, host = "192.168.25.95", port =3022):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)
	
		msg_recv.daemon = True
		msg_recv.start()

		while True:
			msg = input("")
			print("Carregando ...\n")
			sleep(5)
			if msg != "Sair":
				self.send_msg(msg)
			else:
				print("\n--- Jogo Finalizado ---\n")
				self.sock.close()
				sys.exit()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print("[*] Resultado:",bytes.decode(data),"\n\nFaça sua Escolha [Pedra,Papel e Tesoura] ou [Sair]:\n")
			except:
				pass	
	def send_msg(self, msg):
		self.sock.send(str.encode(msg))

c = Cliente()
