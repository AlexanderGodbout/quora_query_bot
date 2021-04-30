
from ques_db import ques_db, Table

from datetime import date




def get_gens(qty):
    db = ques_db()
    gens = db.cursor.execute('''   
                            SELECT 
                                id
                                ,question
                            FROM gens
                            WHERE id NOT IN (
                                SELECT 
                                    gen_id 
                                from evals 
                            )
                            LIMIT ''' + str(qty) 
                    )
    return db.cursor.fetchall()


def alex_eval(gen, params):
    # Use CLI to determine if gen is postable
    print(gen)
    if input() == 'y':
        return {'is_postable': 1}
    return {'is_postable': 0}


def get_eval(model, params, gen): 
    eval_dispatcher = {
        'alex': alex_eval
        }
    return eval_dispatcher[model](gen, params)


if __name__ == '__main__':

    qty = 100
    model = 'alex'
    params = ''

    records = []
    for gen in get_gens(qty): 
        eval = get_eval(model, params, gen['question'])
        record= {
                'eval_group': date.today().strftime("%m/%d/%y") + "_" + str(qty)
                ,'gen_id': gen['id']
                ,'eval_model': model 
                ,'eval_params': params
                ,'eval': eval
                ,'is_postable': eval['is_postable']
                ,'version': '0.0.0.0'
                ,'timestamp':'Now()'
                }
        records.append(record)
    db = ques_db()
    if records: db.insert(Table('evals'), records)
