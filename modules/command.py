from login import login
import os
import sys

def menu():
    while True:
        print("Use help para ver os comandos")
        comando = input("Entre com o comando: ")
        commands = comando.split()
        if commands[0] == 'help':
            os.system('cls')
            print("Comandos permitidos")
            print("login \tuse o comando LOGIN para fazer o login no sistema caso nao \n\ttenha uma conta acesse...\n")
            print("cadastro \tuse o comando CADASTRO para fazer o cadastro no sistema \n")
            print("exit \tuse o comando EXIT para sair do sistema.\n")
            
        elif commands[0] == 'login':
            login()

        elif commands[0] == 'cadastrar':
            cadastro()

        elif commands[0] == 'editor':
            from editor import MainWindow
            del sys.modules["editor"]

        elif commands[0] == 'exit':
            #conn.close()
            break

        else:
            os.system('cls')
            print('Comando invalido opções validas(login, exit)')