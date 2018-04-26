import getpass
import sys
import os
import pymysql.cursors
from prettytable import PrettyTable
from login import login

conn = pymysql.connect(host='localhost', user='root', password='', db='python', autocommit=True)
a = conn.cursor()

def cadastro():
	while True:
		name = input("Nome: ")
		email = input("Email: ")
		password = getpass.getpass('Digite sua senha: ')
		if(a.execute("SELECT * FROM `usuarios` WHERE `email`='"+email+"'")):
			print("Ja existe um registro com esse email");
		else:
			a.execute("INSERT INTO `usuarios` (nome, email, senha) VALUES (%s, %s, %s)",(name, email, password));
			conn.commit()
			os.system("cls");
			menuCadastro();


def menuCadastro():
	while True:
		comando = input("Entre com o comando: ")
		commands = comando.split()
		if commands[0] == 'help':
		    os.system('cls')
		    print("Comandos permitidos")
		    print("exit \tuse o comando EXIT para sair do sistema.\n")
		    
		elif commands[0] == 'login':
		    os.system('cls')
		    login()

		elif commands[0] == 'exit':
		    #conn.close()
		    break

		else:
		    os.system('cls')
		    print('Comando invalido')