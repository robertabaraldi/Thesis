#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, plot_GA, plot_cond, ind_excel, err_excel
import seaborn as sns
from math import log10

#%%
###### PLOT BEST INDIVIDUALS FROM HCM_GA ALGORITHM #######

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13 = ind_excel()

pop = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13]

for i in list(range(1,len(pop))):
    t, v = plot_GA(pop[i])
    plt.plot(t, v, label = f'Trial_{i}')

plt.legend()
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds.png')
plt.show()

#%%
############ PLOT BEST ERROR ################
gen = [i for i in list(range(1,80))]

err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10, err_11, err_12, err_13 = err_excel()

err = [err_1, err_2, err_3, err_4, err_5, err_6, err_7, 
err_8, err_9, err_10, err_11, err_12, err_13]

for i in list(range(1,len(err))):
    best_err = list(err[i]['Best Error'])
    plt.plot(gen, best_err,'*', label = f'Trial_{i}')

plt.legend()
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.suptitle('Best Errors', fontsize=14)
plt.ylim(0,8000)
plt.savefig('Plot_Best_Errors.png')
plt.show()

#%% 
########## PLOT CONDUCTANCES ############
pop = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13]
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
#plt.legend()
plt.show()

