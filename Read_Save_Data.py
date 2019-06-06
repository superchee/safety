#%%
import numpy as np
import pandas as pd




data_00001 = pd.read_csv("./features/part-00000-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00002 = pd.read_csv("./features/part-00001-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00003 = pd.read_csv("./features/part-00002-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00004 = pd.read_csv("./features/part-00003-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00005 = pd.read_csv("./features/part-00004-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00006 = pd.read_csv("./features/part-00005-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00007 = pd.read_csv("./features/part-00006-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00008 = pd.read_csv("./features/part-00007-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00009 = pd.read_csv("./features/part-00008-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")
data_00010 = pd.read_csv("./features/part-00009-e6120af0-10c2-4248-97c4-81baf4304e5c-c000.csv")




frames = [data_00001, data_00002, data_00003, data_00004, data_00005,data_00006,data_00007,data_00008,data_00009,data_00010]
data_all = pd.concat(frames, ignore_index=True)


data_sort = data_all.sort_values(by=['bookingID', 'second'])


data_sort


data_sort.to_hdf('data_all.h5', key='data_sort', mode = 'w')


#%%
