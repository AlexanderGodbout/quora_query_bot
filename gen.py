# predict


def gen_question(generator, question):
    generators = {
        'Alex_gen': Alex_gen
        ,'GPT_gen': GPT_gen
    }
    return generators[generator](question)

def Alex_gen(ref_ques):
    # Uses CLI to collect a user-generated question
    print('\n',ref_ques)
    return input()

def GPT_gen(ref_ques):
    return ''

if __name__ == "__main__":
    from ques_db import ques_db, Table
    import random 

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
    scrapes = db.cursor.fetchall()

    records = []
    model = 'Alex_gen'
    for scrape in scrapes:
        new_question = gen_question(model, scrape['question'])  
        record= {
                'scrape_id': scrape['id']
                ,'question': new_question
                ,'model': model 
                ,'params': ''
                ,'version': '0.0.0.0'
                ,'timestamp':'Now()'
                }
        records.append(record)
    if records: db.insert(Table('gens'), records)

