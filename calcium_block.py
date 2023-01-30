import matplotlib.pyplot as plt
from functions import ca_block, ind_excel, plot_GA, baseline_run
import pandas as pd

############## Calcium block HCM cells ########################

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10]
c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']
c_HCM_block = ['lightcoral', 'indianred', 'brown', 'firebrick', 'maroon', 'red', 'salmon', 'tomato', 'orangered', 'lightsalmon']

t, v, iks, ikr, ical, ina = baseline_run()
plt.plot(t, v, '-k', label = 'Baseline')

for i in list(range(0,len(pop_HCM))):
    t, v = plot_GA(pop_HCM[i])
    plt.plot(t, v, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

for i in list(range(0,len(pop_HCM))):
    t, v = ca_block(pop_HCM[i])
    plt.plot(t, v, color=c_HCM_block[i], label = f'Ca_block_Trial_HCM_{i+1}')

'''for i in list(range(0,len(pop_CTRL))):
    t, v = plot_GA(pop_CTRL[i])
    plt.plot(t, v, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

for i in list(range(0,len(pop_CTRL))):
    t, v = ca_block(pop_CTRL[i])
    plt.plot(t, v, color=c_HCM_block[i], label = f'Trial_CTRL_{i+1}')'''

plt.legend(loc='upper right')
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.savefig('Calcium_block.png')
plt.show()

##################################################################

