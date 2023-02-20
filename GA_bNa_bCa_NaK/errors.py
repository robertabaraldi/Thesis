import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, plot_GA, ind_excel, err_excel
import seaborn as sns
from math import log10
from scipy.signal import find_peaks

gen = [i for i in list(range(1,80))]

err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10, err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6, err_ctrl7, err_ctrl8, err_ctrl9, err_ctrl10 = err_excel()

err_HCM = [err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10]
err_CTRL = [err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6, err_ctrl7, err_ctrl8, err_ctrl9, err_ctrl10]

c_HCM = ['lightsteelblue', 'cyan', 'cornflowerblue', 'c', 'darkturquoise', 'dodgerblue', 'blue', 'royalblue', 'midnightblue', 'darkblue']
c_CTRL = ['lightgreen', 'lime', 'limegreen', 'yellowgreen', 'mediumseagreen', 'green', 'darkolivegreen', 'darkgreen', 'forestgreen','seagreen']


########## Errors HCM ###############
fig, axs = plt.subplots(1, 1, figsize=(12, 8))

for i in list(range(0,len(err_HCM))):
    best_err = list(err_HCM[i]['Best Error'])
    axs.scatter(gen, best_err, color=c_HCM[i], label = f'Trial_HCM_{i+1}')

axs.legend(loc='upper right')
axs.set_ylabel('Error', fontsize=14)
axs.set_xlabel('Generation', fontsize=14)
axs.set_ylim(0,4000)

fig.savefig('Errors_HCM.png')
plt.show()

########## Errors CTRL ##############

fig, axs = plt.subplots(1, 1, figsize=(12, 8))

for i in list(range(0,len(err_CTRL))):
    best_err = list(err_CTRL[i]['Best Error'])
    axs.scatter(gen, best_err, color=c_CTRL[i], label = f'Trial_CTRL_{i+1}')

axs.legend(loc='upper right')
axs.set_ylabel('Error', fontsize=14)
axs.set_xlabel('Generation', fontsize=14)
axs.set_ylim(0,4000)

fig.savefig('Errors_CTRL.png')
plt.show()
