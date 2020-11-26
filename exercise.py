# a = 'hello' + 'there'
# print(a)
#
# b = int('hello 2018')
# # b = int('2018')
# print(type(b))
#
# # print('hello' + '2018')
#
#
# a = input("Enters Hours: ")




_max = -1
print('Before', _max)

for i in [9, 41, 12, 3, 74, 15]:
    if i > _max:
        _max = i
    print(_max, i)

print('After', _max)



word = "before"
for i in word:
    if i == 'o':
        continue
    if i == 'r':
        continue
    print(i)



for i in range(4):
    for j in range(3):
        # print(i, j)
        if j == 1:
            print(i, j)
            continue



x = int("123")
print(x+1)


# a = int(input("입력: "))
# print(a+1)


word = 'banana'
count = 0
for i in word:
    if i == 'a':
        count += 1

print("결과:", count)


# a = [i for i in range(2, 3, 0.1)]
a = [i/10 for i in range(0, 41)]
print(a)


for i in range(3):
    for j in range(4):
        print("[", i, j, "]", end='')
    print()



# words = 'Connect Foundation'
#
# if 'F' in words:
#     words.lower()
#     words[7] = '&'
# else:
#     print(words)
#
# print(words)


# print(words.find('Co'))
# a = words.replace(' ', '&')
# print(a)
#
#
#
#
#
# s = 'Apple'         # 문자열을 관리하는 객체 생성
# t = s + 'Orange'
# s = s + 'Banana'
# print(t, s)
#
# print(s.lower())    # 출력 결과를 소문자로
# print(s)            # s 자체는 변경X
#
# t = s.lower()       # 원본데이터는 변경시키지 않는 것이 원칙 return 값으로
# print(t)
#
# print(s.upper())    # 출력 결과를 대문자로
# print(s.replace('Banana', 'Orange'))        # 바나나 -> 오렌지
# print(s)            # s값이 변경이 안됐다는 것은 대치결과를 return 값으로 받아준 것
#
# print(s.replace('banana', 'Orange'))        # 대소문자




# a = "there is mere horse item mirror"
# b = a.find("m")
# # c = a.find(" ", 9)
# d = a[b:13]
# print(d.upper())
#
#
# thing = "duck"
# place = "lake"
# print(f'the {thing} is in the {place}')
#
#
# import random
# print(random.sample(range(1, 10), 2))













# # from urllib2 import Request, urlopen
# # from urllib.request import urlencode, quote_plus
# from urllib.request import urlopen
#
# url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson'
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('startCreateDt') : '20200310', quote_plus('endCreateDt') : '20200414' })
#
# request = Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read()
# print (response_body)




#
#
# from urllib.request import urlopen
# import json
# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)
#
# import pandas as pd
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                    dtype={"fips": str})
#
# import plotly.express as px
#
# fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
#                            color_continuous_scale="Viridis",
#                            range_color=(0, 12),
#                            scope="usa",
#                            labels={'unemp':'unemployment rate'}
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()






















