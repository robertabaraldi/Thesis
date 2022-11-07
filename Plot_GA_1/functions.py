#%%
import myokit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import log10
import random
from scipy.signal import find_peaks 

#%%
def plot_GA(ind):
    mod, proto, x = myokit.load('./kernik_leak_fixed.mmt')

    for k, v in ind[0].items():
            k1, k2 = k.split('.')
            mod[k1][k2].set_rhs(v)

    proto.schedule(4, 10, 1, 1000, 0) 
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

    return t_leak,v_leak

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
    ################# PACED #############################

    ############### KERNIK + GSEAL #####################
    mod, proto, x = myokit.load('./kernik_leak_fixed.mmt')
    proto.schedule(4, 10, 1, 1000, 0) 

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
    max_idx = np.argmin(np.abs(t-1000))
    t_leak = t[0:max_idx]
    end_ap = start_ap + max_idx

    v_leak = np.array(dat['membrane.V'][start_ap:end_ap])
    peak_v = find_peaks(-v_leak, height=0, distance=100)
    first_peak = peak_v[0][0] #first is to choose between the peaks and the peak_height, then to choose the first peak

    t_leak = t_leak[0:first_peak]
    n_array = 1000 - t[first_peak] #compute time needed to arrive to 1000ms after end of AP
    t_array = np.array([i+1 for i in range(int(t[first_peak]),1000)])
    v_leak = v_leak[0:first_peak]
    last_v = v_leak[-1] #last potential value
    v_array = np.full(int(n_array+1),last_v)

    v_leak = np.concatenate((v_leak, v_array))
    t_leak = np.concatenate((t_leak, t_array))

    return t_leak, v_leak

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

#%%

def plot_cond(ind, lab):

    curr_x = 0
    keys = [k for k, v in ind[0].items()]

    for k, g in ind[0].items():
        g = log10(g)
        x = curr_x + np.random.normal(0, .01)
        plt.scatter(x, g, label = f'Trial_{lab}')
        curr_x += 1

    curr_x = 0

    plt.xticks([i for i in range(0, len(keys))], ['GKs', 'GCaL', 'GKr', 'GNa', 'Gto', 'GK1', 'Gf','Gleak'], fontsize=10)
    plt.ylim(log10(0.1), log10(10))
    plt.ylabel('Log10 Conductance', fontsize=14)
    plt.legend()

#%%
def ind_excel():
    ind_1 = pd.read_excel('Best_ind_1.xlsx')
    ind_1 = ind_1.to_dict('index')

    ind_2 = pd.read_excel('Best_ind_2.xlsx')
    ind_2 = ind_2.to_dict('index')

    ind_3 = pd.read_excel('Best_ind_3.xlsx')
    ind_3 = ind_3.to_dict('index')

    ind_4 = pd.read_excel('Best_ind_4.xlsx')
    ind_4 = ind_4.to_dict('index')

    ind_5 = pd.read_excel('Best_ind_5.xlsx')
    ind_5 = ind_5.to_dict('index')

    ind_6 = pd.read_excel('Best_ind_6.xlsx')
    ind_6 = ind_6.to_dict('index')

    ind_7 = pd.read_excel('Best_ind_7.xlsx')
    ind_7 = ind_7.to_dict('index')

    ind_8 = pd.read_excel('Best_ind_8.xlsx')
    ind_8 = ind_8.to_dict('index')

    ind_9 = pd.read_excel('Best_ind_9.xlsx')
    ind_9 = ind_9.to_dict('index')

    ind_10 = pd.read_excel('Best_ind_10.xlsx')
    ind_10 = ind_10.to_dict('index')

    ind_11 = pd.read_excel('Best_ind_11.xlsx')
    ind_11 = ind_11.to_dict('index')

    ind_12 = pd.read_excel('Best_ind_12.xlsx')
    ind_12 = ind_12.to_dict('index')

    ind_13 = pd.read_excel('Best_ind_13.xlsx')
    ind_13 = ind_13.to_dict('index')

    ind_14 = pd.read_excel('Best_ind_14.xlsx')
    ind_14 = ind_14.to_dict('index')

    return ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13, ind_14

#%%
def err_excel():
    err_1 = pd.read_excel('Errors_1.xlsx')

    err_2 = pd.read_excel('Errors_2.xlsx')

    err_3 = pd.read_excel('Errors_3.xlsx')

    err_4 = pd.read_excel('Errors_4.xlsx')

    err_5 = pd.read_excel('Errors_5.xlsx')

    err_6 = pd.read_excel('Errors_6.xlsx')

    err_7 = pd.read_excel('Errors_7.xlsx')

    err_8 = pd.read_excel('Errors_8.xlsx')

    err_9 = pd.read_excel('Errors_9.xlsx')

    err_10 = pd.read_excel('Errors_10.xlsx')

    err_11 = pd.read_excel('Errors_11.xlsx')

    err_12 = pd.read_excel('Errors_12.xlsx')

    err_13 = pd.read_excel('Errors_13.xlsx')
    
    err_14 = pd.read_excel('Errors_14.xlsx')

    return err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10, err_11, err_12, err_13, err_14
