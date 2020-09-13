import pandas as pd
import numpy as np
import gensim
from gensim import corpora, models
from pprint import pprint
import re
from gensim.utils import simple_preprocess

#dianetics = pd.read_table('Dianetics.txt', sep='\n', header=None, engine='c', encoding = 'utf-16')




with open('Dianetics.txt', 'r', encoding = 'utf-16') as dianetics:
    dntx = re.sub(r'[^\w\s]+|[\d]+', r'', dianetics.read().strip()).lower()
    dntx = re.sub(r'\([^()]_*\)', '', dntx).split() # убрали всё лишнее из нашего текста
d = {}
for i in dntx:
    d[i] = d.get(i, 0) + 1 # используя метод get словаря, создали словать 
    #где ключ - это слово, а значение  = количество повторов

#print(d)
    
'''texts = [[text] for text in dntx] # создали массив из слов
dictionary_dian = corpora.Dictionary(texts) # создали словарь из слов
#print(dictionary_dian)

tokenized_list = [simple_preprocess(doc) for doc in dntx] #токенизированный документ


DIC_WITH_TOKENS = dictionary_dian.token2id

mydict = corpora.Dictionary()
mycorpus = [[mydict.doc2bow(doc, allow_update=True)] for doc in tokenized_list]
pprint(mycorpus)
#word_counts = [[(mydict[id], count)] for id, count in line] for line in mycorpus]'''

"""for j in i:
        if not j.isalpha():
            pass
    i = i.replace(",", "").replace('"', "").replace(':', '').replace(";", "").\
        replace("(", "").replace(")", "").replace(".", "").replace("!", "").\
            replace("-", "").replace("^", "").replace("'", "")"""





                    
