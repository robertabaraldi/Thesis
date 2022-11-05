#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, plot_GA, plot_cond
import seaborn as sns
from math import log10

#%%
###### PLOT BEST INDIVIDUALS FROM HCM_GA ALGORITHM #######

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_1 = pd.read_excel('Best_ind_1.xlsx')
ind_1 = ind_1.to_dict('index')

t1, v1 = plot_GA(ind_1)
plt.plot(t1, v1, label = 'Trial_1')

ind_2 = pd.read_excel('Best_ind_2.xlsx')
ind_2 = ind_2.to_dict('index')

t2, v2 = plot_GA(ind_2)
plt.plot(t2, v2, label = 'Trial_2')

ind_3 = pd.read_excel('Best_ind_3.xlsx')
ind_3 = ind_3.to_dict('index')

t3, v3 = plot_GA(ind_3)
plt.plot(t3, v3, label = 'Trial_3')

ind_4 = pd.read_excel('Best_ind_4.xlsx')
ind_4 = ind_4.to_dict('index')

t4, v4 = plot_GA(ind_4)
plt.plot(t4, v4, label = 'Trial_4')

ind_5 = pd.read_excel('Best_ind_5.xlsx')
ind_5 = ind_5.to_dict('index')

t5, v5 = plot_GA(ind_5)
plt.plot(t4, v4, label = 'Trial_5')

ind_6 = pd.read_excel('Best_ind_6.xlsx')
ind_6 = ind_6.to_dict('index')

t6, v6 = plot_GA(ind_6)
plt.plot(t6, v6, label = 'Trial_6')

ind_7 = pd.read_excel('Best_ind_7.xlsx')
ind_7 = ind_7.to_dict('index')

t7, v7 = plot_GA(ind_7)
plt.plot(t7, v7, label = 'Trial_7')

ind_8 = pd.read_excel('Best_ind_8.xlsx')
ind_8 = ind_8.to_dict('index')

t8, v8 = plot_GA(ind_8)
plt.plot(t8, v8, label = 'Trial_8')

ind_9 = pd.read_excel('Best_ind_9.xlsx')
ind_9 = ind_9.to_dict('index')

t9, v9 = plot_GA(ind_9)
plt.plot(t9, v9, label = 'Trial_9')

ind_10 = pd.read_excel('Best_ind_10.xlsx')
ind_10 = ind_10.to_dict('index')

t10, v10 = plot_GA(ind_10)
plt.plot(t10, v10, label = 'Trial_10')

plt.legend()
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds.png')
plt.show()

#%%
############ PLOT BEST ERROR ################
gen = [i for i in list(range(1,80))]

err_1 = pd.read_excel('Errors_1.xlsx')
best_err_1 = list(err_1['Avg Error'])
plt.plot(gen, best_err_1,'*', label = 'Trial_1')

err_2 = pd.read_excel('Errors_2.xlsx')
best_err_2 = list(err_2['Avg Error'])
plt.plot(gen, best_err_2,'*', label = 'Trial_2')

err_3 = pd.read_excel('Errors_3.xlsx')
best_err_3 = list(err_3['Avg Error'])
plt.plot(gen, best_err_3,'*', label = 'Trial_3')

err_4 = pd.read_excel('Errors_4.xlsx')
best_err_4 = list(err_4['Avg Error'])
plt.plot(gen, best_err_4,'*', label = 'Trial_4')

err_5 = pd.read_excel('Errors_5.xlsx')
best_err_5 = list(err_5['Best Error'])
plt.plot(gen, best_err_5,'*', label = 'Trial_5')

err_6 = pd.read_excel('Errors_6.xlsx')
best_err_6 = list(err_6['Best Error'])
plt.plot(gen, best_err_6,'*', label = 'Trial_6')

err_7 = pd.read_excel('Errors_7.xlsx')
best_err_7 = list(err_7['Best Error'])
plt.plot(gen, best_err_7,'*', label = 'Trial_7')

err_8 = pd.read_excel('Errors_8.xlsx')
best_err_8 = list(err_8['Best Error'])
plt.plot(gen, best_err_8,'*', label = 'Trial_8')

err_9 = pd.read_excel('Errors_9.xlsx')
best_err_9 = list(err_9['Best Error'])
plt.plot(gen, best_err_9,'*', label = 'Trial_9')

err_10 = pd.read_excel('Errors_10.xlsx')
best_err_10 = list(err_10['Best Error'])
plt.plot(gen, best_err_10,'*', label = 'Trial_10')

plt.legend()
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.suptitle('Best Errors', fontsize=14)
plt.ylim(0,8000)
plt.savefig('Plot_Best_Errors.png')
plt.show()

#%% 
########## PLOT CONDUCTANCES ############
pop = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
trials = []

for i in list(range(0,10)):
    trials.append(f'Trial_{i}')

keys = [k for k in pop[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop:
        for k, v in ind[0].items():
            all_ind_dict[k].append(v)

curr_x = 0
n = 0

for k, conds in all_ind_dict.items():
    for i, g in enumerate(conds):
        g = log10(g)
        x = curr_x + np.random.normal(0, .01)
        plt.scatter(x, g) #label = trials[n])

    curr_x += 1

    n += 1

curr_x = 0

plt.hlines(0, -.5, (len(keys)-.5), colors='grey', linestyle='--')
plt.xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak'], fontsize=10)
plt.ylim(log10(0.1), log10(10))
plt.ylabel('Log10 Conductance', fontsize=14)
plt.legend()
plt.show()

