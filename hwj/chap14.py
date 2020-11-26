import json

path = 'example.txt'
records = [json.loads(line) for line in open(path, encoding='UTF8')]
# print(records[0])

#
# time_zones = [rec['tz'] for rec in records]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones)
print(time_zones[:10])

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)
print(counts['America/New_York'])
print(len(time_zones))
print(counts)

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

print(top_counts(counts))

from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))

import pandas as pd

frame = pd.DataFrame(records)
print(frame.info())
print(frame['tz'][:10])

tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))


import seaborn as sns
subset = tz_counts[:10]
# sns.barplot(y=subset.index, x=subset.values)
# plt.show()

print(frame['a'][0])
print(frame['a'][50])
print(frame['a'][1][:5])  # long line

results = pd.Series([x.split()[0] for x in frame.a.dropna()])
# results = [x.split() for x in frame.a.dropna()]
print(results)
print(results[:5])
print(results.value_counts()[:8])

cframe = frame[frame.a.isnull()]
print(cframe)
cframe = frame[frame.a.notnull()]
print(cframe)
cframe = cframe.copy()
print(cframe)

import numpy as np

cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
print(cframe['os'][:5])

################################################################### 여기서부터

by_tz_os = cframe.groupby(['tz', 'os'])

agg_counts = by_tz_os.size().unstack().fillna(0)
# os.size(): 그룹별 합계       unstack(): 표로 배치
print(agg_counts[:10])


# Use to sort in ascending order (오름차순으로 정렬)
indexer = agg_counts.sum(1).argsort()   # argsort(): 작은값부터 정렬
print(indexer[:10])
count_subset = agg_counts.take(indexer[-10:])       # [-10:]: 맨 뒤에서부터 10개
print(count_subset)
##### 위랑 똑같은건데 더 편리하게 할 수 있는 방법
agg_counts.sum(1).nlargest(10)
print(agg_counts.sum(1).nlargest(10))


# Rearrange the data for plotting (시각화를 위해 데이터 재배치)
count_subset = count_subset.stack()
count_subset.name = 'total'
count_subset = count_subset.reset_index()
print(count_subset[:10])

# sns.barplot(x='total', y='tz', hue='os',  data=count_subset)
# plt.show()





# 정규화한 데이터를 그리기위해서

def norm_total(group):
    group['normed_total'] = group.total / group.total.sum()
    return group

results = count_subset.groupby('tz').apply(norm_total)


sns.barplot(x='normed_total', y='tz', hue='os',  data=results)
plt.show()

# 더 효율적으로 하는 거
g = count_subset.groupby('tz')
results2 = count_subset.total / g.total.transform('sum')