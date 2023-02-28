import pandas as pd
import statistics as stat

df_hcm = pd.read_excel('Cond_HCM.xlsx')
df_ctrl = pd.read_excel('Cond_CTRL.xlsx')

hcm_mean=df_hcm.mean()
ctrl_mean=df_ctrl.mean()

print(hcm_mean)
print(ctrl_mean)