# series
# dataframe

import pandas as pd
import numpy as np

# 예제01. 데이터 프레임 생성
# 1)
# data = {"이름": ["황원정1", "황원정2", "황원정3"],
#      "나이": [20, 30, 40],
#      "고향": ["서울", "부산", "제주도"]}
#
# df = pd.DataFrame(data)
# print(df)

# 2)
# a = [10, 20, 30, 40]    # 많은 부분에서 필드의 성격을 지닌다
# b = [50, 60, 70, 80]
# c = [a, b]
#
# df = pd.DataFrame(c).T  # T 붙이고 안붙이고 -> 행과 열이 뒤집힘
# df.columns = ['나이', '급여']
# print(df)
#



# 예제02.
# df = pd.DataFrame(columns=('이름', '나이', '고향'))  # 컬럼만 생성
# print(df)
# print(len(df))  # 0이 출력됨. 로우값이 없다는 뜻
#
# #CRUD
# df.loc[20] = ['호랑이', '30', '서울']  # 20은 키값이고 컬럼순으로 데이터 입력
# df.loc[30] = ['너구리', '20', '부산']
# df.loc[30] = ['얼룩말', '45', '대구']  # update
# print(df)
#
# # 한번에 10개 데이터 넣고 싶을 때
# for i in range(10):
#     df.loc[len(df)] = ["이순신" + str(i), 50+i, "울산"]
# print(df); print("-" * 30)
#
#
# df = df.drop([20, 3, 4, 5])     # D, 삭제
# print(df)
#
# print(df.loc[30])    # 해당 데이터 값 찾아줌
# print(df[2:4]); print("-" * 30)     # 인덱스 번호 2, 3 찾아줌
#
# print(df)
# print(df.head())    # 앞에 있는 데이터 5개 정도 보여줌
# print(df.head(3))    # 앞에 3개만 보고싶을때 (갯수 지정)
# print(df.tail()); print("-" * 30)     # 뒤에 있는 데이터 5개 정도 보여줌

###########################################################################################################

# # Series (1차원 데이터)
# obj = pd.Series([4, 7, -5, 3])
# print(obj)
# print(obj.values)
# print(obj.index)    # range(4)와 같음
#
# obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print(obj2)
# print(obj2.index)
# print(obj2['a'])
# obj2['d'] = 6       # 갱신(update)
# print(obj2)
# print(obj2[['c', 'a', 'd']])        # 여러 값 선택
# print(obj2[obj2 > 0])
# print(obj2 * 2)
# print(np.exp(obj2))
# print('b' in obj2)
# print('e' in obj2)
#
# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# obj3 = pd.Series(sdata)
# print(obj3)
#
# states = ['California', 'Ohio', 'Oregon', 'Texas']
# obj4 = pd.Series(sdata, index=states)
# print(obj4)
# print(pd.isnull(obj4))
# print(pd.notnull(obj4))
# print(obj4.isnull())
#
# print(obj3)
# print(obj4)
# print(obj3 + obj4)
#
# obj4.name = 'population'
# obj4.index.name = 'state'
# print(obj4)
#
# print(obj)
# obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
# print(obj)

#########################################################################################

# # DataFrame
# data = {'state': ['Ohio', 'Ohio', 'Nevada', 'Nevada'],
#         'year': [2000, 2004, 2006, 2008],
#         'pop': [1.5, 1.7, 2.4, 3.8]}
#
# frame = pd.DataFrame(data)
# print(frame)
# print(frame.head())
# print(pd.DataFrame(data, columns=['year', 'pop', 'state']))  # 원하는 순서를 가진 dataframe
#
# frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four'])
# print(frame2)
# print(frame2.columns)
# print(frame2['state'])
# print(frame2.year)
# print(frame2.loc['three'])
# frame2['debt'] = 16.5
# print(frame2)
# frame2['debt'] = np.arange(4.)
# print(frame2)
# val = pd.Series([-1.2, -1.5], index=['two', 'four'])    # 색인에 따라 대입하기
# frame2['debt'] = val
# print(frame2)
# del frame2['debt']   # debt 컬럼 삭제하기
# print(frame2.columns)
#
# pop = {'Nevada': {2001: 2.4, 2002: 2.9},
#        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
#
# frame3 = pd.DataFrame(pop)
# print(frame3)
# print(frame3.T)

##########################################################################################################

