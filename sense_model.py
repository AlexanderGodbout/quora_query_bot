import numpy as np

from ques_db import ques_db, Table
import re 

def import_word_graph():  
    pass 

def clean_word_list(words):
    result = []
    for word in words:
        if word in (''): continue
        word = word.lower()
        word = re.sub(r'[^\w\s]', '', word)
        result.append(word)
    return result 

def add_to_words_graph(word_graph, words):
    prev_word = words[0]
    for word in words[1::]:
        if word in word_graph:
            if prev_word in word_graph[word]:
                word_graph[word][prev_word] = word_graph[word][prev_word] + 1
            else:
                word_graph[word] = {**word_graph[word], **{prev_word:1}}
        else: 
            word_graph[word] = {prev_word:1}
        prev_word = word
    return word_graph 
    

def get_questions(qty):
    db = ques_db()
    gens = db.cursor.execute('''   
                            SELECT 
                                question
                            FROM scrapes
                            WHERE website = "reddit"
                            LIMIT ''' + str(qty) 
                    )
    return db.cursor.fetchall()


from datetime import datetime
start_time = datetime.now()

text = ''
qty = 100000
for question in get_questions(qty):
    text = text + ' ' + question['question']
words = text.split(' ')
words = clean_word_list(words)
word_graph = add_to_words_graph({}, words)

print(len(word_graph.keys()))
for key, associations in word_graph.items():
    for word, dist in associations.items():
        if dist == 2: 
            pass
print(datetime.now() - start_time)
print(qty)
