import pandas as pd
import numpy as np
import gensim
from gensim import corpora, models
from pprint import pprint
import re
from gensim.utils import simple_preprocess
import plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot

# Использование cufflinks в офлайн-режиме
#import cufflinks
#cufflinks.go_offline()

# Настройка глобальной темы cufflinks
#cufflinks.set_config_file(world_readable=True, theme='pearl', offline=True)
# задаем некоторые настройки pandas, регулирующие
# формат вывода
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

# импортируем matplotlib для построения графиков
import matplotlib.pyplot as plt

#dianetics = pd.read_table('Dianetics.txt', sep='\n', header=None, engine='c', encoding = 'utf-16')




with open('Dianetics.txt', 'r', encoding = 'utf-16') as dianetics:
    dntx = re.sub(r'[^\w\s]+|[\d]+', r'', dianetics.read().strip()).lower()
    dntx = re.sub(r'\([^()]_*\)', '', dntx).split() # убрали всё лишнее из нашего текста
d = {}
for i in dntx:
    d[i] = d.get(i, 0) + 1 # создали словарь
list_d = list(d.items())
list_d.sort(key=lambda i: i[1]) # посортируем значения по возрастанию
rev_lst = list_d[::-1]
top_100_words = rev_lst[:100]
df = pd.DataFrame(top_100_words, columns=["words", "words frequency"])
grouped = df.groupby(["words"])

df_with_index = df.set_index(['words'])

df_with_index.plot()
plt.xticks(rotation=90) 

