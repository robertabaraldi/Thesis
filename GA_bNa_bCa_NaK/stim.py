#%%
import myokit
import matplotlib.pyplot as plt
import numpy as np
from functions import baseline_run, plot_GA, ind_excel, err_excel, stim
from math import log10
from scipy.signal import find_peaks

#%%
############## STIMULATED HCM POPULATION ##############
plt.figure(figsize=(14,8))
t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']

for i in list(range(0,len(pop_HCM))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_HCM[i])
    plt.plot(t_leak, v_leak, color=c_HCM[i], label = f'Trial_HCM_{i+1}')
    plt.plot(t_rrc, v_rrc, color=c_CTRL[i], label = f'Trial_Stim_HCM_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best HCM Individuals - Stimulus Injection', fontsize=14)
plt.savefig('Plot_Stim_HCM.png')
plt.show()

############## STIMULATED CTRL POPULATION ##############
plt.figure(figsize=(14,8))
t, v = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6]

for i in list(range(0,len(pop_CTRL))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_CTRL[i])
    plt.plot(t_leak, v_leak, color=c_HCM[i], label = f'Trial_CTRL_{i+1}')
    plt.plot(t_rrc, v_rrc, color=c_CTRL[i], label = f'Trial_Stim_CTRL_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best CTRL Individuals - Stimulus Injection', fontsize=14)
plt.savefig('Plot_Stim_CTRL.png')
plt.show()

# %%
