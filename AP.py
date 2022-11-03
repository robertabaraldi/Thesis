
#%% 
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import calc_APD
from functions import baseline_run
from scipy.signal import find_peaks 

#%%
################## TO CHOOSE PRE-PACING ######################

t, v = baseline_run()
peak_v = find_peaks(v, distance=100)
peak = v[peak_v[0][0]]
print(peak[0])
t_p = t[0:peak[0][0]]
v_p = v[0:peak[0][0]]

plt.plot(t,v)
plt.plot(t_p,v_p)

print(max(v))
print(v[peak[0][0]])


apd_val = calc_APD(t, v, 90)

#%% 
################ ANOTHER WAY TO CHECK PRE-PACING ################
import random
from math import log10
from HCM_GA import get_normal_sim_dat
import matplotlib.pyplot as plt
from math import ceil
import pandas as pd
from HCM_GA import get_normal_sim_dat
import numpy as np

pop=3
ind_list = []

for i in list(range(0,pop)):
    """
    Creates the initial population of individuals. The initial 
    population 

    Returns:
        An Individual with conductance parameters 
    """
    tunable_parameters=['i_cal_pca_multiplier',
                        'i_kr_multiplier',
                        'i_ks_multiplier',
                        'i_na_multiplier',
                        'i_to_multiplier',
                        'i_k1_multiplier',
                        'i_f_multiplier']

    lower_exp = log10(0.1)
    upper_exp = log10(10)
    initial_params = [10**random.uniform(lower_exp, upper_exp)
                        for i in range(0, len(
                            tunable_parameters))]

    keys = [val for val in tunable_parameters]
    ind = dict(zip(keys, initial_params)) 
    ind_list.append(ind)

    
#%%
for i in ind_list:
    print(i)
    t, v, cai, i_ion = get_normal_sim_dat([i])
    '''# fixed number of columns
    cols = 5
    # number of rows, based on cols
    rows = ceil(pop/cols)
    # new subplot with (i + 1)-th index laying on a grid
    plt.subplot(rows, cols, i + 1) 
    plt.plot(t,v)'''
    apd_val = calc_APD(t, v, 90)


# %%
