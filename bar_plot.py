import matplotlib.pyplot as plt
from functions import ind_excel
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind
from math import log10
import numpy as np

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10]
c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']

keys = [k for k in pop_HCM[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop_HCM:
        for k, v in ind[0].items():
            v = log10(v)
            all_ind_dict[k].append(v)

'''data_hcm = pd.DataFrame(all_ind_dict)
data_hcm.to_excel('Cond_HCM.xlsx', sheet_name='Sheet1',index=False)'''

keys = [k for k in pop_CTRL[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop_CTRL:
        for k, v in ind[0].items():
            v = log10(v)
            all_ind_dict[k].append(v)

'''data_ctrl = pd.DataFrame(all_ind_dict)
data_ctrl.to_excel('Cond_CTRL.xlsx', sheet_name='Sheet1',index=False)'''

df_hcm = pd.read_excel('Cond_HCM.xlsx')
df_ctrl = pd.read_excel('Cond_CTRL.xlsx')

fig, axs = plt.subplots(1, 1, figsize=(12, 8))
plt.rcParams['svg.fonttype'] = 'none'

axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)

sns.pointplot(df_hcm, join=False, capsize=.2, color='blue')
sns.pointplot(df_ctrl, join=False, capsize=.2, color='red')

axs.hlines(0, -.5, (len(keys)-.5), colors='black', linestyle='--')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
axs.set_ylabel('Conductances', fontsize=14)
plt.savefig('Bar_conductances.png')
plt.show()

