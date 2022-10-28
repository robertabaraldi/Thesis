#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import log10
import random

#%%
def plot_GA(ind):
    #mod, proto, x = myokit.load('./kernik_leak_fixed.mmt')
    mod, proto, x = myokit.load('./paci-2013-ventricular-leak-fixed.mmt')

    for k, v in ind[0].items():
            k1, k2 = k.split('.')
            mod[k1][k2].set_rhs(v)

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
    mod, proto, x = myokit.load('./kernik_leak_fixed.mmt')
    #mod, proto, x = myokit.load('./paci-2013-ventricular-leak-fixed.mmt')
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
def build_pop(pop):
    
    ind_list = []

    for i in list(range(0,pop)):
        """
        Creates the initial population of individuals. The initial 
        population 

        Returns:
            An Individual with conductance parameters 
        """
        tunable_parameters=['iks.g_scale',
                            'ical.g_scale',
                            'ikr.g_scale',
                            'ina.g_scale',
                            'ito.g_scale',
                            'ik1.g_scale',
                            'ifunny.g_scale',
                            'membrane.gLeak']

        lower_exp = log10(0.1)
        upper_exp = log10(10)
        initial_params = [10**random.uniform(lower_exp, upper_exp)
                            for i in range(0, len(
                                tunable_parameters))]

        keys = [val for val in tunable_parameters]
        ind = dict(zip(keys, initial_params)) 
        ind_list.append(ind)
    
    return ind_list