import os
import time 
import subprocess
import datetime

while True:
    print(datetime.datetime.now())
    os.system('bash update_website.sh') 
    time.sleep(60)
