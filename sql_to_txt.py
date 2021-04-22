


from ques_db import ques_db 

db = ques_db()
db.cursor.execute(''' SELECT 
                        *
                        FROM scrapes 
                        where website = 'quora' 
                        ''' 
                        )

with open('quora_scrape_2 copy.txt', 'a') as f:
    for line in db.cursor.fetchall():
        f.write(line['question'] + '\n')

