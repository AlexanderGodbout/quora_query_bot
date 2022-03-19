
#!/usr/bin/python3

import pymysql

from secrets import db_cred
class ques_db: 
    def __init__(self): 
        db = pymysql.connect(
                    host="mysql.queryquarry.tech"
                    ,user= db_cred['user'] 
                    ,passwd= db_cred['passwd'] 
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

        if table == 'gens': 
            self.desc = { 
                'id':               'INT AUTO_INCREMENT PRIMARY KEY' 
                ,'scrape_group':    'VARCHAR(255)'
                ,'question':        'VARCHAR(255)'
                ,'model':           'VARCHAR(255)'
                ,'params':          'VARCHAR(255)'
                ,'version':         'VARCHAR(255)'
                ,'timestamp':       'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
            }

    
        if table == 'evals': 
            self.desc = { 
                'id':               'INT AUTO_INCREMENT PRIMARY KEY' 
                ,'eval_group':      'VARCHAR(255)'
                ,'gen_id':          'INT NOT NULL REFERENCES gen(id)'
                ,'eval_model':      'VARCHAR(255)'
                ,'eval_params':     'VARCHAR(255)'
                ,'is_postable':     'TINYINT(1)'
                ,'version':         'VARCHAR(255)'
                ,'timestamp':       'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
            }


        if table == 'posts': 
            self.desc =  {
                'id':               'INT AUTO_INCREMENT PRIMARY KEY' 
                ,'gen_id':          'INT NOT NULL REFERENCES gen(id)'
                ,'account':         'VARCHAR(255)'
                ,'is_grammatical':  'TINYINT(1)'
                ,'is_unique':       'TINYINT(1)'
                ,'is_posted':       'TINYINT(1)'
                ,'version':         'VARCHAR(255)'
                ,'timestamp':       'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
            }


        if table == 'benchmarks': 
            self.desc =  {
                'id':                 'INT AUTO_INCREMENT PRIMARY KEY' 
                ,'earnings':          'DECIMAL(12, 2)'
                ,'question':          'VARCHAR(255)'
                ,'ask_date':          'DATE'
                ,'topics':            'VARCHAR(255)'
                ,'answer_count':      'INT'
                ,'request_count':     'INT'
                ,'followers':         'INT'
                ,'views':             'INT'
                ,'ad_impressions':    'INT' 
                ,'traffic_sources':   'VARCHAR(255)'
                ,'question_earnings': 'DECIMAL(12, 2)'
                ,'request_earnings':  'DECIMAL(12, 2)'
                ,'version':           'VARCHAR(255)'
                ,'timestamp':         'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
            }

        if table == 'groups': 
            self.desc = { 
                'item_id':          'INT' 
                ,'group_name':      'VARCHAR(255)'
                ,'item_tbl':        'VARCHAR(255)'
                ,'group_tbl':       'VARCHAR(255)'
            }
    
def create_database(): 

    db = ques_db()
    db.create_table(Table('scrapes')) 
    db.create_table(Table('posts') )
    db.create_table(Table('benchmarks'))
    db.create_table(Table('gens'))
    db.create_table(Table('groups'))


#create_database() 



