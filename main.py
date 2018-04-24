import pymysql.cursors
import getpass
import ftplib
import os
import hashlib
import sys
import time

sys.path.append('modules')
from carrega import progress
from command import menu

def main():
    os.system('cls')
    print("Carregando")
    progress()
    os.system('cls')
    print("""
    _              _      ___  ____  
   / \   _ __ ___ | |__  / _ \/ ___| 
  / _ \ | '_ ` _ \| '_ \| | | \___ \ 
 / ___ \| | | | | | |_) | |_| |___) |
/_/   \_\_| |_| |_|_.__/ \___/|____/ 
    """)
    menu()

try:
    main()

except (KeyboardInterrupt):
    os.system('cls')
    print ("Voce pressionou Ctrl+C ou Delete para interromper este programa!")