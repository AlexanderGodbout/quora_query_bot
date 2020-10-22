import os
import time 
import subprocess

import signal 


devnull = open('./null.txt', 'w') 
p = subprocess.Popen(["./main"], stdout=devnull, shell=False) 

pid = p.pid 

#while True: 
#    time.sleep(60)
os.system('bash update_website.sh')

time.sleep(120)
os.kill(pid, signal.SIGINT)

if not p.poll():
    print("Process correctly halted") 
