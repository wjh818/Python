# Static(통계)
"""
# 1) 친구 수 히스토그램
from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,
               13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,
               9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,
               7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
               5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
               3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friends_counts = Counter(num_friends)
xs = range(101)                         # 최대값은 100
ys = [friends_counts[x] for x in xs]    # 히스토그램의 높이는 해당 친구 수를 갖고 있는 사용자 수
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
# plt.show()

num_points = len(num_friends)
print(num_points)
largest_value = max(num_friends)
print(largest_value)
smallest_values = min(num_friends)
print(smallest_values)

# 크기 순을 정렬을 해 놓으면 맨 앞에 있는게 최소값, 맨 뒤에 있는게 최대값
sorted_values = sorted(num_friends)
print(sorted_values)
smallest_values = sorted_values[0]              # 1
print(smallest_values)
largest_value = sorted_values[-1]               # 100
print(largest_value)
second_largest_values = sorted_values[-2]       # 49
print(second_largest_values)





# 2) 중심 경향성
# 평균
def mean(x):
    return sum(x) / len(x)

print(mean(num_friends))        # 한 명이 평균적으로 갖고 있는 친구 수 = 7.33333




# 중앙값
def median_odd(a):
    return sorted(a)[len(a)//2]     # 정렬해서 가운데 있는 값 출력

def median_even(b):                 # b = [1, 9, 2, 10]
    sorted_b = sorted(b)            # sorted(b) = [1, 2, 9, 10]
    hi_midpoint = len(b)//2         # len(b)=4   len(b)//2=2
    return (sorted_b[hi_midpoint - 1] + sorted_b[hi_midpoint]) / 2
#               sorted_b[1] = 2              sorted_b[2] = 9
def median(c):
    return median_even(c) if len(c) % 2 == 0 else median_odd(c)


print(median([1, 10, 2, 9, 5]))     # 5
print(median([1, 9, 2, 10]))        # 5.5
print(median(num_friends))          # 6 -> len(num_friends) = 204로 짝수이므로 median_even함수 사용
### 주의사항 ###
"""
# def f1():
#     return 10
#
# def f2():
#     return f1()
#
# def f3():
#     return f2()
#
# print(f3())
#
#
#
#
# a = abs(-3)
# print(a)
#
# abs = 10        # 내장함수를 변수로 쓰면 그 기능을 잃음
# a = abs(-3)
# print(a)
"""




# print(int(3.14))
# print(int(0.2 * 260))
# print(0.2 * 260)

# 분위
def quantile(x, a):
    a_index = int(a * len(x))
    return sorted(x)[a_index]

# 0.10 * len(num_friends)      # 20.4000000
# int(0.10 * len(num_friends)) # 20
print(quantile(num_friends, 0.10))  # 1
# 0.25 * len(num_friends)        # 51.0
# int(0.25 * len(num_friends))   # 51
print(quantile(num_friends, 0.25))  # 3
print(quantile(num_friends, 0.75))  # 9
print(quantile(num_friends, 0.90))  # 13




# 최빈값
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

print(set(mode(num_friends)))
# print(Counter(num_friends))
# print(Counter(num_friends).values())
# print(max(Counter(num_friends).values()))
# print(Counter(num_friends).items())
# a = [x_i for x_i, count in Counter(num_friends).items()]
# print(a)





# 3) 산포도
import math

a = [1, 2, 3, 4, 5]         # 변위
b = sum(a)/len(a)           # 평균
print(b)
c = [x - b for x in a]      # 편차 (x: a의 데이터, b: 평균, a: 리스트)
print(c)
d = [abs(x) for x in c]
print(sum(d) / len(d))      # 평균 편차(편차 절댓값의 합의 평균)
e = [x ** 2 for x in c]
f = sum(e) / len(e)         # 분산(편차 제곱의 합의 평균)
print(f)
print(math.sqrt(f))         # 표준 편차(분산에 루트 씌운거)

# 짚고넘어가기
print(0 <= 3 <= 7)
print(0 <= 11 <= 7)
"""










# Probability(확률)
# 1) 조건부 확률
# from enum import Enum
# import random
#
# class kid(Enum):
#     boy = 0     # 0을 BOY로 치환해서 쓰겠다
#     girl = 1

# print(kid.boy)
# print(kid.boy.value)
# print(kid.boy.name)
# print(random.choice([kid.boy, kid.girl]))   # 둘 중에 하나 랜던하게 선택



# class Color(Enum):
#     red = 0
#     green = 1
#     blue = 2
#
# print(random.choice([Color.red, Color.green, Color.blue]))




# ct0 = 0
# ct1 = 0
# ct2 = 0
#
# for _ in range(1000):
#     a = random.choice([kid.boy, kid.girl])
#     b = random.choice([kid.boy, kid.girl])
#     if a == kid.boy:        # 50%
#         ct0 += 1
#     if a == kid.boy and b == kid.girl:      # 25%
#         ct1 += 1
#     if a == kid.boy or b == kid.girl:       # 75%
#         ct2 += 1
#
# print(ct0, ct1, ct2)
# print(ct1/ct0, ct1/ct2)




