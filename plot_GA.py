#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, plot_GA, ind_excel, err_excel
import seaborn as sns
from math import log10
from scipy.signal import find_peaks

#%%
###### PLOT HCM BEST IND #######

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_1 = ind_excel()

pop_HCM = [ind_1]
pop_CTRL = []

for i in list(range(0,len(pop_HCM))):
    t, v = plot_GA(pop_HCM[i])
    plt.plot(t, v, label = f'Trial_HCM_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals HCM: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds_HCM.png')
plt.show()


####### PLOT CTRL BEST IND ########

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

for i in list(range(0,len(pop_CTRL))):
    t, v = plot_GA(pop_CTRL[i])
    plt.plot(t, v, label = f'Trial_CTRL_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals CTRL: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds_CTRL.png')
plt.show()

######## PLOT TOGETHER HCM AND CTRL ############

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

for i in list(range(0,len(pop_HCM))):
    t, v = plot_GA(pop_HCM[i])
    plt.plot(t, v, label = f'Trial_HCM_{i+1}')

for i in list(range(0,len(pop_CTRL))):
    t, v = plot_GA(pop_CTRL[i])
    plt.plot(t, v, label = f'Trial_CTRL_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds.png')
plt.show()


#%%
############ PLOT BEST ERROR HCM ################
gen = [i for i in list(range(1,80))]

err_5, err_7, err_8, err_9, err_ctrl1, err_ctrl2, err_ctrl4, err_ctrl5 = err_excel()

err_HCM = [err_5, err_7, err_8, err_9]
err_CTRL = [err_ctrl1, err_ctrl2, err_ctrl4, err_ctrl5]

for i in list(range(0,len(err_HCM))):
    best_err = list(err_HCM[i]['Best Error'])
    plt.plot(gen, best_err,'*', label = f'Trial_HCM_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.suptitle('Best Errors HCM', fontsize=14)
plt.ylim(0,5000)
plt.savefig('Plot_Best_Errors_HCM.png')
plt.show()

############ PLOT BEST ERROR CTRL ################

for i in list(range(0,len(err_CTRL))):
    best_err = list(err_CTRL[i]['Best Error'])
    plt.plot(gen, best_err,'*', label = f'Trial_CTRL_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.suptitle('Best Errors CTRL', fontsize=14)
plt.ylim(0,5000)
plt.savefig('Plot_Best_Errors_CTRL.png')
plt.show()


#%% 
########## PLOT HCM CONDUCTANCES ############
plt.figure(figsize=(12,6))
trials = []

for i in list(range(0,len(pop_HCM))):
    trials.append(f'Trial_HCM_{i+1}')

keys = [k for k in pop_HCM[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop_HCM:
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
plt.xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak','GbNa','GbCa','GNaK'], fontsize=10)
plt.ylim(log10(0.1), log10(10))
plt.ylabel('Log10 Conductance', fontsize=14)
plt.suptitle('Conductances_HCM')
plt.savefig('Conductances_HCM.png')
plt.show()

########## PLOT CTRL CONDUCTANCES ############

plt.figure(figsize=(12,6))
trials = []

for i in list(range(0,len(pop_CTRL))):
    trials.append(f'Trial_CTRL_{i+1}')

keys = [k for k in pop_CTRL[0][0].keys()]
empty_arrs = [[] for i in range(len(keys))]
all_ind_dict = dict(zip(keys, empty_arrs))

for ind in pop_CTRL:
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
plt.xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak','GbNa','GbCa','GNaK'], fontsize=10)
plt.ylim(log10(0.1), log10(10))
plt.ylabel('Log10 Conductance', fontsize=14)
plt.suptitle('Conductances_CTRL')
plt.savefig('Conductances_CTRL.png')
plt.show()

