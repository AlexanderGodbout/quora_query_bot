
#!/usr/bin/python3

import pymysql

class ques_db: 
    def __init__(self): 
        db = pymysql.connect(
                    host="mysql.queryquarry.tech"
                    ,user="scopesdbu"
                    ,passwd="mmlja5ja5ja%"
                    ,db="quora_query_db" 
                    ,charset='utf8mb4'
                )
        self.cursor = db.cursor() 

    def create_table(self, desc, table): 
        query = 'CREATE TABLE IF NOT EXISTS ' + table + '(\n\t'
        for col_name, col_type in desc.items(): 
            query += col_name + ' ' + col_type + ',\n\t'
        query = query[:-3] + '\n );'
        print(query)
        #self.cursor.execute(query)

    def insert(self, data, table):
        query =  'INSERT INTO '+ table \
            +'('+ str(list(data.keys())).strip("[]").replace("'","") + ')' \
            + ' VALUES (' 
        for record in data: 
            query += str(list(data.values())).strip('[]') 
        query += + ')'

        query = query.replace('None','NULL')
        self.cursor.execute(query)


if __name__ == '__main__':

    scrapes_desc = {
        'id':           'INT AUTO_INCREMENT PRIMARY KEY' 
        ,'question':    'VARCHAR(255)'
        ,'website' :    'CHAR(10)'
        ,'topic':       'VARCHAR(255)'
        ,'version':     'VARCHAR(255)'
        ,'timestamp':   'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
    }

    posts_desc = {
        'id':               'INT NOT NULL'
        ,'account':         'VARCHAR(255)'
        ,'topics':          'VARCHAR(255)'
        ,'answers':         'INT'
        ,'followers':       'INT'
        ,'views':           'INT'
        ,'ad_impressions':  'INT'
        ,'ques_earn':       'DECIMAL(12, 2)'
        ,'req_earn':        'DECIMAL(12, 2)'
        ,'tot_earn':        'DECIMAL(12, 2)'
        ,'grammatical':     'TINYINT(1)'
        ,'unique':          'TINYINT(1)'
        ,'version':         'VARCHAR(255)'
        ,'timestamp':       'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
    }

    predicts_desc ={
        'id':               'INT NOT NULL'
        ,'pred_views':      'INT'
        ,'pred_topics':     'VARCHAR(255)'
        ,'pred_grammatical':'TINYINT(1)'
        ,'pred_unique':     'TINYINT(1)'
        ,'pred_views':      'INT'
        ,'pred_tot_earn':   'DECIMAL(12, 2)'
        ,'features_id':     'INT'
        ,'version':         'VARCHAR(255)'
        ,'timestamp':       'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
    }

    db = ques_db()
    db.create_table(scrapes_desc, 'scrapes') 
    db.create_table(posts_desc, 'posts') 
    db.create_table(predicts_desc, 'predicts') 