# from random import *
#
# ct = 0
# sum = 0
#
# for _ in range(10000):
#     sum += ct
#     ct = 0
#
#     while True:
#         a = randint(1, 10)
#         b = randint(1, 10)
#
#         if a != b:
#             # ct = 0
#             while True:
#                 c = randint(1, 10)
#                 d = randint(1, 10)
#                 # ct += 1
#
#                 if ((a == c and b == d) or (a == d and b == c)):
#                     break
#                 else:
#                     ct += 1
#
#
# print(sum/10000)





# 2) 정규분포
# import math
#
# SQRT_TWO_PI = math.sqrt(2 * math.pi)
#
# def normal_pdf(x=0, mu=0, sigma=1):
#     return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma)
#
#
# import matplotlib.pyplot as plt
#
# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
# plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
#
# plt.legend()
# plt.show()




###########################################################################################################





# 산점도
# from matplotlib import pyplot as plt
#
x = [2, 4, 6, 8]        # 공부한 시간
y = [81, 93, 91, 97]    # 점수
#
# # plt.axis("equal")
#
#
# plt.scatter(x, y)
# plt.show()



# 최소제곱법
# 실제 데이터에 가장 근사한 직선 그래프를 그린다
# y = ax + b 인 그래프를 만드는 것

# a = ((x - x의 평균) * (y - y의 평균))의 합 / ((x - x의 평균)^2)의 합
# a = ((2-5)*(81-90) + (4-5)*(93-90) + ...) / ((2-5)^2 + (4-5)^2 + ...)
# a = ((2-5)*(81-90.5) + (4-5)*(93-90.5) + (6-5)*(91-90.5) + (8-5)*(97-90.5)) / ((2-5)**2 + (4-5)**2 + (6-5)**2 + (8-5)**2)
# print(a)



# a 구하는 식
# 내가 푼거
a = [i-5 for i in x]    # x-x평균
# print(a)
b = [i-90.5 for i in y]     # y-y평균
# print(b)
c = sum((i-5)**2 for i in x)   # (x - x의 평균)^2의 합
# print(c)
d = sum(i*j for i, j in zip(a, b))  # (x - x의 평균) * (y - y의 평균))의 합
# print(d)

result = d / c      # 최종
print(result)



# a 구하는 식
# 편하게
def mean(xs):
    return sum(xs)/len(xs)

def least_squares(xs, ys):
    x_avg = mean(x)
    y_avg = mean(y)
    return sum((x - x_avg) * (y - y_avg) for x, y in zip(xs, ys)) / sum((x - x_avg)**2 for x in xs)

print(least_squares(x, y))



# numpy 사용해서 -> mean함수 따로 만들필요 없음
import numpy as np

mean_x = np.mean(x)
mean_y = np.mean(y)
print("x 평균: ", mean_x)
print("y 평균: ", mean_y)

t1 = sum((i-mean_x)*(j-mean_y) for i,j in zip(x,y))
print("분자: ", t1)

t2 = sum((i - mean_x)**2 for i in x)
print("분모: ", t2)

print("결과: ", t1/t2)




# b 구하기
# b = [j - 2.3*i for i, j in zip(x,y)]
# print(b)
# print(sum(b)/len(b))

a = t1/t2
b = mean_y - (mean_x * a)
print(b)



# 선형회귀 그래프
from matplotlib import pyplot as plt
                            # x = [2, 4, 6, 8]
c = [a*i+b for i in x]      # y = 2.3x + 79
print(c)

plt.plot(x, c, color='r')
plt.scatter(x, y)
# plt.show()



# 평균 제곱 오차(MSE)
y = [81, 93, 91, 97]    # 실제 값
# (예측값-실제 값)의 제곱의 합 평균
# (84.5-81)^2 + (88.5-93)^2 + .. / 4

k = [(i-j)**2 for i, j in zip(c, y)]
k1 = sum(k)/len(k)
print(k1)









# 문제.
d = [i for i in np.arange(0, 4.7, 0.1)]     # [0, 0.1, 0.2, 0.3, 0.4 ...]
print(d)

g = []

for i in range(len(d)):
    d1 = d[i]
    c = [d1 * i + 79 for i in x]
    k = [(i - j) ** 2 for i, j in zip(c, y)]
    k1 = sum(k) / len(k)
    g.append(k1)

print(g)


plt.plot(d, g)
plt.show()










x = [2, 4, 6, 8]
y = [81, 93, 91, 97]
xdata = np.array(x)
ydata = np.array(y)
print(type(xdata), xdata) # 배열이다.
a = 0; b = 0
lr = 0.05 # 확습률
for i in range(1000):
    y = a * xdata + b
    a_dif = -(1 / len(xdata)) * sum(xdata * (ydata-y))
    b_dif = -(1 / len(xdata)) * sum(ydata - y)
    a = a - lr * a_dif
    b = b - lr * b_dif
    print(i, round(a,3), round(b,3))