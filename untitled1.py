import pandas as pd
import numpy as np
import gensim
from gensim import corpora, models
from pprint import pprint
import re
from gensim.utils import simple_preprocess
# How to create a dictionary from a list of sentences?
documents = ["The Saudis are preparing a report that will acknowledge that", 
             "Saudi journalist Jamal Khashoggi's death was the result of an", 
             "interrogation that went wrong, one that was intended to lead", 
             "to his abduction from Turkey, according to two sources."]
documents_2 = ["One source says the report will likely conclude that", 
                "the operation was carried out without clearance and", 
                "transparency and that those involved will be held", 
                "responsible. One of the sources acknowledged that the", 
                "report is still being prepared and cautioned that", 
                "things could change."]
# Tokenize(split) the sentences into words
texts = [[text for text in doc.split()] for doc in documents]
# Create dictionary
dictionary = corpora.Dictionary(texts)
# Get information about the dictionary
print(dictionary)

# List with 2 sentences
my_docs = ["Who let the dogs out?",
           "Who? Who? Who? Who?"]
# Tokenize the docs
tokenized_list = [simple_preprocess(doc) for doc in my_docs]
# Create the Corpus
mydict = corpora.Dictionary()
mycorpus = [mydict.doc2bow(doc, allow_update=True) for doc in tokenized_list]
pprint(mycorpus)
word_counts = [[(mydict[id], count) for id, count in line] for line in mycorpus]
#pprint(word_counts)
#> [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], [(4, 4)]]