import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import ind_excel, currents

fig, axs = plt.subplots(1, 1, figsize=(12, 8))

### Baseline ###
ind = pd.read_excel('Best_ind.xlsx')
ind = ind.to_dict('index')
t_b, v_b, iks_b, ikr_b, ical_b, ina_b, cat_b = currents(ind)
###############

ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10 = ind_excel()
pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10]

c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']

for i in list(range(0,len(pop_HCM))):
    t, v, iks, ikr, ical, ina, cat = currents(pop_HCM[i])
    axs.plot(t, cat, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

for i in list(range(0,len(pop_CTRL))):
    t, v, iks, ikr, ical, ina, cat = currents(pop_CTRL[i])
    axs.plot(t, cat, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

axs.plot(t_b, cat_b, 'k', label = 'Baseline')

axs.legend(fontsize = 5, loc='upper right')
axs.set_ylabel('iKs (A/F)', fontsize=14)
plt.show()