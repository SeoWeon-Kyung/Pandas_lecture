import numpy as np
import pandas as pd

df = pd.read_csv('python/datasets/성적통계.csv', encoding='euc-kr')
print(df)

# cut 메서드
# 등급 나누기 - 구간 생성
print(pd.cut(df['국어'], 3))  # bins 로 구간, 값 등 조정 가능

bins = [0, 60, 70, 80, 90, 101]
bins_label = list('가양미우수')

df['등급'] = pd.cut(df['국어'], bins, right=False, labels=bins_label) 
print(df)

#%% 
df = pd.read_csv('python/datasets/신체치수.csv')
print(df)

print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# 결측치 확인
print(df[['wt', 'ht', 'waist']].isnull().sum() / len(df[['wt', 'ht', 'waist']]))
print(df[df['waist'].isnull() == True])

df1 = df.dropna(subset=['waist'])
print(df1[df1['waist'].isnull()==True])
sns.boxplot(x='wt', data=df1)
plt.show()

sns.lmplot(x='wt', y='waist', data=df1)
plt.show()

sns.lmplot(x='wt', y='ht', data=df1)
plt.show()

sns.lmplot(x='ht', y='waist', data=df1)
plt.show()

#%%
df = pd.DataFrame({'visitor': np.random.randint(1, 100, size=10)}
                  , index=pd.date_range('2019-01-01', periods=10, freq='1D'))
print(df)

# 하루씩 뒤로 미룸
df['전일'] = df.shift(1, fill_value=0)
print(df)

df['증가량'] = df['visitor'] - df['전일']
print(df)

































