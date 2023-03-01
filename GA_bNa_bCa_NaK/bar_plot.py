import matplotlib.pyplot as plt
from functions import ind_excel
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind
from math import log10
import numpy as np
import matplotlib.lines as mlines

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
            ##v = log10(v)
            all_ind_dict[k].append(v)

data_hcm = pd.DataFrame(all_ind_dict)
data_hcm.to_excel('Cond_HCM.xlsx', sheet_name='Sheet1',index=False)

keys = [k for k in pop_CTRL[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop_CTRL:
        for k, v in ind[0].items():
            #v = log10(v)
            all_ind_dict[k].append(v)

data_ctrl = pd.DataFrame(all_ind_dict)
data_ctrl.to_excel('Cond_CTRL.xlsx', sheet_name='Sheet1',index=False)

df_all = pd.read_excel('conductances.xlsx')

plt.figure(figsize=(12,8))

#sns.pointplot(df_hcm, join=False, capsize=.2, color='red', markers='o', errwidth=2)
#sns.pointplot(df_ctrl, join=False, capsize=.2, color='blue', markers='d', errwidth=2)
#sns.swarmplot(df_hcm, palette=sns.color_palette(['lightcoral','lightcoral','lightcoral','lightcoral','lightcoral','lightcoral','lightcoral','lightcoral']))
#sns.swarmplot(df_ctrl, palette=sns.color_palette(['lightblue','lightblue','lightblue','lightblue','lightblue','lightblue','lightblue','lightblue']))


sns.swarmplot(df_all, x='conductance_name', y='parameter_value', hue='cell_type', palette=sns.color_palette(['lightblue','lightcoral']), dodge=True)
sns.pointplot(df_all, x='conductance_name', y='parameter_value', hue='cell_type',join=False, capsize=.2, palette=sns.color_palette(['blue','red']), markers=['d','o'], errwidth=2, dodge=0.3)

red_circle = mlines.Line2D([], [], color='red', marker='o', linestyle='None', markersize=7, label='HCM')
blue_diamond = mlines.Line2D([], [], color='blue', marker='d', linestyle='None', markersize=7, label='CTRL')

plt.legend(handles=[blue_diamond, red_circle])
plt.hlines(0, -.5, (len(keys)-.5), colors='black', linestyle='--')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Log10 Conductance', fontsize=14)
plt.savefig('Bar_Cat_conductances.png')
plt.show()

#######################################################################################

plt.figure(figsize=(12,8))

#sns.pointplot(df_hcm, join=False, capsize=.2, color='red', markers='o', errwidth=2)
#sns.pointplot(df_ctrl, join=False, capsize=.2, color='blue', markers='d', errwidth=2)
sns.pointplot(df_all, x='conductance_name', y='parameter_value', hue='cell_type',join=False, capsize=.2, palette=sns.color_palette(['blue','red']), markers=['d','o'], errwidth=2, dodge=0.3)

red_circle = mlines.Line2D([], [], color='red', marker='o', linestyle='None', markersize=7, label='HCM')
blue_diamond = mlines.Line2D([], [], color='blue', marker='d', linestyle='None', markersize=7, label='CTRL')

plt.legend(handles=[ blue_diamond, red_circle])
plt.hlines(0, -.5, (len(keys)-.5), colors='black', linestyle='--')
plt.xticks(label=['GKs','GCal','GKr','GNa','Gto','GK1','Gf','Gleak','GbNa','GbCa','GNaK'],fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Log10 Conductance', fontsize=14)
plt.xlabel(xlabel=None)
plt.savefig('Bar_conductances.png')
plt.show()