# 핵심 기능
# reindex
# obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# print(obj)
#
# obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# print(obj2)
#
# obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# print(obj3)
#
# obj3.reindex(range(6), method='ffill')      # ffill을 이용해 누락된 값을 직접의 값으로 채워 넣을 수 있음
# print(obj3.reindex(range(6), method='ffill'))
#
#
# frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
#                      index=['a', 'c', 'd'],
#                      columns=['Ohio', 'Texas', 'California'])
# print(frame)
#
# frame2 = frame.reindex(['a', 'b', 'c', 'd'])
# print(frame2)
#
# states = ['Texas', 'Utah', 'California']
# print(frame.reindex(columns=states))


# 하나의 로우나 컬럼 삭제하기
# obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# print(obj)
#
# new_obj = obj.drop('c')
# print(new_obj)
#
# print(obj.drop(['d', 'c']))
#
#
# data = pd.DataFrame(np.arange(16).reshape((4, 4)),
#                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
#                     columns=['one', 'two', 'three', 'four'])
# print(data)

##################################################################################################

# df = pd.DataFrame({
#     "t1": [2, 4, 6],
#     "t2": [81, 93, 91]
# })
#
# print(df)
# print(df.corr(method='pearson'))
# print(df['t1'].corr(df['t2']))  # 이 둘의 상관관계 계산 - 방법1
# print(df.t1.corr(df.t2))        # 이 둘의 상관관계 계산 - 방법2
# print(df['t1'].cov(df['t2']))  # 이 둘의 공분산 계산


# df = pd.DataFrame( columns=[ 't1', 't2' ], dtype='int64')
# print(df.columns)
# df.loc[0] = [2, 81]
# df.loc[1] = [4, 93]
# df.loc[2] = [6, 91]
# df.loc[3] = [8, 97]
# print(df)
# # print(df.dtypes())
# print(df.corr(method='pearson'))    # 문제의 코드
# # print(df.dtypes())
# print(df['t1'].corr(df['t2'])) # 요것이 에러

###############################################################################################

# 유일값, 값 세기, 멤버십
# obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
#
# uniques = obj.unique()
# print(uniques)  # 중복되는 값 제거하고 유일값만
# print(obj.value_counts())   # 갯수
#
# a = pd.value_counts(obj.values, sort=False)
# print(a)    # 갯수 세서 순차정렬
#
# print(obj)
#
# mask = obj.isin(['b', 'c'])
# print(mask)
# print(obj[mask])    # b,c만 뽑아냄
#
# to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
# unique_vals = pd.Series(['c', 'b', 'a'])
# print(pd.Index(unique_vals).get_indexer(to_match))  # [0 2 1 1 0 2] = [c의 인덱스 번호, a의 인덱스 번호 ...]


##############################################################################################

# df = pd.read_csv('mytxt/ex1.csv')
# print(df)
#
# df = pd.read_csv('mytxt/ex1.csv', header=None)
# print(df)
#
# df = pd.read_csv('mytxt/ex1.csv', names=['나이', '월급', '급여', '형제', '고향'])
# print(df)
#
# names=['나이', '월급', '급여', '형제', '고향']
# df = pd.read_csv('mytxt/ex1.csv', names=names, index_col='고향')
# print(df)


#################################################################################################


"""

python에서 oracle 접속하기
1. Oracle 서버가 설치된 폴더가 시스템 환경변수 path에 등록되어 있어야 한다.
    C:\oraclexe\app\oracle\product\11.2.0\server\bin
2. Oracle Instant Client dll 을 사용하기 위해 path 설정
    C:\Study\instantClient_11_2
3. cx_Oracle 파이썬 패키지를 설치
    1) pip install 명령어를 사용: pip install cx_Oracle
    2) pyCharm에서 설치(File -> Project -> Proejct Interpreter)

"""
# 1) pandas 이용하지 않고
# # cx_Oracle 패키지 모듈들을 import
# import cx_Oracle as oci
#
# # Oracle 서버와 연결(Connection 맺기)
# # conn = oci.connect('hwj', '1234', 'localhost:1521/orcl')
# conn = oci.connect('hwj/1234@localhost:1521/orcl')
#
#
# # Connection 확인
# # print(conn.version)
# conn.version
#
# # Oracle DB의 test_member 테이블 검색(select)
# cursor = conn.cursor() # cursor 객체 얻어오기
# cursor.execute('select * from STUDY') # SQL 문장 실행
#
# # print(cursor.fetchall())  # 한번에 불러옴
#
# # rows = cursor.fetchall()  # 원하는 순서의 데이터 뽑아오기
# # print(rows[3])
#
# # print(cursor.fetchone())  # 하나만 불러옴
#
# # print(cursor.fetchmany())  # 원하는 갯수만큼 불러옴
#
# # for rs in cursor:   # for문 돌려서 하나씩
# #     print(rs)
#
# cursor.close() # cursor 객체 닫기
#
# # Oracle 서버와 연결 끊기
# conn.close




