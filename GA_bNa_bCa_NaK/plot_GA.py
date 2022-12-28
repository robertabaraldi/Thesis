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
###### PLOT HCM BEST IND ########
fig, axs = plt.subplots(1, 2, figsize=(20, 6))

t, v = baseline_run()
axs[0].plot(t, v, '-k', label = 'Baseline')

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10]
c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']

for i in list(range(0,len(pop_HCM))):
    t, v = plot_GA(pop_HCM[i])
    axs[0].plot(t, v, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[0].legend(loc='upper right')
axs[0].set_ylabel('Voltage (mV)', fontsize=14)
axs[0].set_xlabel('Time (ms)', fontsize=14)

############ PLOT BEST ERROR HCM ################
gen = [i for i in list(range(1,80))]

err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10, err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6, err_ctrl7, err_ctrl8, err_ctrl9, err_ctrl10 = err_excel()

err_HCM = [err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10]
err_CTRL = [err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6, err_ctrl7, err_ctrl8, err_ctrl9, err_ctrl10]

for i in list(range(0,len(err_HCM))):
    best_err = list(err_HCM[i]['Best Error'])
    axs[1].plot(gen, best_err,'*', color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[1].legend(loc='upper right')
axs[1].set_ylabel('Error', fontsize=14)
axs[1].set_xlabel('Generation', fontsize=14)
axs[1].set_ylim(0,5000)

fig.suptitle('HCM Individuals', fontsize=14)
fig.savefig('Plot_HCM.png')
plt.show()

#%%
####### PLOT CTRL BEST IND ########
fig, axs = plt.subplots(1, 2, figsize=(20, 6))

t, v = baseline_run()
axs[0].plot(t, v, '-k', label = 'Baseline')

for i in list(range(0,len(pop_CTRL))):
    t, v = plot_GA(pop_CTRL[i])
    axs[0].plot(t, v, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

axs[0].legend(loc='upper right')
axs[0].set_ylabel('Voltage (mV)', fontsize=14)
axs[0].set_xlabel('Time (ms)', fontsize=14)

############ PLOT BEST ERROR CTRL ################

for i in list(range(0,len(err_CTRL))):
    best_err = list(err_CTRL[i]['Best Error'])
    axs[1].plot(gen, best_err,'*', color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

axs[1].legend(loc='upper right')
axs[1].set_ylabel('Error', fontsize=14)
axs[1].set_xlabel('Generation', fontsize=14)
axs[1].set_ylim(0,5000)

fig.suptitle('CTRL Individuals', fontsize=14)
fig.savefig('Plot_CTRL.png')
plt.show()


#%%

######## PLOT TOGETHER HCM AND CTRL ############
plt.figure(figsize=(14,8))

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

for i in list(range(0,len(pop_HCM))):
    t, v = plot_GA(pop_HCM[i])
    plt.plot(t, v, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

for i in list(range(0,len(pop_CTRL))):
    t, v = plot_GA(pop_CTRL[i])
    plt.plot(t, v, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.savefig('Plot_Best_HCMandCTRL.png')
plt.show()

#%% 

########## PLOT HCM CONDUCTANCES ############
fig, axs = plt.subplots(1, 2, figsize=(20, 6))
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

for k, conds in all_ind_dict.items():
    for i, g in enumerate(conds):
        g = log10(g)
        x = curr_x + np.random.normal(0, .01)
        if m == 0:
            axs[0].scatter(x, g, color=c_HCM[i], label = trials[i])
            axs[0].legend(fontsize=5, loc='upper right')
        else:
            axs[0].scatter(x, g, color=c_HCM[i])
    m = 1

    curr_x += 1

curr_x = 0

axs[0].hlines(0, -.5, (len(keys)-.5), colors='grey', linestyle='--')
axs[0].set_xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak','GbNa','GbCa','GNaK'], fontsize=10)
axs[0].set_ylim(log10(0.1), log10(10))
axs[0].set_ylabel('Log10 Conductance', fontsize=14)

########## PLOT CTRL CONDUCTANCES ############

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

for k, conds in all_ind_dict.items():
    for i, g in enumerate(conds):
        g = log10(g)
        x = curr_x + np.random.normal(0, .01)
        if m == 0:
            axs[1].scatter(x, g, color=c_CTRL[i], label = trials[i])
            axs[1].legend(fontsize=5, loc='upper right')
        else:
            axs[1].scatter(x, g, color=c_CTRL[i])
    m = 1

    curr_x += 1

curr_x = 0

axs[1].hlines(0, -.5, (len(keys)-.5), colors='grey', linestyle='--')
axs[1].set_xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak','GbNa','GbCa','GNaK'], fontsize=10)
axs[1].set_ylim(log10(0.1), log10(10))
axs[1].set_ylabel('Log10 Conductance', fontsize=14)

fig.suptitle('Conductances HCM and CTRL')
fig.savefig('Conductances.png')
plt.show()

#%%

######### PLOT CTRL AND HCM CONDUCTANCES TOGETHER ########

plt.figure(figsize=(14,8))
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

for k, conds in all_ind_dict.items():
    for i, g in enumerate(conds):
        g = log10(g)
        x = curr_x + np.random.normal(0, .01)
        if m == 0:
            plt.scatter(x, g, color=c_HCM[i], label = trials[i])
            plt.legend(fontsize=5, loc='upper right')
        else:
            plt.scatter(x, g, color=c_HCM[i])
    m = 1

    curr_x += 1

curr_x = 0

plt.hlines(0, -.5, (len(keys)-.5), colors='grey', linestyle='--')
plt.xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak','GbNa','GbCa','GNaK'], fontsize=10)
plt.ylim(log10(0.1), log10(10))
plt.ylabel('Log10 Conductance', fontsize=14)

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

for k, conds in all_ind_dict.items():
    for i, g in enumerate(conds):
        g = log10(g)
        x = curr_x + np.random.normal(0, .01)
        if m == 0:
            plt.scatter(x, g, color=c_CTRL[i], label = trials[i])
            plt.legend(fontsize=5, loc='upper right')
        else:
            plt.scatter(x, g, color=c_CTRL[i])
    m = 1

    curr_x += 1

curr_x = 0

plt.suptitle('Conductances Comparison')
plt.savefig('Conductances Comparison.png')
plt.show()


# %%
