import sys
import time

def progress():
    for i in range(70+1):
        time.sleep(0.1)
        sys.stdout.write(('▀'*i)+(''*(20-i))+("\r [ %d"%i+"% ] "))
        sys.stdout.flush()