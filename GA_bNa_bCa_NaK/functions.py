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
    max_idx = np.argmin(np.abs(t-900))
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
    max_idx = np.argmin(np.abs(t-990))
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

    #iks = np.array(dat['iks.i_Ks'][0:917])
    #ikr = np.array(dat['ikr.i_Kr'][0:917])
    #ical = np.array(dat['ical.i_CaL'][0:917])
    #ina = np.array(dat['ina.i_Na'][0:917])

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
def ind_excel():

    ind_1 = pd.read_excel('Best_ind1.xlsx')
    ind_1 = ind_1.to_dict('index')

    ind_2 = pd.read_excel('Best_ind2.xlsx')
    ind_2 = ind_2.to_dict('index')

    ind_3 = pd.read_excel('Best_ind3.xlsx')
    ind_3 = ind_3.to_dict('index')

    ind_4 = pd.read_excel('Best_ind4.xlsx')
    ind_4 = ind_4.to_dict('index')

    ind_5 = pd.read_excel('Best_ind5.xlsx')
    ind_5 = ind_5.to_dict('index')

    ind_6 = pd.read_excel('Best_ind6.xlsx')
    ind_6 = ind_6.to_dict('index')

    ind_7 = pd.read_excel('Best_ind7.xlsx')
    ind_7 = ind_7.to_dict('index')

    ind_8 = pd.read_excel('Best_ind8.xlsx')
    ind_8 = ind_8.to_dict('index')

    ind_9 = pd.read_excel('Best_ind9.xlsx')
    ind_9 = ind_9.to_dict('index')

    ind_10 = pd.read_excel('Best_ind10.xlsx')
    ind_10 = ind_10.to_dict('index')

    ind_11 = pd.read_excel('Best_ind11.xlsx')
    ind_11 = ind_11.to_dict('index')

    ind_12 = pd.read_excel('Best_ind12.xlsx')
    ind_12 = ind_12.to_dict('index')

    ind_13 = pd.read_excel('Best_ind13.xlsx')
    ind_13 = ind_13.to_dict('index')

    ind_14 = pd.read_excel('Best_ind14.xlsx')
    ind_14 = ind_14.to_dict('index')

    ind_15 = pd.read_excel('Best_ind15.xlsx')
    ind_15 = ind_15.to_dict('index')

    ind_ctrl1 = pd.read_excel('Best_ind_ctrl1.xlsx')
    ind_ctrl1 = ind_ctrl1.to_dict('index')

    ind_ctrl2 = pd.read_excel('Best_ind_ctrl2.xlsx')
    ind_ctrl2 = ind_ctrl2.to_dict('index')

    ind_ctrl3 = pd.read_excel('Best_ind_ctrl3.xlsx')
    ind_ctrl3 = ind_ctrl3.to_dict('index')

    ind_ctrl4 = pd.read_excel('Best_ind_ctrl4.xlsx')
    ind_ctrl4 = ind_ctrl4.to_dict('index')

    ind_ctrl5 = pd.read_excel('Best_ind_ctrl5.xlsx')
    ind_ctrl5 = ind_ctrl5.to_dict('index')

    ind_ctrl6 = pd.read_excel('Best_ind_ctrl6.xlsx')
    ind_ctrl6 = ind_ctrl6.to_dict('index')

    ind_ctrl7 = pd.read_excel('Best_ind_ctrl7.xlsx')
    ind_ctrl7 = ind_ctrl7.to_dict('index')

    ind_ctrl8 = pd.read_excel('Best_ind_ctrl8.xlsx')
    ind_ctrl8 = ind_ctrl8.to_dict('index')

    ind_ctrl9 = pd.read_excel('Best_ind_ctrl9.xlsx')
    ind_ctrl9 = ind_ctrl9.to_dict('index')

    ind_ctrl10 = pd.read_excel('Best_ind_ctrl10.xlsx')
    ind_ctrl10 = ind_ctrl10.to_dict('index')

    return ind_1, ind_2, ind_3, ind_4, ind_5, ind_6, ind_7, ind_8, ind_9, ind_10, ind_11, ind_12, ind_13, ind_14, ind_15, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5, ind_ctrl6, ind_ctrl7, ind_ctrl8, ind_ctrl9, ind_ctrl10

