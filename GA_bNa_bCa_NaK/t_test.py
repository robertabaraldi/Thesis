import matplotlib.pyplot as plt
from functions import ind_excel
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind
from math import log10

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10]

keys = [k for k in pop_HCM[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop_HCM:
        for k, v in ind[0].items():
            v = log10(v)
            all_ind_dict[k].append(v)

keys = [k for k in pop_CTRL[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop_CTRL:
        for k, v in ind[0].items():
            v = log10(v)
            all_ind_dict[k].append(v)

df_hcm = pd.read_excel('Cond_HCM.xlsx')
df_ctrl = pd.read_excel('Cond_CTRL.xlsx')

t_value = ttest_ind(df_hcm, df_ctrl)
cond_significance = []

for i in t_value.pvalue:
    if i < .05:
        cond_significance.append([keys, i])
        print(i)

#Iks has a pvalue<0.05
#Ina has a pvalue<0.05
#Ibca has a pvalue<0.05
#Inak has a pvalue<0.05