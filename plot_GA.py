#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, plot_GA, plot_g
import seaborn as sns
from scipy.signal import find_peaks 

#%%
######## PLOT BEST INDIVIDUALS #########

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_1 = pd.read_excel('Best_ind_primo.xlsx')
ind_1 = ind_1.to_dict('index')

t1, v1 = plot_GA(ind_1)
plt.plot(t1, v1, label = 'Trial_1')

ind_2 = pd.read_excel('Best_ind_secondo_.xlsx')
ind_2 = ind_2.to_dict('index')

t2, v2 = plot_GA(ind_2)
plt.plot(t2, v2, label = 'Trial_2')

plt.legend()
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds.png')
plt.show()

# %%
############ PLOT BEST ERROR ################
gen = [i for i in list(range(1,80))]

err_1 = pd.read_excel('Errors_primo.xlsx')
best_err_1 = list(err_1['Avg Error'])
plt.plot(gen, best_err_1,'*', label = 'Trial_1')

err_2 = pd.read_excel('Errors_secondo_.xlsx')
best_err_2 = list(err_2['Avg Error'])
plt.plot(gen, best_err_2,'*', label = 'Trial_2')

plt.legend()
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.suptitle('Best Errors', fontsize=14)
plt.savefig('Plot_Best_Errors.png')
plt.show()

# %%
