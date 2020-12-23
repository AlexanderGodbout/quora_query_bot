import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('scrape.py', 'scrape2.py')                                    
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python3 {}'.format(process))                                       
                                                                                
while True: 
    try:                                                                             
        pool = Pool(processes=2)                                                        
        pool.map(run_process, processes) 
    except:     
        print('Abort')