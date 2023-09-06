#!/usr/bin/python2
#coding=utf-8
import socket
import subprocess
import sys
from datetime import datetime

# Rotina para realizar scan nas portas TCP de um host
def scanHost(ip):
	# Mostra tela com dados do host sendo testado
	print "------------------------------------------------------------"
	print "Aguarde, testando host", ip
	print "------------------------------------------------------------"

	# Uso da rotina range para indicar portas (todas as portas entre 1 e 1024)
	for porta in range(1,1025):  
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ret = sock.connect_ex((ip, porta))
		if ret == 0:
			print "Porta {}: 	 Aberta".format(porta)
		sock.close()

# Limpa tela
subprocess.call('clear', shell=True)

# Solicita host a ser consultado
host = raw_input("Informe o host a ser consultado: ")

# Armazena momento que o teste inicia
t1 = datetime.now()

try:
	scanHost(socket.gethostbyname(host))

# Captura e trata eventuais erros
except KeyboardInterrupt:
	print "Encerramento solicitado via Ctrl+C"
	sys.exit()

except socket.gaierror:
	print "Não foi possível resolver o nome do host"
	sys.exit()

except socket.error:
	print "Não foi possível conectar ao host"
	sys.exit()

# Armazena momento de final do teste
t2 = datetime.now()

# Calcula o tempo gasto
total =  t2 - t1

# Apresenta tempo total gasto
print 'Scanning concluído em: ', total
