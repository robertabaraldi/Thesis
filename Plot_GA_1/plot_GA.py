#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, plot_GA, ind_excel, err_excel
import seaborn as sns
from math import log10

#%%
###### PLOT BEST INDIVIDUALS FROM HCM_GA ALGORITHM #######

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_6, ind_7, ind_8 = ind_excel()

pop = [ind_6, ind_7, ind_8]

for i in list(range(0,len(pop))):
    t, v = plot_GA(pop[i])
    plt.plot(t, v, label = f'Trial_{i+1}')

plt.legend()
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds.png')
plt.show()

#%%
############ PLOT BEST ERROR ################
gen = [i for i in list(range(1,80))]

err_6, err_7, err_8 = err_excel()

err = [err_6, err_7, err_8]

for i in list(range(0,len(err))):
    best_err = list(err[i]['Best Error'])
    plt.plot(gen, best_err,'*', label = f'Trial_{i+1}')

plt.legend()
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.suptitle('Best Errors', fontsize=14)
plt.suptitle('Best Errors')
plt.ylim(0,8000)
plt.savefig('Plot_Best_Errors.png')
plt.show()

#%% 
########## PLOT CONDUCTANCES ############
pop = [ind_6, ind_7, ind_8]
trials = []

for i in list(range(0,len(pop))):
    trials.append(f'Trial_{i+1}')

keys = [k for k in pop[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop:
        for k, v in ind[0].items():
            all_ind_dict[k].append(v)

curr_x = 0
m = 0
c = ['lightsteelblue', 'cornflowerblue', 'royalblue', 'blue', 'mediumblue', 'darkblue', 
'lightgreen', 'limegreen','mediumseagreen', 'green', 'darkgreen', 'r']

for k, conds in all_ind_dict.items():
    for i, g in enumerate(conds):
        g = log10(g)
        x = curr_x + np.random.normal(0, .01)
        if m == 0:
            plt.scatter(x, g, color=c[i], label = trials[i])
            plt.legend()
        else:
            plt.scatter(x, g, color=c[i])
    m = 1

    curr_x += 1

curr_x = 0

plt.hlines(0, -.5, (len(keys)-.5), colors='grey', linestyle='--')
plt.xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak'], fontsize=10)
plt.ylim(log10(0.1), log10(10))
plt.ylabel('Log10 Conductance', fontsize=14)
plt.suptitle('Conductances_HCM')
plt.savefig('Conductances_HCM.png')
plt.show()

# %%
