import numpy as np
import pandas as pd

si = pd.Series([1, 2.0, '가', True, np.nan], index=[1, '삼', 5, 7, 9])
print(si)

df = pd.DataFrame([1, 2.0, '가', True, np.nan],
                  index=[1, '삼', 5, 7, 9],
                  columns=['A'])
print(df)

# Series
# 생성
si = pd.Series([1, 2, 3, 4, 5], index=list('abcde'))
print(si)

si2 = pd.Series({'e': 5, 'b': 2, 'd': 4, 'c': 3, 'a': 1})
print(si2)

si3 = pd.Series(si2, index=['a', 'b', 'n', 'd'])
print(si3)

si4 = pd.Series(1, index=list('abcde'))
print(si4)

for k, v in si.items():
    print(f'{k}: {v}')

# 인덱스    
print(si['c':'e'])
print(si['e':'c':-1])

#연산
si = pd.Series([1, 2, 3, 4, 5, np.nan])
print(si.sum())
print(pd.Series.sum(si))

print(si.notnull())

# 날짜 인덱스
print(pd.to_datetime(['1/1/2019 08:15AM', '2019-08-15 15:30']))

print(pd.date_range(start='2019-05-01', end='2019-05-10'))
print(pd.date_range(start='2019-05-01', end='2019-05-10', periods=20))
print(pd.date_range(start='2019-05-01', end='2019-05-10', freq='3D'))
print(pd.date_range(start='2019-05-01', periods=7))
print(pd.date_range(start=pd.Timestamp.now(), periods=7))





