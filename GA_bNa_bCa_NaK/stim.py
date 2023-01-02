#%%
import myokit
import matplotlib.pyplot as plt
import numpy as np
from functions import baseline_run, plot_GA, ind_excel, err_excel, stim
from math import log10
from scipy.signal import find_peaks

#%%
############## STIMULATED HCM POPULATION ##############
fig, axs = plt.subplots(1, 2, figsize=(28, 6))
t, v, iks, ikr, ical, ina = baseline_run()
axs[0].plot(t, v, '-k', label = 'Baseline')

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']

for i in list(range(0,len(pop_HCM))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_HCM[i])
    axs[0].plot(t_leak, v_leak, color=c_HCM[i], label = f'Trial_HCM_{i+1}')
    axs[0].plot(t_rrc, v_rrc, color=c_CTRL[i], label = f'Trial_Stim_HCM_{i+1}')

axs[0].legend(fontsize= 5, loc='lower center')
axs[0].set_ylabel('Voltage (mV)', fontsize=14)
axs[0].set_xlabel('Time (ms)', fontsize=14)

############## STIMULATED CTRL POPULATION ##############
t, v, iks, ikr, ical, ina = baseline_run()
axs[1].plot(t, v, '-k', label = 'Baseline')

pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10]

for i in list(range(0,len(pop_CTRL))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_CTRL[i])
    axs[1].plot(t_leak, v_leak, color=c_HCM[i], label = f'Trial_CTRL_{i+1}')
    axs[1].plot(t_rrc, v_rrc, color=c_CTRL[i], label = f'Trial_Stim_CTRL_{i+1}')

axs[1].legend(fontsize= 5, loc='upper right')
axs[1].set_ylabel('Voltage (mV)', fontsize=14)
axs[1].set_xlabel('Time (ms)', fontsize=14)

fig.savefig('Plot_CurrentInjection.png')
plt.show()
