import matplotlib.pyplot as plt
from functions import ind_excel
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind
from math import log10

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13, ind_14, ind_15, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10, ind_ctrl11, ind_ctrl12, ind_ctrl13, ind_ctrl14, ind_ctrl15 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13, ind_14, ind_15]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10, ind_ctrl11, ind_ctrl12, ind_ctrl13, ind_ctrl14, ind_ctrl15]
c_HCM = ['paleturquoise','lightsteelblue', 'cyan','mediumturquoise', 'cornflowerblue', 'darkcyan', 'c', 'teal', 'darkturquoise', 'dodgerblue', 'blue', 'steelblue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['palegreen', 'lawngreen', 'lightgreen', 'lime', 'limegreen', 'yellowgreen', 'olive', 'mediumseagreen', 'seagreen', 'green','darkseagreen', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']

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
print(t_value)

for i in t_value.pvalue:
    if i < .05:
        cond_significance.append([keys, i])
        print(i)

#Ikr has a pvalue<0.01 