
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
                    ,autocommit=True
                    ,cursorclass=pymysql.cursors.DictCursor
                )
        self.cursor = db.cursor() 


    def create_table(self, Table): 
        query = 'CREATE TABLE IF NOT EXISTS ' + Table.name + '(\n\t'
        for col_name, col_type in Table.desc.items(): 
            query += col_name + ' ' + col_type + ',\n\t'
        query = query[:-3] + '\n );'
        self.cursor.execute(query)


    def insert(self, Table, records):
        query =  'INSERT INTO '+ Table.name \
            +'('+ str(list(Table.desc.keys())).strip("[]").replace("'","") + ')\n' \
            + ' VALUES \n' 
        for record in records: 
            query += '('
            for field in Table.desc.keys(): 
                cell = str(record.get(field, 'Null')).replace("'","").replace("\\","")
                cell = cell if cell in ('Null','Now()') else "'" + cell + "'"
                query +=  cell + ', '
            query = query[:-2]  + '),\n' 
        query = query[:-2] + ';'
<<<<<<< HEAD
    
=======
>>>>>>> a36acc6c74345bca4c56d30b8b41e7cb79b02920
        print(query)
        self.cursor.execute(query)


    def get_questions(self):
        pass
      

class Table: 
    def __init__(self, table): 
        self.name = table

        if table == 'scrapes': 
            self.desc = {
                'id':           'INT AUTO_INCREMENT PRIMARY KEY' 
                ,'question':    'VARCHAR(255)'
                ,'website' :    'CHAR(10)'
                ,'topic':       'VARCHAR(255)'
                ,'version':     'VARCHAR(255)'
                ,'timestamp':   'TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL'
            }

        if table == 'posts': 
            self.desc =  {
                'id':               'INT NOT NULL'
                ,'account':         'VARCHAR(255)'
                ,'is_grammatical':  'TINYINT(1)'
                ,'is_unique':       'TINYINT(1)'
                ,'is_posted':       'TINYINT(1)'
                ,'version':         'VARCHAR(255)'
                ,'timestamp':       'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
            }
        
        if table == 'benchmarks': 
            self.desc =  {
                'id':               'INT NOT NULL'
                ,'topics':          'VARCHAR(255)'
                ,'answers':         'INT'
                ,'followers':       'INT'
                ,'views':           'INT'
                ,'ad_impressions':  'INT'
                ,'ques_earn':       'DECIMAL(12, 2)'
                ,'req_earn':        'DECIMAL(12, 2)'
                ,'tot_earn':        'DECIMAL(12, 2)'
                ,'version':         'VARCHAR(255)'
                ,'timestamp':       'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
            }

        if table == 'predicts': 
            self.desc = { 
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

    
def create_database(): 

    db = ques_db()
    db.create_table(Table('scrapes')) 
    db.create_table(Table('posts') )
    db.create_table(Table('predicts'))
