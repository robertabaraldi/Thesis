#%%
import matplotlib.pyplot as plt
from functions import err_excel, currents, ind_excel

#%%

###### PLOT ERRORS, COMPARE WITH AP FEATURES ########

######## HCM ERRORS ############
plt.figure(figsize=(14,8))

gen = [i for i in list(range(1,80))]

err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10, err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6 = err_excel()

err_HCM = [err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10]
err_CTRL = [err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6]

c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen' 'darkgreen', 'forestgreen','seagreen']

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

########## PLOT CURRENTS ###########
plt.figure(figsize=(14,8))

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6 = ind_excel()
pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6]

for i in list(range(0,len(pop_HCM))):
    t, v, iks, ikr, ical, ina = currents(pop_HCM[i])
    plt.plot(t, iks, color=c_HCM[i], label = f'Trial_HCM_{i+1}')
    plt.plot(t, ikr, color=c_HCM[i], label = f'Trial_HCM_{i+1}')
    plt.plot(t, ical, color=c_HCM[i], label = f'Trial_HCM_{i+1}')
    plt.plot(t, ina, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

plt.legend(loc='upper right')
plt.ylabel('Time (ms)', fontsize=14)
plt.xlabel('Current (A/F)', fontsize=14)
plt.ylim(0,5000)
plt.suptitle('HCM Currents', fontsize=14)
plt.savefig('HCM_Currents.png')
plt.show()
