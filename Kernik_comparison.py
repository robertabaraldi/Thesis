#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import baseline_run, calc_APD, build_pop
from scipy.signal import find_peaks 

#%%
############### NOT PACED ############################

########### KERNIK + GSEAL #########################
mod, proto, x = myokit.load('./kernik_leak_fixed.mmt')
proto.schedule(1, 10, .0001, 1000, 0) 

mod['membrane']['gLeak'].set_rhs(0.1)

sim = myokit.Simulation(mod, proto)
sim.pre(1000 * 100)
dat = sim.run(1200)

t_leak = np.array(dat['engine.time'])
v_leak = np.array(dat['membrane.V'])

plt.plot(t_leak,v_leak, label = 'Kernik + 0.1gseal')

############ KERNIK ##########################
mod, proto, x = myokit.load('./kernik.mmt')
proto.schedule(1, 10, .0001, 1000, 0) 

sim = myokit.Simulation(mod, proto)
sim.pre(1000 * 100)
dat = sim.run(1200)

t = np.array(dat['engine.time'])
v = np.array(dat['membrane.V'])

plt.plot(t,v, label = 'Kernik')
plt.savefig('Not paced.png')
plt.show()

# %%
################# PACED #############################

############### KERNIK + GSEAL #####################
mod, proto, x = myokit.load('./kernik_leak_fixed.mmt')
proto.schedule(4, 10, 1, 1000, 0) 

#mod['ik1']['g_K1'].set_rhs(mod['ik1']['g_K1'].value()*(11.24/5.67))
#mod['ina']['g_Na'].set_rhs(mod['ina']['g_Na'].value()*(187/129))

mod['membrane']['gLeak'].set_rhs(0.1)

sim = myokit.Simulation(mod, proto)
sim.pre(1000 * 100)
dat = sim.run(50000)

i_stim = dat['stimulus.i_stim']
peaks = find_peaks(-np.array(i_stim), distance=100)[0]
start_ap = peaks[-3] 
end_ap = peaks[-2] 

t = np.array(dat['engine.time'][start_ap:end_ap])
t = t - t[0]
max_idx = np.argmin(np.abs(t-600))
t_leak = t[0:max_idx]
end_ap = start_ap + max_idx

v_leak = np.array(dat['membrane.V'][start_ap:end_ap])

plt.plot(t_leak,v_leak, label = 'Kernik + 0.1gseal')

############### KERNIK ##########################
mod, proto, x = myokit.load('./kernik.mmt')
proto.schedule(4, 10, 1, 1000, 0) 

sim = myokit.Simulation(mod, proto)
sim.pre(1000 * 100)
dat = sim.run(50000)

i_stim = dat['stimulus.i_stim']
peaks = find_peaks(-np.array(i_stim), distance=100)[0]
start_ap = peaks[-3] 
end_ap = peaks[-2] 

t = np.array(dat['engine.time'][start_ap:end_ap])
t = t - t[0]
max_idx = np.argmin(np.abs(t-1200))
t = t[0:max_idx]
end_ap = start_ap + max_idx

v = np.array(dat['membrane.V'][start_ap:end_ap])

plt.plot(t,v, label = 'Kernik')
plt.savefig('Paced.png')
plt.show()

#%%