# 2) pandas 이용해서
# import cx_Oracle
# db = cx_Oracle.connect('hwj','1234', 'localhost:1521/orcl')
# print('{}'.format(db.version))
#
# import pandas as pd
# datas = pd.read_sql(sql='select * from STUDY', con = db)
# print(datas)
# db.close


#############################################################################################


# data = pd.DataFrame({'호랑이': [10, 20, 30, 40],
#                        '사자': [15, 25, 35, 45]})
# print(data)
#
#
# fn = 'mytxt/out.csv'      # 파일명 지정해준거
# # data.to_csv(fn)     # 데이터를 csv로 넣겠다
# data.to_csv(fn, sep='|')
#
# fn = '호%d랑%d이' % (10, 20)
# print(fn)
#
#
# for i in range(10):
#     fn = 'mytxt/Tiger%04d.csv' % i  # 네자리 맞춰서 000i
#     data.to_csv(fn)
#     print(fn)
#
#
# import sys
# a = data.to_csv(sys.stdout, sep='|')
# print(a)


##############################

#
# data = pd.DataFrame({'호랑이': [10, None, 30, 40],
#                        '사자': [15, 25, 35, 45]})
#
# import sys
# b = data.to_csv(sys.stdout, na_rep='TIGER')     # 비어있는 데이어에 TIGER라고 넣겠다
# print(b)
#
#
#
# c = pd.read_csv('mytxt/0000.csv')   # null값이 있는 파일을 불러오면 어떻게 될까
# print(c)
#
# print(pd.isnull(c))     # 결측 데이터 찾기
# # print(c.fillna('missing'))      # 결측 데이터 채워넣기
# print(c.replace(to_replace=np.nan, value='missing'))        # replace함수 이용해서 결측 데이터 채워넣기


##############################


# x = pd.read_csv('mytxt/study.csv')
# print(x); print(sep="*")
#
#
# import csv
# f = open('mytxt/study.csv')
# reader = csv.reader(f)
#
# for line in reader:
#     print(line)
# print()
#
# with open('mytxt/study.csv') as f:
#     lines = list(csv.reader(f))
#
# print(lines); print(sep="*")
#
#
# header, values = lines[0], lines[1:]
# print(header)
# print(values); print(sep="*")
#
#
# data_dict = {h:v for h,v in zip(header, zip(*values))}
# # data_dict = {x for x in zip(header, zip(*values))}
# print(data_dict)


################################################

# a = [1, 2, 3]
# b = [[4, 5, 6]]
# print(a)
# print(b)
#
# for i in zip(a, *b):
#     print(i)


#################################################
# JSON

# ""을 문자열로 처리하고 싶어서 """ -> 주석 잡은게 아님
obj = """{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38, "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""
#
# import json
#
# result = json.loads(obj)        # json 문자열을 파이썬 형태로 변환
# print(result)
#
# asjson = json.dumps(result)     # 파이썬 객체를 json 형태로 변환
# print(asjson)
#
# siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
# print(result['siblings'])
# print(siblings)
#
# data = pd.read_json('mytxt/example.json')
# print(data)
# print(data.to_json())
# print(data.to_json(orient='records'))


#########################################################################################
# EXCEL

# xlsx = pd.ExcelFile('mytxt/ex1.xlsx')
#
# a = pd.read_excel(xlsx, 'Sheet1')
# print(a)
#
# frame = pd.read_excel('mytxt/ex1.xlsx', 'Sheet1')
# print(frame)
#
#
# writer = pd.ExcelWriter('mytxt/ex2.xlsx')
# frame.to_excel(writer, 'Sheet1')
# writer.save()
#
# frame.to_excel('mytxt/ex2.xlsx')

#############################################################################################

import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resp = requests.get(url)
print(resp)

data = resp.json()
print(data)

a = data[0]['title']
print(a)

issues = pd.DataFrame(data, columns=['number', ' title', 'labels', 'state'])
print(issues)



















