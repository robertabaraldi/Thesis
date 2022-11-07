#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, plot_GA, plot_cond, ind_excel, err_excel
import seaborn as sns
from math import log10
from scipy.signal import find_peaks

#%%
###### PLOT BEST INDIVIDUALS FROM HCM_GA ALGORITHM #######

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_1 = ind_excel()

pop = [ind_1]

for i in list(range(0,len(pop))):
    t, v = plot_GA(pop[i])
    plt.plot(t, v, label = f'Trial_{i+1}')

plt.legend()
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds.png')
plt.show()

######## PRINT FEATURES ##########
ap_features = {}
mdp = min(v)
max_p = max(v)
max_p_idx = np.argmax(v)
apa = max_p - mdp
dvdt_max = np.max(np.diff(v[0:30])/np.diff(t[0:30]))

ap_features['dvdt_max'] = dvdt_max
peak_v = find_peaks(v, distance=100)
peak = v[peak_v[0][0]]
ap_features['peak'] = peak
ap_features['apa']= apa

for apd_pct in [50, 90]:
    repol_pot = max_p - apa * apd_pct/100
    idx_apd = np.argmin(np.abs(v[max_p_idx:] - repol_pot))
    apd_val = t[idx_apd+max_p_idx]

    ap_features[f'apd{apd_pct}'] = apd_val

ap_features['mdp']= mdp

#print(ap_features)

#%%
############ PLOT BEST ERROR ################
gen = [i for i in list(range(1,80))]

err_1 = err_excel()

err = [err_1]

for i in list(range(0,len(err))):
    best_err = list(err[i]['Avg Error'])
    plt.plot(gen, best_err,'*', label = f'Trial_{i+1}')

plt.legend()
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.suptitle('Best Errors', fontsize=14)
plt.ylim(0,5000)
plt.savefig('Plot_Best_Errors.png')
plt.show()

#%% 
########## PLOT CONDUCTANCES ############
pop = [ind_1]
trials = []

for i in list(range(0,len(pop))):
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
plt.xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak','GbNa','GbCa','GNaK'], fontsize=10)
plt.ylim(log10(0.1), log10(10))
plt.ylabel('Log10 Conductance', fontsize=14)
#plt.legend()
plt.savefig('Conductances.png')
plt.show()
