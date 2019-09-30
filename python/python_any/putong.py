from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
with open('datas/example.txt','r') as f:
    record = f.readlines()
records = [json.loads(i) for i in record]
 
frame = DataFrame(records)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'haha'
tz_counts = clean_tz.value_counts()
#tz_counts[:10].plot(kind='barh', rot=0)
#plt.show()
results = Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])
print(results.value_counts()[:8])
cframe = frame[frame.a.notnull()]
op_sys = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
print(op_sys[:5])
os_tz = cframe.groupby(['tz', op_sys])
os_tz_counts = os_tz.size().unstack().fillna(0)

print(os_tz_counts[:10])

index_tz = os_tz_counts.sum(1).argsort()

print(index_tz[:10])

count_subset = os_tz_counts.take(index_tz)[-10:]

print(count_subset)

count_subset.plot(kind='barh', stacked=True)
plt.show()

normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
plt.show()
