# 누락된 데이터 처리하기
import pandas as pd

string_data = pd.Series(['aardvark', 'artichoke', 'np.nan', 'avocado'])
print(string_data)
print(string_data.isnull())     # 결측 데이터 찾기 -> 불리언값으로 나타냄

string_data[0] = None
print(string_data.isnull())

#######################################################

# 7.1.1 누락된 데이터 골라내기
from numpy import nan as NA
import numpy as np

# (1)
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())    # 결측 데이터 있는 로우/컬럼 제외시킴(1)
print(data[data.notnull()])     # 결측 데이터 있는 로우/컬럼 제외시킴(2)



# (2)
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])
print(data)

cleaned = data.dropna()     # dataframe의 경우, NA 값을 하나라도 포함하고 있는 로우 제외시킴
print(cleaned)

print(data.dropna(how='all'))   # how='all': 모두 NA 값인 로우만 제외시킴

data[4] = NA
print(data)
print(data.dropna(axis=1, how='all'))   #axis=1, how='all': 모두 NA 값인 컬럼 제외시킴



# (3)
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))      # thresh=2: 2개 이상의 값이 들어있는 로우를 보고싶을 때
                                # df.dropna(thresh=2): 2개 이상의 결측 값 있는 로우 삭제

################################################################################################

# 위에 예제 이어서..
# 7.1.2 결측치 채우기
print(df.fillna(0))     # 결측치 0으로 채우기
print(df.fillna({1: 0.5, 2: 0}))    # 컬럼마다 다른 값으로 채우기(1열은 0.5, 2열은 0으로)

_ = df.fillna(0, inplace=True)      # 원래는 기존 데이터는 그대로 있는데 inplace=True 이걸로 기존 데이터를 바꿔버림
print(df)

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))        # 바로 위에 값으로 결측 데이터 채우기
print(df.fillna(method='ffill', limit=2))       # 채우는 갯수 제한 둘 수도 있음

data = pd.Series([1., NA, 3.5, NA, 7])
print(data.fillna(data.mean()))     # 결측 데이터 데이터의 평균값으로 채우기

#################################################################################################

# 7.2.1 중복 제거하기
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
print(data.duplicated())        # 중복인지 아닌지 알려줌
print(data.drop_duplicates())   # 중복인 데이터 삭제

data['v1'] = range(7)   # 컬럼명이 v1인 컬럼 새로 만들고
print(data.drop_duplicates(['k1']))     # k1 컬럼에 기반해서 중복 걸러냄

print(data.drop_duplicates(['k1', 'k2'], keep='last'))      # keep='last': 마지막으로 발견된 값 반환
                                                            # 기본적으론 처음 발견된 값 유지함

#################################################################################################

# 7.2.2 함수나 매핑을 이용해서 데이터 변형하기
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()   # 대소문자 섞여있으니까 모두 소문자로 바꿔줌
data['animal'] = lowercased.map(meat_to_animal)     # 일치하는거 매칭시켜주기
print(data)

data['food'].map(lambda x: meat_to_animal[x.lower()])       # 함수 통해서도 할 수 있음
print(data)

#################################################################################################

# 7.2.3 값 치환하기
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)

print(data.replace(-999, np.nan))   # -999 -> NaN
print(data.replace([-999, -1000], np.nan))  # 여러개의 값을 한번에 치환
print(data.replace([-999, -1000], [np.nan, 0]))     # 각각 다른 값으로 치환할 때
print(data.replace({-999: np.nan, -1000: 0}))       # 리스트 대신 딕셔너리 사용 가능

#################################################################################################

# 7.2.4 축 색인 이름 바꾸기
data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
transform = lambda x: x[:4].upper()     # 대문자로 변경
print(data.index.map(transform))

data.index = data.index.map(transform)  # 대문자로 변경된 축 이름 index에 바로 대입
print(data)

print(data.rename(index=str.title, columns=str.upper))      # 원래 객체 변경하지 않고 새로운 객체 생성

data.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'peekaboo'})