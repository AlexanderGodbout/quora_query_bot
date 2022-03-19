
from ques_db import ques_db, Table

from datetime import date
import language_tool_python



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


def naive_eval(gen, param):
    # Eval using simple string matching 
    print(gen) 
    if "quora" not in gen.lower() and len(gen) < 120: 
        return {'is_postable': 1}
    return {'is_postable': 0}

def grammar_eval(gen, param): 
    # Eval using the LanguageTool
    print(gen)
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(gen)
    if len(matches) == 0: 
        return {'is_postable': 1}
    return {'is_postable': 0}



def get_eval(model, params, gen): 
    eval_dispatcher = {
        'alex': alex_eval
        ,'naive': naive_eval 
        ,'grammar': grammar_eval
        }
    return eval_dispatcher[model](gen, params)


if __name__ == '__main__':

    qty = 100
    model = 'grammar'
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
