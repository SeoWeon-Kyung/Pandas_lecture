import numpy as np
import pandas as pd

df = pd.read_csv('python/datasets/airport_month_test.csv')
print(df)
print(df.info())

df = pd.read_excel('python/datasets/airport_month.xlsx')
print(df)
print(df.info())

#%%
df = pd.read_excel('python/datasets/로또당첨번호_수정.xlsx')
print(df)
print(df.info())

# 당첨 번호 빈도 통한 최다 추첨 숫자 찾기 - 당첨 번호 전체를 하나의 열로 변환
df1 = pd.melt(df, id_vars=['회차']
              , value_vars=['1번', '2번', '3번', '4번', '5번', '6번']
              , var_name='추첨순서', value_name='당첨번호')
display(df1)
print(df1.loc[df1['회차']==900])

result = df1['당첨번호'].value_counts()
print("==== result ====")
print(result)
print(result.sort_index())

result.to_excel('./python/data_result/로또당첨번호빈도수.xlsx'
                , sheet_name='당첨번호 빈도')

#%%
df = pd.read_excel('python/datasets/airport_month.xlsx')
print(df)
# 일자 열 없앤 것
df1 = df.drop('일자', axis=1)  # 열 = 1
print(df1)

print(df1.sum())  # decault : 세로로 더함

df2 = df.T   # 전치
df2 = df2.drop('일자')  # axis=0 기본, 행 삭제
print(df2)
print(f'{" 일자별 합 ":=^20}')
print(df2.sum())

#%%
df = pd.read_excel('python/datasets/airport_month.xlsx', index_col='일자')
display(df)
print(df.info())

#'공항별 총계' 행 추가
df.loc['공항별총계'] = df.sum()

# '일자별 총계' 열 추가
df['일별총계'] = df.sum(axis=1)   # 행 = 1 가로로 합 
print(df)

"""
drop method -  axis=0 이 가로 한줄 없앰
sum method -   axis=0 이 세로로 값 다 더함
"""


#%%













































































