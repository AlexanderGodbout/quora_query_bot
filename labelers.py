# label 


import bs4 as bs
import os 
import pickle
from PyDictionary import PyDictionary


def get_OPTED_dictionary():
    path  = '/Users/alexandergodbout/Documents/Grammarism/Code/Quora_Query_Bot/data/OPTED/v003/'
    POS_dict= {}
    for filename in os.listdir(path): 
        if '.html' not in filename: continue 
        with open(path+filename, 'rb') as file: 
            soup = bs.BeautifulSoup(file, features='lxml')
            for entry in soup.find_all('p'): 
                try: 
                    word = entry.find('b').text
                    POS = entry.find('i').text.replace('.','').replace(' ','').split('&').split(',')
                    POS_dict[word] = POS_dict.get(word, set()).union(set(POS))
                except: 
                    print("skip")
    return POS_dict 
        
def misc():
    with open('POS_dict.p', 'wb') as fp:
        pickle.dump(get_OPTED_dictionary(), fp, protocol=pickle.HIGHEST_PROTOCOL)


    with open('POS_dict.p', 'rb') as fp:
        data = pickle.load(fp)

    POS_count = {}
    for word, pos_group in data.items(): 
        #if 'pl' in pos_group: print(word)
        for pos in pos_group: 
            POS_count[pos] = POS_count.get(pos, 0) + 1
        #POS_set = POS_set.union(set(pos_group))

    for pos in sorted(POS_count):
        #if POS_count[pos] > 100: print(pos, POS_count[pos])  
        #print(pos, POS_count[pos])  
        pass 
    print(list(data['The']))
    print('and&the,ok/yes'.split('&'))

def label_grammatical(question): 
    return 1

def label_uniqueness(question): 
    return 1

def label_virality(question):
    return 1

def label_obsessionality(question):
    return 1


if __name__ == "__main__":
    dictionary=PyDictionary()
    #print (dictionary.meaning("a"))
    print(dictionary.meaning("the"))
    # noun 
    # verb 
    # adjective 
    # adverb 
    # article
    sentence = "The dog barked"
    POS = ""
    for word in sentence.split(' '): 
        #print(word)
        #print(dictionary.meaning("the"))
        POS = POS + " " + list(dictionary.meaning("word").keys())[0]
    print(POS)      