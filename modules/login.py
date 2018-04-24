import getpass
import sys
import os
import pymysql.cursors
from ftp import ftp_connect
from prettytable import PrettyTable

conn = pymysql.connect(host='localhost', user='root', password='', db='python', autocommit=True)
a = conn.cursor()

def login():
    while True:
        username = input("Username: ")
        password = getpass.getpass('Digite sua senha: ')
        #h = hashlib.md5(password.encode()) h.hexdigest()
        if(a.execute("SELECT * FROM `usuarios` WHERE `email`='"+ username +"'AND `senha`='"+ password +"'")):
            conn.commit()
            os.system('cls') 
            print ("Login com sucesso")
            menuLogin()
            
            break   
        else:
            conn.commit()
            print("Falha no login")

def menuLogin():
    while True:
        comando = input("Entre com o comando: ")
        commands = comando.split()
        if commands[0] == 'help':
            os.system('cls')
            print("Comandos permitidos")
            print("exit \tuse o comando EXIT para sair do sistema.\n")
            
        elif commands[0] == 'ftp':
            os.system('cls')
            ftp_connect()

        elif commands[0] == 'usuarios':
            os.system('cls')
            sql = 'SELECT id, nome, email FROM `usuarios`;'
            a.execute(sql)
            data = a.fetchall()
            
            t = PrettyTable(['id', 'nome', 'email'])
            for row in data:
                t.add_row(row)
            print(t)

        elif commands[0] == 'exit':
            #conn.close()
            break

        else:
            os.system('cls')
            print('Comando invalido')