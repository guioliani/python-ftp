import getpass
import ftplib
import os
import shutil

def ftp_connect():
    while True:
        site_address = input('Entre com o endereço do FTP: ')
        ftp_usuario = input('Entre com o usuario do FTP: ')
        ftp_senha = getpass.getpass('Entre com a senha do FTP: ')
        try:
            with ftplib.FTP(site_address) as ftp:
                ftp.login(ftp_usuario, ftp_senha)
                print(ftp.getwelcome())
                print("\n")
                print("╔════════════════════════════════════════════════════════════════════════════╗")
                print('Diretorio atual', ftp.pwd())
                ftp.dir()
                print("╚════════════════════════════════════════════════════════════════════════════╝")
                print("\n")
                print("""\t\t\t
                
    _              _     _____ _____ ____  
   / \   _ __ ___ | |__ |  ___|_   _|  _ \ 
  / _ \ | '_ ` _ \| '_ \| |_    | | | |_) |
 / ___ \| | | | | | |_) |  _|   | | |  __/ 
/_/   \_\_| |_| |_|_.__/|_|     |_| |_|    
                                          
                """)
                print('comandos validos /cd /get /upload /ls /delete /mkdir /rmdir /exit ex: get readme.txt')
                ftp_command(ftp)
                break 
        except ftplib.all_errors as e:
            print('falha na conexao verifique o endereço FTP.', e)


def ftp_command(ftp):
    while True:
        command = input('FTP>> ')
        commands = command.split()
        if commands[0] == 'cd':
            try:
                ftp.cwd(commands[1])
                os.system('cls')
                print("╔════════════════════════════════════════════════════════════════════════════╗")
                print('Diretorio: ', ftp.pwd())
                ftp.dir()
                print('\n\t\t\tdiretorio atual', ftp.pwd())
                print("╚════════════════════════════════════════════════════════════════════════════╝")
            except ftplib.error_perm as e:
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'diretorio nao existe ou nao tem permissao')
       
        elif commands[0] == 'get':#get nome arquivo
            try:
                ftp.retrbinary('RETR ' + commands[1], open(commands[1], 'wb').write)
                arquivoDownload = commands[1]
                destino = "arquivos/download/"
                shutil.move(arquivoDownload, destino)
                print('download feito com sucesso')
            except ftplib.error_perm as e:
                error_code = str(e).split(None, 1)
                if error_code[0] == '550':
                    print(error_code[1], 'arquivo nao existe ou nao tem permissao')
        
        elif commands[0] == 'upload':#upload nomearquivo
            ftp.storbinary('STOR ' + commands[1], open("arquivos/upload/"+commands[1], 'rb'))        
            print('upload com sucesso')
        elif commands[0] == 'delete':#delete
            deleta = input('nome do arquivo para deletar: ')
            ftp.delete(deleta)
            print('deletado com sucesso')
        
        elif commands[0] == 'ls':
            print("╔════════════════════════════════════════════════════════════════════════════╗")
            print('diretorio: ', ftp.pwd())
            ftp.dir()
            print("╚════════════════════════════════════════════════════════════════════════════╝")

        elif commands[0] == 'mkdir':
            mkdir = input('Nome da pasta que deseja criar: ')
            ftp.mkd(mkdir)
            print('Pasta '+ mkdir + ' foi criada com sucesso')

        elif commands[0] == 'rmdir':
            rmdir = input('Nome da pasta que deseja apagar: ')
            ftp.rmd(rmdir)
            print('Pasta '+ rmdir + ' foi excluida com sucesso')
        
        elif commands[0] == 'exit':
            ftp.quit()
            os.system('cls')
            break
        
        else:
            print('comando invalido tente novamente (opcoes validas /cd /get /upload /ls /delete /mkdir /rmdir /exit')
