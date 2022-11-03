#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import log10

#%%
def plot_GA(ind):
    mod, proto, x = myokit.load('./kernik.mmt')

    for k, v in ind[0].items():
            mod['multipliers'][k].set_rhs(v)

    mod['ik1']['g_K1'].set_rhs(mod['ik1']['g_K1'].value()*(11.24/5.67))
    mod['ina']['g_Na'].set_rhs(mod['ina']['g_Na'].value()*(187/129))

    proto.schedule(4, 10, 1, 1000, 0) 
    sim = myokit.Simulation(mod,proto)
    sim.pre(1000 * 100) #pre-pace for 100 beats, to allow AP reach the steady state
    dat = sim.run(1000)
    t = dat['engine.time']
    v = dat['membrane.V']

    return t,v

#%%
def calc_APD(t, v, apd_pct):
    t = [i-t[0] for i in t]
    mdp = min(v)
    max_p = max(v)
    max_p_idx = np.argmax(v)
    apa = max_p - mdp
    repol_pot = max_p - apa * apd_pct/100
    idx_apd = np.argmin(np.abs(v[max_p_idx:] - repol_pot))
    apd_val = t[idx_apd+max_p_idx]

    return(apd_val)

#%%
def baseline_run():
    #Single Run
    mod, proto, x = myokit.load('./kernik.mmt')
    proto.schedule(4, 10, 1, 1000, 0) 

    ############### MATURE AP ##############################################
    # These two lines of code are used to mature the ipsc so it looks more adult-like
    mod['ik1']['g_K1'].set_rhs(mod['ik1']['g_K1'].value()*(11.24/5.67))
    mod['ina']['g_Na'].set_rhs(mod['ina']['g_Na'].value()*(187/129))
    ########################################################################

    sim = myokit.Simulation(mod, proto)
    sim.pre(1000 * 100)
    dat = sim.run(1000)

    t = np.array(dat['engine.time'])
    v = np.array(dat['membrane.V'])

    return t, v

#%%
def plot_g(ind):
    keys = [k for k in ind.keys()]

    curr_x = 0
    for k, conds in ind.items():
            for i, g in enumerate(conds):
                g = log10(g)
                x = curr_x + np.random.normal(0, .01)
                plt.scatter(x, g)

            curr_x += 1

    curr_x = 0

    plt.hlines(0, -.5, (len(keys)-.5), colors='grey', linestyle='--')
    plt.xticks([i for i in range(0, len(keys))],['GCaL', 'GKr', 'GKs', 'GNa', 'Gto', 'GK1', 'Gf'], fontsize=10)
    plt.ylim(log10(0.1), log10(10))
    plt.ylabel('Log10 Conductance', fontsize=14)
