#%%
import myokit
import matplotlib.pyplot as plt
import numpy as np
from functions import baseline_run, plot_GA, ind_excel, err_excel, stim
from math import log10
from scipy.signal import find_peaks

#%%
t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_5, ind_7, ind_8, ind_9, ind_ctrl1, ind_ctrl2, ind_ctrl4, ind_ctrl5 = ind_excel()

pop_HCM = [ind_5, ind_7, ind_8, ind_9]


for i in list(range(0,len(pop_HCM))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_HCM[i])
    plt.plot(t_rrc, v_rrc, label = f'Trial_Stim_HCM_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals - Stimulus Injection', fontsize=14)
plt.savefig('Plot_Stim_HCM.png')
plt.show()

# %%
