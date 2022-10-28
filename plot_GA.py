#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, plot_GA
import seaborn as sns

#%%
###### PLOT BEST INDIVIDUALS FROM HCM_GA ALGORITHM #######

t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_1 = pd.read_excel('Best_ind_1.xlsx')
ind_1 = ind_1.to_dict('index')

t1, v1 = plot_GA(ind_1)
plt.plot(t1, v1, '-b', label = 'Trial_1')

ind_2 = pd.read_excel('Best_ind_2.xlsx')
ind_2 = ind_2.to_dict('index')

t2, v2 = plot_GA(ind_2)
plt.plot(t2, v2, '-m', label = 'Trial_2')

ind_3 = pd.read_excel('Best_ind_3.xlsx')
ind_3 = ind_3.to_dict('index')

t3, v3 = plot_GA(ind_3)
plt.plot(t3, v3, '-r', label = 'Trial_3')

ind_4 = pd.read_excel('Best_ind_4.xlsx')
ind_4 = ind_4.to_dict('index')

t4, v4 = plot_GA(ind_4)
plt.plot(t4, v4, '-g', label = 'Trial_4')

ind_5 = pd.read_excel('Best_ind_5.xlsx')
ind_5 = ind_5.to_dict('index')

t5, v5 = plot_GA(ind_5)
plt.plot(t5, v5, '-y', label = 'Trial_5')

plt.legend()
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds.png')
plt.show()


# %%
