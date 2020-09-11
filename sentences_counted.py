import pandas as pd
import numpy as np
import gensim
from gensim import corpora, models
from pprint import pprint
import re
from gensim.utils import simple_preprocess

#dianetics = pd.read_table('Dianetics.txt', sep='\n', header=None, engine='c', encoding = 'utf-16')




with open('Dianetics.txt', 'r', encoding = 'utf-16') as dianetics:
    dntx = dianetics.read()
lenth_of_sent = []
dianetics_pron = re.sub(r'[.!?]\s',r'stop_scentence', dntx)
sentences = len(dianetics_pron.split('stop_scentence'))
full_text = dianetics_pron.split('stop_scentence')
for sentence in full_text:
    lenth_of_sent.append(len(sentence))
print("Amoutn of sentences is: " + str(sentences), "quantity of words in \
      every sentence: " +  str(lenth_of_sent) )

    
                    


    
    
