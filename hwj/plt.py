# 예제01.
# 환경 설정 방법
# File > Setting > matplotlib 설치


# 예제02.
# 1) 형태01.
# import matplotlib.pyplot
# matplotlib.pyplot.plot()
# matplotlib.pyplot.show()

# 2) 형태02. pyplot 생략하고 출력 가능
# from matplotlib.pyplot import *
# plot()
# show()

# 3) 형태03.
# import matplotlib.pyplot as plt
# plt.plot()
# plt.show()




# 예제03. plot의 종류
# 1) lineplot: 점과 점 사이를 선으로 이어줌
# 2) barplot: 막대그래프 형태로 보여줌 (barchart)
# 3) histogram(히스토그램) plot
# 4) scatter plot
# 5) contour(컨투어) plot
# 6) surface plot
# 7) box plot




# 예제04. 그래프의 title 설정
# import matplotlib.pyplot as plt
# plt.title("title")
# plt.show()




# 예제05. 리스트 설정
# 1)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16])     # y축 값으로 설정됨
# plt.show()

# 2)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])       # 순서대로 x축, y축 값으로 설정됨
# plt.show()

# 3)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 40])       # x,y 갯수 안맞으면 불가능
# plt.show()

# 4)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
# plt.grid(True)      # 격자 보여줌 -> 아무데나 써도 나옴
# plt.show()

# 5)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
# plt.xlabel("x-label")       # x축 이름
# plt.ylabel("y-label")       # y축 이름
# plt.show()

# 6) 기존의 plot을 그대로 유지한 채 새로운 plot을 추가하는 것을 "hold"라고 함
# import matplotlib.pyplot as plt
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.plot([10, 20, 30, 40], [3, 7, 11, 20])
# plt.plot([10, 20, 30, 40], [5, 8, 13, 24])
# plt.show()

# 7)
# import matplotlib.pyplot as plt
# plt.plot([10, 20, 30, 40], range(4))        # range로도 나타낼 수 있음
# plt.plot([10, 20, 30, 40], range(2, 6))
# plt.show()




# 예제06. 꾸미기
# 1) 색상 설정
# import matplotlib.pyplot as plt
# plt.plot(range(1, 5), "r")      # 색상 설정
# plt.plot(range(2, 6), "g")
# plt.plot(range(3, 7), "b")
# plt.plot(range(4, 8), "c")
# plt.plot(range(5, 9), "m")
# plt.plot(range(6, 10), "y")
# plt.plot(range(7, 11), "k")
# plt.plot(range(8, 12), "w")
# plt.plot(range(8, 12), range(1, 5), "m")
# plt.show()

# 2) 마크 설정
# import matplotlib.pyplot as plt
# a = '.,ov^<>w1234sp*hH+xDd'     # 문자열로도 끄집어낼 수 있다
# for k, v in enumerate(a):
#     print(k, v)
#     plt.plot(range(1+k, 5+k),  v + '-')
# plt.show()

# 3) 선 스타일 설정
# import matplotlib.pyplot as plt
# plt.plot(range(1, 5), '-')
# plt.plot(range(2, 6), '--')
# plt.plot(range(3, 7), '-.')
# plt.plot(range(4, 8), ':')
# plt.show()

# 4) 색상+마크+선스타일 모두
# import matplotlib.pyplot as plt
# plt.plot(range(2, 6), 'r^:')        # 세가지 한번에 설정(색상, 마크, 선스타일 순서로)
# plt.plot(range(1, 7), range(4, 10), 'co-.')        # 세가지 한번에 설정(색상, 마크, 선스타일 순서로)
# plt.show()

# 5) 선 세부 설정
# import matplotlib.pyplot as plt
# plt.plot(
#     [10, 20, 30, 40],  # x축
#     [1, 4, 9, 16],   # y축
#     c="m",    # 선 색깔
#     lw=4,     # 선 굵기
#     ls=":",      # 선 스타일
#     marker="^",       # 마커 종류
#     ms=5,        # 마커 크기
#     mec="g",      # 마커 선 색깔
#     mew=10,        # 마커 선 굵기
#     mfc="y"       # 마커 내부 색깔
# )
# plt.show()




# 예제07.
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40], 'co-.')
# plt.xlim(-10, 30)       # x의 유효범위 (x축의 범위)
# plt.ylim(-20, 70)       # y의 유효범위 (y축의 범위)
# plt.grid(True)
# plt.show()




# 예제08.
# 1)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
# plt.xticks(range(0, 50, 10))        # x축의 간격
# plt.yticks(range(0, 50, 10))        # y축의 간격
# plt.show()

# 2)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
# plt.xticks([1, 2, 3, 4], ["oneday", "twoday", "threeday", "fourday"], rotation="70")        # 글자 겹치지 않게 70도 회전시켜서 보여줘라
# plt.yticks([1, 2, 3, 4], ["tiger", "lion", "dog", "cat"])
# plt.show()




# 예제09. legend(범례)
# import matplotlib.pyplot as plt
# plt.plot([10, 20, 30, 40], label="Tiger")
# plt.plot([5 ,6, 7, 8], label="Lion")
# plt.legend(loc=7)
# # 범례 위치
# #   2   9   1
# #   6       7
# #   3   8   4
# plt.show()




# 예제10. 배경색 설정
# import matplotlib.pyplot as plt
# plt.gca().set_facecolor([0.5, 0.3, 0.8])
# plt.show()




