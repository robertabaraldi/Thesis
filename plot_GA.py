#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import plot_GA

#%%
###### PLOT BEST INDIVIDUALS FROM HCM_GA ALGORITHM #######
ind_1= pd.read_excel('Best_ind_1.xlsx')
ind_1 = ind_1.to_dict('index')

t1, v1 = plot_GA(ind_1)
plt.plot(t1, v1, '-b', label= 'Trial_1')

ind_2= pd.read_excel('Best_ind_2.xlsx')
ind_2 = ind_2.to_dict('index')

t2, v2 = plot_GA(ind_2)
plt.plot(t2, v2, '-m', label= 'Trial_2')

plt.legend()
plt.ylabel('Voltage (mV)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.suptitle('Best Individuals from GA', fontsize=14)
plt.show()

# %%
