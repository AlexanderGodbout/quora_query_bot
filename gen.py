# gen

import gpt_2_simple as gpt2
from datetime import datetime
import random 
from ques_db import ques_db, Table


def gen_questions(generator, params):
    generators = {
        'Alex_gen': Alex_gen
        ,'GPT_gen': GPT_gen
    }
    return generators[generator](params)

def Alex_gen(params):
    # Uses CLI to collect a user-generated question
    db = ques_db()
    db.cursor.execute(''' SELECT r1.id, r1.question
                            FROM scrapes AS r1 JOIN
                            (SELECT CEIL(RAND() *
                                        (SELECT MAX(id)
                                        FROM scrapes)) AS id)
                                AS r2
                            WHERE r1.id >= r2.id
                            ORDER BY r1.id ASC
                            LIMIT 10
                    ''')
    gens = []
    for scrape in db.cursor.fetchall(): 
        print('\n',scrape['question'])
        gens.append(
            {
            'scrape_group': 'AG1_' + scrape['id']
            ,'question': input()
            }
        )
    return gens


def GPT_gen(params):
    #Use GPT2 to generate questions 

    #gpt2.download_gpt2(model_name="124M")
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(
        sess
        ,checkpoint_dir="/Users/alexandergodbout/Documents/Grammarism/Code/Quora_Query_Bot/checkpoint/checkpoint_gpt2_v4"
        ,run_name="run1"
        ,model_name=None
        ,model_dir='models'
        ,multi_gpu=False
        )

    questions = gpt2.generate(
            sess
            ,run_name= params['run_name']
            ,checkpoint_dir= params['checkpoint_dir'] 
            ,model_name= params['model_name'] 
            ,model_dir= params['model_dir']
            ,sample_dir= params['sample_dir']
            ,return_as_list= params['return_as_list']
            ,truncate= params['truncate']
            ,destination_path= params['destination_path']
            ,sample_delim= params['sample_delim']
            ,prefix= params['prefix']
            ,seed= params['seed']
            ,nsamples= params['nsamples']
            ,batch_size= params['batch_size']
            ,length= params['length']
            ,temperature= params['temperature']
            ,top_k= params['top_k']
            ,top_p= params['top_p']
            ,include_prefix= params['include_prefix']
        )

    gens = []
    ques_list = questions[0].split('\n')
    for question in ques_list:
        gens.append(
            {
                'scrape_group': 'quora_gpt2_1'
                ,'question': question
            }
        ) 
    return gens 


if __name__ == "__main__":
    db = ques_db()
  
    model = 'GPT_gen'

    params = {
            'run_name': 'run1'
            ,'checkpoint_dir': "/Users/alexandergodbout/Documents/Grammarism/Code/Quora_Query_Bot/checkpoint/checkpoint_gpt2_v4" 
            ,'model_name': None
            ,'model_dir': 'models'
            ,'sample_dir': 'samples'
            ,'return_as_list': True
            ,'truncate': None
            ,'destination_path': None
            ,'sample_delim': '=' * 20 + '\n'
            ,'prefix': None
            ,'seed': None
            ,'nsamples': 1
            ,'batch_size': 1
            ,'length': 1023
            ,'temperature': 0.8
            ,'top_k': 0
            ,'top_p': 0.0
            ,'include_prefix': True
    }
    print(model)

    records = []
    for gens in gen_questions(model, params) : 
        print(gens['question'])
        record= {
                'scrape_group': gens['scrape_group']
                ,'question': gens['question']
                ,'model': model 
                ,'params': params
                ,'version': '0.0.0.0'
                ,'timestamp':'Now()'
                }
        records.append(record)
    if records: db.insert(Table('gens'), records)

