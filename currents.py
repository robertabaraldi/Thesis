#%%
import matplotlib.pyplot as plt
from functions import err_excel, currents, ind_excel, baseline_run
import pandas as pd

#%%

###### PLOT ERRORS, FOR COMPARISON WITH AP FEATURES ########

######## HCM ERRORS ############
plt.figure(figsize=(14,8))

gen = [i for i in list(range(1,80))]

err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10, err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6, err_ctrl7, err_ctrl8, err_ctrl9, err_ctrl10 = err_excel()

err_HCM = [err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10]
err_CTRL = [err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6, err_ctrl7, err_ctrl8, err_ctrl9, err_ctrl10]

c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']

for i in list(range(0,len(err_HCM))):
    best_err = list(err_HCM[i]['Best Error'])
    plt.plot(gen, best_err,'*', color=c_HCM[i], label = f'Trial_HCM_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.ylim(0,5000)
plt.suptitle('HCM Errors', fontsize=14)
plt.savefig('HCM_Errors.png')
plt.show()

######### CTRL ERRORS ##########
plt.figure(figsize=(14,8))

for i in list(range(0,len(err_CTRL))):
    best_err = list(err_CTRL[i]['Best Error'])
    plt.plot(gen, best_err,'*', color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Error', fontsize=14)
plt.xlabel('Generation', fontsize=14)
plt.ylim(0,5000)
plt.suptitle('CTRL Errors', fontsize=14)
plt.savefig('CTRL_Errors.png')
plt.show()

#%%

############ PLOT HCM CURRENTS #############
fig, axs = plt.subplots(4, 1, figsize=(16, 8))

### Baseline ###
ind = pd.read_excel('Best_ind.xlsx')
ind = ind.to_dict('index')
t_b, v_b, iks_b, ikr_b, ical_b, ina_b = currents(ind)
###############

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10 = ind_excel()
pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10]

for i in list(range(0,len(pop_HCM))):
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    axs[0].plot(t, iks, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[0].plot(t_b, iks_b, 'k', label = 'Baseline')

axs[0].legend(fontsize = 5, loc='upper right')
axs[0].set_ylabel('iKs (A/F)', fontsize=14)

for i in list(range(0,len(pop_HCM))):
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    axs[1].plot(t, ikr, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[1].plot(t_b, ikr_b, 'k', label = 'Baseline')

axs[1].legend(fontsize = 5, loc='upper right')
axs[1].set_ylabel('iKr (A/F)', fontsize=14)

for i in list(range(0,len(pop_HCM))):
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    axs[2].plot(t, ical, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[2].plot(t_b, ical_b, 'k', label = 'Baseline')

axs[2].legend(fontsize = 5, loc='upper right')
axs[2].set_ylabel('iCaL (A/F)', fontsize=14)

for i in list(range(0,len(pop_HCM))):
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    axs[3].plot(t, ina, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[3].plot(t_b, ina_b, 'k', label = 'Baseline')

axs[3].legend(fontsize = 5, loc='upper right')
axs[3].set_ylabel('iNa (A/F)', fontsize=14)
axs[3].set_xlabel('Time (ms)', fontsize=14)

plt.suptitle('HCM Currents', fontsize=20)
plt.savefig('HCM_Currents.png')
plt.show()

#%%

############ PLOT CTRL CURRENTS #############
fig, axs = plt.subplots(4, 1, figsize=(16, 8))

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina = currents(pop_CTRL[i])
    axs[0].plot(t, iks, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

axs[0].plot(t_b, iks_b, 'k', label = 'Baseline')

axs[0].legend(fontsize = 5, loc='upper right')
axs[0].set_ylabel('iKs (A/F)', fontsize=14)

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina = currents(pop_CTRL[i])
    axs[1].plot(t, ikr, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

axs[1].plot(t_b, ikr_b, 'k', label = 'Baseline')

axs[1].legend(fontsize = 5, loc='upper right')
axs[1].set_ylabel('iKr (A/F)', fontsize=14)

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina = currents(pop_CTRL[i])
    axs[2].plot(t, ical, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

axs[2].plot(t_b, ical_b, 'k', label = 'Baseline')

axs[2].legend(fontsize = 5, loc='upper right')
axs[2].set_ylabel('iCaL (A/F)', fontsize=14)

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina = currents(pop_CTRL[i])
    axs[3].plot(t, ina, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

axs[3].plot(t_b, ina_b, 'k', label = 'Baseline')

axs[3].legend(fontsize = 5, loc='upper right')
axs[3].set_ylabel('iNa (A/F)', fontsize=14)
axs[3].set_xlabel('Time (ms)', fontsize=14)

plt.suptitle('CTRL Currents', fontsize=20)
plt.savefig('CTRL_Currents.png')
plt.show()

#%%
############ PLOT CURRENTS TOGETHER #############

fig, axs = plt.subplots(4, 1, figsize=(16, 8))

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina = currents(pop_CTRL[i])
    axs[0].plot(t, iks, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    axs[0].plot(t, iks, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[0].plot(t_b, iks_b, 'k', label = 'Baseline')

axs[0].legend(fontsize = 5, loc='upper right')
axs[0].set_ylabel('iKs (A/F)', fontsize=14)

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina = currents(pop_CTRL[i])
    axs[1].plot(t, ikr, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    axs[1].plot(t, ikr, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[1].plot(t_b, ikr_b, 'k', label = 'Baseline')

axs[1].legend(fontsize = 5, loc='upper right')
axs[1].set_ylabel('iKr (A/F)', fontsize=14)

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina = currents(pop_CTRL[i])
    axs[2].plot(t, ical, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    axs[2].plot(t, ical, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[2].plot(t_b, ical_b, 'k', label = 'Baseline')

axs[2].legend(fontsize = 5, loc='upper right')
axs[2].set_ylabel('iCaL (A/F)', fontsize=14)

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina = currents(pop_CTRL[i])
    axs[3].plot(t, ina, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    axs[3].plot(t, ina, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs[3].plot(t_b, ina_b, 'k', label = 'Baseline')

axs[3].legend(fontsize = 5, loc='upper right')
axs[3].set_ylabel('iNa (A/F)', fontsize=14)
axs[3].set_xlabel('Time (ms)', fontsize=14)

plt.suptitle('Currents', fontsize=20)
plt.savefig('Currents.png')
plt.show()

