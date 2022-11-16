import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, calc_APD, build_pop
from scipy.signal import find_peaks 


################# PACED #############################

############### KERNIK + GSEAL #####################
mod, proto, x = myokit.load('./paci-2013-ventricular-leak-fixed.mmt')
proto.schedule(4, 10, 1, 1000, 0) 

mod['membrane']['gLeak'].set_rhs(0.1)
mod['ical']['g_scale'].set_rhs(3)

sim = myokit.Simulation(mod,proto)
sim.pre(1000 * 100) #pre-pace for 100 beats, to allow AP reach the steady state
dat = sim.run(50000)

i_stim = dat['stimulus.i_stim']
peaks = find_peaks(-np.array(i_stim), distance=100)[0]
start_ap = peaks[-3] 
end_ap = peaks[-2]

t = np.array(dat['engine.time'][start_ap:end_ap])
t = t - t[0]
max_idx = np.argmin(np.abs(t-1000))
t_leak = t[0:max_idx]
end_ap = start_ap + max_idx

v_leak = np.array(dat['membrane.V'][start_ap:end_ap])

plt.plot(t_leak,v_leak, label = 'HCM')
plt.suptitle('HCM model')
plt.legend()
plt.savefig('HCM.png')
plt.show()