
#%% 
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, calc_APD, build_pop
from scipy.signal import find_peaks 

#%%
####### TO CHOOSE PRE-PACING ##########

t, v = baseline_run()

plt.plot(t,v)

apd_val = calc_APD(t, v, 90)

#%% 
######## ANOTHER WAY TO CHECK PRE-PACING ##########
import random
from math import log10
from HCM_GA_KernikUpdate import get_normal_sim_dat
import matplotlib.pyplot as plt
from math import ceil
import pandas as pd
import numpy as np

ind_list = build_pop(3)

for i in ind_list:
    t, v, cai, i_ion = get_normal_sim_dat([i])
    '''# fixed number of columns
    cols = 5
    # number of rows, based on cols
    rows = ceil(pop/cols)
    # new subplot with (i + 1)-th index laying on a grid
    plt.subplot(rows, cols, i + 1) 
    plt.plot(t,v)'''
    apd_val = calc_APD(t, v, 90)

plt.plot(t,v)


# %%
