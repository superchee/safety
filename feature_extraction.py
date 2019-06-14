#%%
import numpy as np
import pandas as pd 
import tsfresh as ts 
import matplotlib.pyplot as plt 



#%%
data_all = pd.read_hdf("data_all.h5")



#%%
data_all.head()

#%%
data_all.columns

#%%
o_columns = ['bookingID', 'second', 'Accuracy', 'Bearing', 'acceleration_x', 'acceleration_y', 'acceleration_z', 'gyro_x', 'gyro_y', 'gyro_z', 'Speed']
o_columns_r = ['id', 'time', 'Accuracy', 'Bearing', 'acceleration_x', 'acceleration_y', 'acceleration_z', 'gyro_x', 'gyro_y', 'gyro_z', 'Speed']

#%%
data_all_r = data_all[o_columns]

#%%
data_all_r.columns = o_columns_r

#%%
data_all_r.head()

#%%
data_all_r[data_all_r['id']==8].plot(x='time', subplots=True, sharex=True, figsize=(10,10))
plt.show()


#%%