# 예제11. 창 크기 조절
# import matplotlib.pyplot as plt
# plt.figure(figsize=(6.4, 4.8))  # default 크기
# plt.figure(figsize=(6.4*2, 4.8*2))
# plt.show()



# 예제12. 한글 깨지지 않게
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# font_location = 'C:/Windows/Fonts/malgun.ttf' # 오른쪽 마우스 정보 얻음
# font_family = fm.FontProperties( fname=font_location).get_name()
# plt.rc( 'font', family = font_family )
# plt.plot(["호랑이", "코끼리", "돼지"])
# plt.show()




# 예제13. 하나의 창에 여러개의 plot 그래프
# import matplotlib.pyplot as plt
# plt.subplot(2, 2, 2)        # 맨 마지막 인수가 위치 설정함
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
# plt.subplot(2, 2, 3)
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
# plt.subplot(4, 3, 1)        # 앞에 두 인수(4, 3)에 의해 크기 설정
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
# plt.show()




# 예제14. y축 2개 사용하기
# import matplotlib.pyplot as plt
# age = [10,20,30,40,50,60]
# weight = [20, 40, 55, 50, 70, 63]
# height = [100, 120, 140, 150, 170, 165]
# plt.plot(age, weight, 'r')
# plt.twinx()
# plt.plot(age, height, 'b')
# plt.show()




# 예제15.
# import matplotlib.pyplot as plt
# plt.plot([10, 20, 30, 40], 'y')
# fig = plt.gcf()
# plt.show()
# fig.savefig("test.png")




# 예제16. bar 차트
# 1)
# import matplotlib.pyplot as plt
# plt.bar([1, 2, 3], [2, 3, 1])
# plt.show()

# 2) 가로로 출력 barh
# import matplotlib.pyplot as plt
# plt.barh([1, 2, 3], [2, 3, 1])
# plt.show()

# 3)
# import matplotlib.pyplot as plt
# a = ["python", "c++", "java", "scala", "lisp", "perl", "javascript"]
# b = [12, 8, 10, 6, 14, 3, 9]
# plt.subplot(1,2,1)
# plt.bar(a, b, align='edge')     # align='edge' 또는 align='center'
# plt.subplot(1,2,2)
# plt.barh(a, b)                  # align='center'는 디폴트 값으로 생략 가능
# plt.show()

# 4)
# import matplotlib.pyplot as plt
# a = ["python", "c++", "java", "scala", "lisp", "perl", "javascript"]
# b = [12, 8, 10, 6, 14, 3, 9]                                      # 단축키: ctrl+b
# plt.bar(a, b, width=0.2, bottom=10, align='edge', alpha=0.5)      # width: 두께 설정 / bottom: 밑바닥 시작 위치 설정
#                                                                   # alpha: 배경색과 막대그래프의 색이 섞이는 정도
# plt.show()




# 예제17. 위치값 조절, 두 그래프를 겹쳐서 사용
# import matplotlib.pyplot as plt
# import numpy as np
# a = [0, 1, 2, 3]
# # a = a + 3     불가능
# a = range(4)
# # a = a + 3     불가능
# a = np.arange(4)
# a = a + 3       # 가능 -> numpy를 쓰는 이유
# print(type(a), a)       # list 타입 아님(콤마 없음)
# a = a + 0.5
# print(a)
#
# 1)
# a = plt.bar( np.arange(4)+0.3, [90, 55, 40, 65], 0.4, color='c', label='Tiger')
# b = plt.bar( np.arange(4)+0.6, [65, 40, 55, 95], 0.4, color='m', label="Lion" )
# plt.legend(loc=9)
# plt.show()
#
# 2)
# import matplotlib.pyplot as plt
# import numpy as np
# a = plt.bar( np.arange(4), [90, 55, 40, 65], 0.4)
# b = plt.bar( np.arange(4), [65, 40, 55, 95], 0.4, bottom=[90, 55, 40, 65])
# plt.show()
#
# 3) 년도별 우리나라 석탄 채굴량
import matplotlib.pyplot as plt
from random import *
import matplotlib.font_manager as fm
font_location = 'C:/Windows/Fonts/malgun.ttf' # 오른쪽 마우스 정보 얻음
font_family = fm.FontProperties( fname=font_location).get_name()
plt.rc( 'font', family = font_family )

year = [1900 + i*10 for i in range(12)]
x = []
for _ in range(12):
    a = randint(100, 1000)
    x.append(a)
print(x)

plt.bar(year, x, width=5, color='g')
plt.title("년도별 석탄 채굴량")
plt.xlabel("연도")
plt.ylabel("석탄 채굴량")
plt.xticks(rotation=30)
plt.grid("True")
plt.show()
#
# 4) 문제 유형
# 나이대별 급여 / 직업별 월급 차이 / 성별 급여 차이 / 학과별 경쟁률 / 월별 수익률 / 팀별 성적
# 종교 유무별 이혼률 / 동물원별 사자와 호랑이에 대한 개체수 / 나라별 인구수 / 나라별 남자 여자에 대한 인구수
# 연령대별 성별에 대한 월급 차이 / 성별 직업에 대한 빈도수 / 지역별 연령대 비율 / 연령대별 정당에 대한 지지율
# 지역별 정당에 대한 지지율 / 나라별 금은동 메달 수 / 도시별 성별에 대한 범죄율 / 기타 등등...
# 경제 성장률 / 자살률 / 합격률 / 취업률 / 백분율(타율) / 판매량 / 재고량 / 성장률 / 생산량 / 분포량 / 빈도 / 유입량 / 이자율A