#%%
def err_excel():

    err_1 = pd.read_excel('Errors1.xlsx')

    err_2 = pd.read_excel('Errors2.xlsx')

    err_3 = pd.read_excel('Errors3.xlsx')

    err_4 = pd.read_excel('Errors4.xlsx')

    err_5 = pd.read_excel('Errors5.xlsx')

    err_6 = pd.read_excel('Errors6.xlsx')

    err_7 = pd.read_excel('Errors7.xlsx')

    err_8 = pd.read_excel('Errors8.xlsx')

    err_9 = pd.read_excel('Errors9.xlsx')

    err_10 = pd.read_excel('Errors10.xlsx')

    err_11 = pd.read_excel('Errors11.xlsx')

    err_12 = pd.read_excel('Errors12.xlsx')

    err_13 = pd.read_excel('Errors13.xlsx')

    err_14 = pd.read_excel('Errors14.xlsx')

    err_15 = pd.read_excel('Errors15.xlsx')

    err_ctrl1 = pd.read_excel('Errors_ctrl1.xlsx')

    err_ctrl2 = pd.read_excel('Errors_ctrl2.xlsx')

    err_ctrl3 = pd.read_excel('Errors_ctrl3.xlsx')

    err_ctrl4 = pd.read_excel('Errors_ctrl4.xlsx')

    err_ctrl5 = pd.read_excel('Errors_ctrl5.xlsx')

    err_ctrl6 = pd.read_excel('Errors_ctrl6.xlsx')

    err_ctrl7 = pd.read_excel('Errors_ctrl7.xlsx')

    err_ctrl8 = pd.read_excel('Errors_ctrl8.xlsx')

    err_ctrl9 = pd.read_excel('Errors_ctrl9.xlsx')

    err_ctrl10 = pd.read_excel('Errors_ctrl10.xlsx')

    return err_1, err_2, err_3, err_4, err_5, err_6, err_7, err_8, err_9, err_10, err_11, err_12, err_13, err_14, err_15, err_ctrl1, err_ctrl2, err_ctrl3, err_ctrl4, err_ctrl5, err_ctrl6, err_ctrl7, err_ctrl8, err_ctrl9, err_ctrl10

#%%
def stim(ind):
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
    max_idx = np.argmin(np.abs(t-980))
    t_leak = t[0:max_idx]
    end_ap = start_ap + max_idx

    v_leak = np.array(dat['membrane.V'][start_ap:end_ap])

    sim.reset()

    proto.schedule(0.04, 2011, 1000, 1000, 1)
    sim.set_protocol(proto)
    dat_rrc = sim.run(5000)

    i_stim = dat_rrc['stimulus.i_stim']
    peaks = find_peaks(-np.array(i_stim), height=10, distance=100)[0]
    start_ap = peaks[-3] 
    end_ap = peaks[-2]

    t = np.array(dat_rrc['engine.time'][start_ap:end_ap])
    t = t - t[0]
    max_idx = np.argmin(np.abs(t-980))
    t_rrc = t[0:max_idx]
    end_ap = start_ap + max_idx

    v_rrc = np.array(dat_rrc['membrane.V'][start_ap:end_ap])

    return t_leak, v_leak, t_rrc, v_rrc

#%%
def currents(ind):
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
    max_idx = np.argmin(np.abs(t-900))
    t_leak = t[0:max_idx]
    end_ap = start_ap + max_idx

    v_leak = np.array(dat['membrane.V'][start_ap:end_ap])
    iks = np.array(dat['iks.i_Ks'][start_ap:end_ap])
    ikr = np.array(dat['ikr.i_Kr'][start_ap:end_ap])
    ical = np.array(dat['ical.i_CaL'][start_ap:end_ap])
    ina = np.array(dat['ina.i_Na'][start_ap:end_ap])


    return t_leak,v_leak, iks, ikr, ical, ina