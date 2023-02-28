#%%
import myokit
import matplotlib.pyplot as plt
from functions import baseline_run, ind_excel, stim
import matplotlib.lines as mlines

#%%
############## STIMULATED HCM POPULATION ##############
fig, axs = plt.subplots(1, 1, figsize=(12, 8))
t, v = baseline_run()
axs.plot(t, v, '-k', label = 'Baseline')

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13, ind_14, ind_15, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10, ind_ctrl11, ind_ctrl12, ind_ctrl13, ind_ctrl14, ind_ctrl15 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13, ind_14, ind_15]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10, ind_ctrl11, ind_ctrl12, ind_ctrl13, ind_ctrl14, ind_ctrl15]
c_HCM = ['paleturquoise','lightsteelblue', 'cyan','mediumturquoise', 'cornflowerblue', 'darkcyan', 'c', 'teal', 'darkturquoise', 'dodgerblue', 'blue', 'steelblue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['palegreen', 'lawngreen', 'lightgreen', 'lime', 'limegreen', 'yellowgreen', 'olive', 'mediumseagreen', 'seagreen', 'green','darkseagreen', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']
c_stim = ['mistyrose','lightcoral','coral', 'indianred', 'brown', 'rosybrown', 'firebrick', 'maroon', 'sienna', 'red', 'salmon', 'tomato', 'darksalmon', 'orangered', 'lightsalmon']

for i in list(range(0,len(pop_HCM))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_HCM[i])
    axs.plot(t_leak, v_leak, color=c_HCM[i])

for i in list(range(0,len(pop_HCM))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_HCM[i])
    axs.plot(t_rrc, v_rrc, color=c_stim[i])

hcm = mlines.Line2D([], [], color='blue', label='HCM trials')
hcm_inj = mlines.Line2D([], [], color='red', label='HCM trials with current injection')

axs.legend(fontsize=13, handles=[hcm, hcm_inj])
axs.set_ylabel('Voltage (mV)', fontsize=16)
axs.set_xlabel('Time (ms)', fontsize=16)
fig.savefig('CurrentInjection_HCM.png')
plt.show()

############## STIMULATED CTRL POPULATION ##############
fig, axs = plt.subplots(1, 1, figsize=(12, 8))
t, v = baseline_run()
axs.plot(t, v, '-k', label = 'Baseline')

for i in list(range(0,len(pop_CTRL))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_CTRL[i])
    axs.plot(t_leak, v_leak, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

for i in list(range(0,len(pop_CTRL))):
    t_leak, v_leak, t_rrc, v_rrc = stim(pop_CTRL[i])
    axs.plot(t_rrc, v_rrc, color=c_stim[i], label = f'Trial_Inj_CTRL_{i+1}')

ctrl = mlines.Line2D([], [], color='green', label='CTRL trials')
ctrl_inj = mlines.Line2D([], [], color='red', label='CTRL trials with current injection')

axs.legend(fontsize=13, handles=[ctrl, ctrl_inj], loc='upper right')
axs.set_ylabel('Voltage (mV)', fontsize=16)
axs.set_xlabel('Time (ms)', fontsize=16)
fig.savefig('CurrentInjection_CTRL.png')
plt.show()
