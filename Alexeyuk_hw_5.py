"""
Александр Алексеюк
DS5

Unsupervised Learning and 
Dimensionality Reduction
"""
from __future__ import division #division of integers
print(__doc__)

from time import time
from scipy import stats
from scipy.spatial.distance import cdist, pdist
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import csv
import operator

from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, FastICA, FactorAnalysis
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import MDS
from sklearn.manifold import TSNE
from sklearn import random_projection
from itertools import cycle
from sklearn.metrics import roc_auc_score
from sklearn import mixture
from matplotlib.colors import LogNorm
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score, StratifiedShuffleSplit
from sklearn import cross_validation
from sklearn.svm import SVC
from sklearn.random_projection import johnson_lindenstrauss_min_dim
from sklearn.learning_curve import learning_curve

data = pd.read_csv('credit_train.csv', encoding='cp1251', sep=';')

def clean_data(data):
    # готовим некоторые данные
    data['score_shk'] = data['score_shk'].str.replace(',','.').astype(float)
    data['credit_sum'] = data['credit_sum'].str.replace(',','.').astype(float)
    # преобразуем указанные переменные в тип object
    for i in ['tariff_id', 'open_account_flg']:
        data[i] = data[i].astype('object')
    data['living_region'] = data['living_region'].astype(str)
    from_replace = ['\s?(ОБЛАСТЬ|ОБЛ\.|ОБЛ|КРАЙ\.|КРАЙ|РЕСПУБЛИКА|РЕСП\.|РЕСП|Г\.\s|Г\s|\sГ|АО|Р-Н)\s?', '74',
                '98|САНКТ-ПЕТЕРБУРГ', 'ЕВРЕЙСКАЯБЛ', 'КАМЧАТСКАЯ|КАМЧАТС\?\?ИЙ', '(МОСКВА|МОСКВОСКАЯ|МЫТИЩИНСКИЙ)',
                '(САХА \(ЯКУТИЯ\)|САХА \/ЯКУТИЯ\/)', 'СЕВ\. ОСЕТИЯ - АЛАНИЯ', 'ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУ- ЮГРА',
                'ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУ- Ю', '(ЧУВАШИЯ\sЧУВАШСКАЯ-|ЧУВАШСКАЯ\s?-\sЧУВАШИЯ)', 'БЛ ЕВРЕЙСКАЯ', 
                'БРЯНСКИЙ', 'ГОРЬКОВСКАЯ', 'ОРЁЛ', 'ПЕРМСКАЯ', 'ПРИВОЛЖСКИЙ ФЕДЕРАЛЬНЫЙ ОКРУГ', 'ЭВЕНКИЙСКИЙ', 
                'nan|ГУСЬ-ХРУСТАЛЬНЫЙ|МОСКОВСКИЙ\sП|РОССИЯ', 'ХАНТЫ-МАНСИЙСКИЙ-ЮГРА', 'ЧЕЛЯБИНСК$', 'ЧИТИНСКАЯ',
                'ЧУКОТСКИЙ\sАO', 'Г.МОСКОВСКАЯ', 'Г.ОДИНЦОВО\sМОСКОВСКАЯ', 'ДАЛЬНИЙ\sВОСТОК']
    to_replace = ['', 'ЧЕЛЯБИНСКАЯ', 'ЛЕНИНГРАДСКАЯ', 'ЕВРЕЙСКАЯ АВТОНОМНАЯ',
              'КАМЧАТСКИЙ', 'МОСКОВСКАЯ', 'САХА', 'СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ',
              'ХАНТЫ-МАНСИЙСКИЙ', 'ХАНТЫ-МАНСИЙСКИЙ', 'ЧУВАШСКАЯ', 'ЕВРЕЙСКАЯ АВТОНОМНАЯ',
              'БРЯНСКАЯ', 'НИЖЕГОРОДСКАЯ', 'ОРЛОВСКАЯ', 'ПЕРМСКИЙ', 'МОСКОВСКАЯ', 'КРАСНОЯРСКИЙ', 
              'МОСКОВСКАЯ', 'ХАНТЫ-МАНСИЙСКИЙ', 'ЧЕЛЯБИНСКАЯ', 'ЗАБАЙКАЛЬСКИЙ', 'ЧУКОТСКИЙ', 
              'МОСКОВСКАЯ', 'МОСКОВСКАЯ', 'ПРИМОРСКИЙ']
    data['living_region'].replace(from_replace, to_replace, regex=True, inplace=True)
    
    
def job_tariff_correction():
    data.at[data['job_position'] == 'PNV', 'job_position'] = 'OTHER'
    data.at[data['job_position'] == 'PNS', 'job_position'] = 'OTHER'
    data.at[data['job_position'] == 'HSK', 'job_position'] = 'OTHER'
    data.at[data['job_position'] == 'INV', 'job_position'] = 'OTHER'
    data.at[data['job_position'] == 'ONB', 'job_position'] = 'OTHER'
    data.loc[data['tariff_id'].value_counts()[data['tariff_id']].values < 55, 
         'tariff_id'] = '1.99'
    
def region_clean():
    region_series = data['living_region'].value_counts()
    mask = (region_series/region_series.sum() * 100).lt(0.029)
    data['living_region'] = np.where(data['living_region'].isin(region_series[mask].index), 
                                 'OTHER', data['living_region'])
    
def inputation():
    data['age'].fillna(data['age'].median(), inplace=True)
    for i in ['credit_sum', 'score_shk']:
        data[i].fillna(data[i].median(), inplace=True)
    data['monthly_income'].fillna(30000.0, inplace=True)
    for i in ['credit_count', 'overdue_credit_count']:
        data[i].fillna(-1, inplace=True)
    data['marital_status'] = data['marital_status'].fillna('MAR')
    data['education'].fillna(data['education'].value_counts().index[0], inplace=True)
    data['tariff'] = data['tariff_id'].astype('float')
