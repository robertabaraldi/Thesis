#%%
import numpy as np
from functions import plot_GA, ind_excel
from scipy.signal import find_peaks 
import pandas as pd

#%%
ind_1, ind_2, ind_3, ind_4, ind_5, ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5 = ind_excel()

pop_HCM = [ind_1, ind_2, ind_3, ind_4, ind_5]
pop_CTRL = [ind_ctrl1, ind_ctrl2, ind_ctrl3, ind_ctrl4, ind_ctrl5]

############## HCM FEATURES ###############

ap_features = {}

t, v = plot_GA(pop_HCM[0])

# Voltage/APD features#######################
mdp = min(v)
max_p = max(v)
max_p_idx = np.argmax(v)
apa = max_p - mdp
dvdt_max = np.max(np.diff(v[0:30])/np.diff(t[0:30]))

ap_features['dvdt_max'] = dvdt_max
peak_v = find_peaks(v, distance=100)
peak = v[peak_v[0][0]]
ap_features['peak'] = peak
ap_features['apa']= apa

for apd_pct in [50, 90]:
    repol_pot = max_p - apa * apd_pct/100
    idx_apd = np.argmin(np.abs(v[max_p_idx:] - repol_pot))
    apd_val = t[idx_apd+max_p_idx]

    ap_features[f'apd{apd_pct}'] = apd_val

ap_features['mdp']= mdp

# Features
f = [ap_features]
df = pd.DataFrame(f)

for i in list(range(1,len(pop_HCM))):
    t, v = plot_GA(pop_HCM[i])

    # Voltage/APD features#######################
    mdp = min(v)
    max_p = max(v)
    max_p_idx = np.argmax(v)
    apa = max_p - mdp
    dvdt_max = np.max(np.diff(v[0:30])/np.diff(t[0:30]))

    ap_features['dvdt_max'] = dvdt_max
    peak_v = find_peaks(v, distance=100)
    peak = v[peak_v[0][0]]
    ap_features['peak'] = peak
    ap_features['apa']= apa

    for apd_pct in [50, 90]:
        repol_pot = max_p - apa * apd_pct/100
        idx_apd = np.argmin(np.abs(v[max_p_idx:] - repol_pot))
        apd_val = t[idx_apd+max_p_idx]

        ap_features[f'apd{apd_pct}'] = apd_val

    ap_features['mdp']= mdp

    # Features
    f = [ap_features]
    df1 = pd.DataFrame(f)
    df = pd.concat([df, df1])

df.to_excel('AP_features_HCM.xlsx', sheet_name='Sheet1',index=False)

############## CTRL FEATURES ###############

ap_features = {}

t, v = plot_GA(pop_CTRL[0])

# Voltage/APD features#######################
mdp = min(v)
max_p = max(v)
max_p_idx = np.argmax(v)
apa = max_p - mdp
dvdt_max = np.max(np.diff(v[0:30])/np.diff(t[0:30]))

ap_features['dvdt_max'] = dvdt_max
peak_v = find_peaks(v, distance=100)
peak = v[peak_v[0][0]]
ap_features['peak'] = peak
ap_features['apa']= apa

for apd_pct in [50, 90]:
    repol_pot = max_p - apa * apd_pct/100
    idx_apd = np.argmin(np.abs(v[max_p_idx:] - repol_pot))
    apd_val = t[idx_apd+max_p_idx]

    ap_features[f'apd{apd_pct}'] = apd_val

ap_features['mdp']= mdp

# Features
f = [ap_features]
df = pd.DataFrame(f)

for i in list(range(1,len(pop_CTRL))):
    t, v = plot_GA(pop_CTRL[i])

    # Voltage/APD features#######################
    mdp = min(v)
    max_p = max(v)
    max_p_idx = np.argmax(v)
    apa = max_p - mdp
    dvdt_max = np.max(np.diff(v[0:30])/np.diff(t[0:30]))

    ap_features['dvdt_max'] = dvdt_max
    peak_v = find_peaks(v, distance=100)
    peak = v[peak_v[0][0]]
    ap_features['peak'] = peak
    ap_features['apa']= apa

    for apd_pct in [50, 90]:
        repol_pot = max_p - apa * apd_pct/100
        idx_apd = np.argmin(np.abs(v[max_p_idx:] - repol_pot))
        apd_val = t[idx_apd+max_p_idx]

        ap_features[f'apd{apd_pct}'] = apd_val

    ap_features['mdp']= mdp

    # Features
    f = [ap_features]
    df1 = pd.DataFrame(f)
    df = pd.concat([df, df1])

df.to_excel('AP_features_CTRL.xlsx', sheet_name='Sheet1',index=False)

#%%


