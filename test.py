import pandas as pd
import numpy as np
import gensim
from gensim import corpora, models
from pprint import pprint
import re
from gensim.utils import simple_preprocess

#dianetics = pd.read_table('Dianetics.txt', sep='\n', header=None, engine='c', encoding = 'utf-16')




with open('test.txt', 'r') as t:
    tt = t.read().split()
    
    
    
dc = {}
for i in tt:
    re.sub(r'[^\w\s]+|[\d]+', r'',i).strip()
    #re.sub(r"[#%!@*]", "", i)
    dc[i] = dc.get(i, 0) + 1
#print(dc)


k = [" lkjf.df/////./.f/", "[][]asf[a]sd]f"]
for i in k:
    re.sub(r'[^\w\s]+|[\d]+', r'', i).strip()
    print(i)

print(re.sub(r'[^\w\s]+|[\d]+', r'', "slkfjasfm..s.df.a sd/f.a/s.dfas/").strip())