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

ind_1 = pd.read_excel('Best_ind_1_.xlsx')
ind_1 = ind_1.to_dict('index')

t1, v1 = plot_GA(ind_1)
plt.plot(t1, v1, '-b', label = 'Trial_1')

ind_2 = pd.read_excel('Best_ind_2.xlsx')
ind_2 = ind_2.to_dict('index')

t2, v2 = plot_GA(ind_2)
plt.plot(t2, v2, '-m', label = 'Trial_2')

ind_3 = pd.read_excel('Best_ind_3_.xlsx')
ind_3 = ind_3.to_dict('index')

t3, v3 = plot_GA(ind_3)
plt.plot(t3, v3, '-r', label = 'Trial_3')

ind_4 = pd.read_excel('Best_ind_4_.xlsx')
ind_4 = ind_4.to_dict('index')

t4, v4 = plot_GA(ind_4)
plt.plot(t4, v4, '-g', label = 'Trial_4')

ind_5 = pd.read_excel('Best_ind_5_.xlsx')
ind_5 = ind_5.to_dict('index')

t5, v5 = plot_GA(ind_5)
plt.plot(t5, v5, '-y', label = 'Trial_5')

ind_6 = pd.read_excel('Best_ind_6.xlsx')
ind_6 = ind_6.to_dict('index')

t6, v6 = plot_GA(ind_6)
plt.plot(t6, v6, '-c', label = 'Trial_6')

ind_7 = pd.read_excel('Best_ind_72.xlsx')
ind_7 = ind_7.to_dict('index')

t7, v7 = plot_GA(ind_7)
plt.plot(t7, v7, c = 'hotpink', label = 'Trial_7')

ind_8 = pd.read_excel('Best_ind_8.xlsx')
ind_8 = ind_8.to_dict('index')

t8, v8 = plot_GA(ind_8)
plt.plot(t8, v8, c = 'brown', label = 'Trial_8')

plt.legend()
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals: pop = 100, gen = 80', fontsize=14)
plt.savefig('Plot_Best_Inds.png')
plt.show()


# %%
