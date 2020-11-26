# numpy
# 데이터를 수치적으로 관리하고 싶을 때 사용



# Swith문
# a = {10:"호랑이", 20:"사자", 20:"독수리"}
#
# # def f1(dan):
# #     for i in range(1,10):
# #         print(dan*i)
# #
# # def f2(num):
# #     sum = 0
# #     for i in range(num):
# #         sum += num
# #     print(sum)
#
# def f1(n):
#     a = {10: "호랑이", 20: "사자", 20: "독수리"}
#     print(a[n])
#
# f1(10)
#
#
# def f2():
#     print("나는 구구단")
#
# def f3():
#     print("나는 합산")
#
# def f4(n):
#     b = {10: f2, 20: f3}
#     b[n]()
#
# f4(20)
#
#
# # b = {10: f1, 20: f2}
# #
# # for i in b:
# #     if i == 10:
# #         f1(3)
# #     if i == 20:
# #         f2(2)
#
#
################################################################
#
#
# XOR
# # Exclusive or (XOR)
# print(False ^ False)        # 둘이 같으면 false
# print(True ^ False)         # 둘이 달라야 true
# print(False ^ True)
# print(True ^ True)
#
#
#################################################################
#
#
# import numpy as np
#
# a = np.arange(10)   # [0 1 2 3 4 5 6 7 8 9]
# b = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(a, b)
#
#
# for _ in range(10):
#     c = a - 2
# print(c)            # [-2 -1  0  1  2  3  4  5  6  7]
#
# # for _ in range(10):
#     # d = b - 2
# # print(d)            # error
#
#
#
#
#
# a = np.random.randn(3, 4)       # (행의 갯수, 열의 갯수)
# print(a); print(sep="*"*50)
#
# b = a + a
# print(b); print(sep="*"*50)
#
# c = a + b
# print(c); print(sep="*"*50)
#
# print(a.shape, a.dtype)
#
#
#
#
# a = [1, 2, 3, 4]
# b = np.array(a)     # list를 array 형태로 바꾸고싶을 때
# print(b)
# print(b.ndim)
#
#
# a = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ]
# b = np.array(a)
# print(b)
# print(b.ndim)       # dimension(배열)
#
#
#
#
# print(np.zeros(5))
# print(np.zeros((3, 4, 2)))
#
#
#
# a = np.arange(10)
# print(a)
#
#
# a = np.array([[1., 2., 3.],
#                [4., 5., 6.]])
# b = np.array([[2., 3., 4.],
#                [5., 6., 7.]])
#
# print(a+b); print(sep="*")
# print(1/a); print(sep="*")
# print(4**0.5)
#
#
#
# a = np.arange(10)
# print(a)
# print(a[5])
# print(a[5:8])
# a[5:8] = 12
# print(a)
# b = a[5:8]
# print(b)
# b[1] = 12345
# print(a)
# a[:] = 7
# print(a)
#
#
# a = np.array([[1., 2., 3.],
#               [4., 5., 6.]])
# print(a)
# print(a[1])
# print(a[1][2])        # 위, 아래 똑같음
# print(a[1, 2])
# # print(a[2][1])      # error: out of bounds
# a[1,2] = 100
# print(a)
# a[1, 2] = 200
# print(a)
#
#
#
#
# a = np.array([[1., 2., 3.],
#               [4., 5., 6.]])
# b = a[:2, 1:]
# print(b); print(sep="*")
#
#
#
# a = np.array([[1., 2., 3., 4.],
#               [5., 6., 7., 8.],
#               [9., 10., 11., 12]])
# print(a[:2, 2:]); print(sep="*")
# print(a[1:, 1:3]); print(sep="*")
# print(a[:, 1:3]); print(sep="*")
#
#
#
# a = np.array(["호랑이", "코끼리", "독수리", "호랑이", "독수리"])
# print(a == "호랑이")
# print(~(a == "호랑이"))    # 부정(~) -> 원래 결과를 반전시킴
#
#
#
# a = np.empty((8, 4))
# for i in range(8):
#     a[i] = i
# print(a); print(sep="*")
#
#
#
# a = np.arange(32)
# b = a.reshape((8, 4))        # 1차원 배열을 2차원 배열로
# print(a); print(sep="*")
# print(b); print(sep="*")
#
#
#
# # 전치
# a = np.arange(15).reshape((3, 5))
# print(a); print(sep="*")
# print(a.T); print(sep="*")
# # 행렬 곱
# print(np.dot(a, a.T))
#
#
# a = np.arange(10)
# print(a)
# print(np.sqrt(a))
#
#
# a = np.array([-10, 0, 10])
# print(np.sign(a))       # 각 원소의 부호 계산( -1:음수, 0:영, 1:양수)
#
#
# a = np.array([1, 2, 3])
# b = np.array([2, 3, 4])
# print(a+b)
# print(np.add(a, b)); print(sep="*")




# points = np.arange(-5, 5, 0.01)
# xs, ys = np.meshgrid(points, points)
# print(ys); print(sep="*")
# z = np.sqrt(xs**2 + ys**2)
# print(z); print(sep="*")
#
# import matplotlib.pyplot as plt
# plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# # plt.show()




# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([True, False, True, True, False])
#
# result = [(x if c else y)
#           for x, y, c in zip(xarr, yarr, cond)]
# print(result)
#
# result = np.where(cond, xarr, yarr)
# print(result); print(sep="*")




# arr = np.random.randn(4, 4)
# print(arr)
# print(arr > 0)
# print(np.where(arr > 0, 2, -2))     #
# print(np.where(arr > 0, 2, arr)); print(sep="*")   # 양수를 2로 바꾸기




# a = np.random.randn(5, 4)
# print(a)
# print(a.mean())
# print(np.mean(a))
# print(a.sum())
# print(a.mean(axis=1))
# print(a.sum(axis=0)); print(sep="*")




# b = np.array([0, 1, 2, 3, 4, 5, 6, 7])
# print(b.cumsum()); print(sep="*")       # 누적합


# c = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(c)
# print(c.cumsum(axis=0))     # 세로(axis=0) 누적합
# print(c.cumsum(axis=1))     # 가로(axis=1) 누적합
# print(c.cumprod(axis=0))    # 세로 누적곱
# print(c.cumprod(axis=1)); print(sep="*")    # 가로 누적곱




# a = np.arange(10)
# np.save('some_array', a)
# print(np.load('some_array.npy'))


###########################################################################


# import numpy as np
#
# x = np.array([[1., 2., 3.],
#               [4., 5., 6.]])
# y = np.array([[6., 23.],
#               [-1, 7],
#               [8, 9]])
#
# print(x); print(sep="*")
# print(y); print(sep="*")
# print(x.dot(y))
# print(np.dot(x, y)); print(sep="*")     # 동일( x.dot(y) = np.dot(x, y) )
#
# print(np.ones(3))
# print(np.dot(x, np.ones(3)))
# print(x @ np.ones(3)); print(sep="*")


##########################################################################


# from numpy.linalg import inv, qr
#
# x = np.random.randn(3, 3)
# print(x); print(sep="*")
# print(x.T); print(sep="*")
#
# y = inv(x)      # 역행렬 구하기
# print(y); print(sep="*")
#
# mat = x.T.dot(x)
# print(inv(mat)); print(sep="*")
#
#
# a = np.array([1, 2, 3])
# b = np.diag(a)          # diag:
# print(np.trace(b)); print(sep="*")      # trace: 대각선 원소의 합


#############################################################################


# A*x=b에서 x 값 구하기
# 문제1)
# A = np.array([[1,2],
#               [3,4]])
# b = np.array([[6,7],
#               [8,9]])
#
# x = np.linalg.solve(A,b)
# print(x); print(sep="*")


# 문제2)
# A = np.array([[2, 3],
#               [3, 1]])
# b = np.array([[5],
#               [2]])
#
# x = np.linalg.solve(A, b)
# print(x); print(sep="*")



# 문제3)
# (1) 좌표 이동
# x = [10, 20, 20, 10, 10]
# y = [10, 10, 20, 20, 10]
#
# dx = 50
# dy = 30
#
# newx = []
# newy = []
#
# for i in range(len(x)):
#     c = x[i]
#     d = y[i]
#     a = [[1, 0, dx],
#          [0, 1, dy],
#          [0, 0, 1]]
#     b = [[c],
#          [d],
#          [1]]
#     t = np.dot(a, b)
#     newx.append(t[0])
#     newy.append(t[1])
#
# print(t)
# print(newx)
# print(newy)
#
# import matplotlib.pyplot as plt
#
# plt.plot(x, y)
# plt.plot(newx, newy)
# plt.xlim(0, 100)
# plt.ylim(0, 100)
# plt.show()


# (2) 회전 이동
# import math
# s = math.sin(math.radians(30))    # sin30
# c = math.cos(math.radians(30))    # cos30
#
# x = [10, 20, 20, 10, 10]
# y = [10, 10, 20, 20, 10]
#
# newx = []
# newy = []
#
# for i in range(len(x)):
#     l = x[i]
#     m = y[i]
#     a = [[c, -s, 0],
#          [s, c, 0],
#          [0, 0, 1]]
#     b = [[l],
#          [m],
#          [1]]
#     t = np.dot(a, b)
#     newx.append(t[0])
#     newy.append(t[1])
#
# print(t)
# print(newx)
# print(newy)
#
# import matplotlib.pyplot as plt
#
# plt.plot(x, y)
# plt.plot(newx, newy)
# # plt.xlim(0, 100)
# # plt.ylim(0, 100)
# plt.show()


# (3)
import math
import matplotlib.pyplot as plt
import numpy as np

x = [-5, 5, 5, -5, -5]
y = [-5, -5, 5, 5, -5]


# 크기 조절 함수
def s_func(sx, sy):
    s_x = []
    s_y = []
    for i in range(len(x)):
        l = x[i]
        m = y[i]

        sxy = [[sx, 0, 0],
               [0, sy, 0],
               [0, 0, 1]]
        b = [[l],
             [m],
             [1]]

        t = np.dot(sxy, b)
        s_x.append(t[0])
        s_y.append(t[1])


    return s_x,s_y

# x1,y1 = s_func(2,2)
# plt.plot(x1,y1)


# 회전 함수
def r_func(r):
    s = math.sin(math.radians(r))
    c = math.cos(math.radians(r))
    r_x = []
    r_y = []

    for i in range(len(x)):
        l = x[i]
        m = y[i]
        a = [[c, -s, 0],
             [s,  c, 0],
             [0,  0, 1]]
        b = [[l],
             [m],
             [1]]
        t = np.dot(a, b)
        r_x.append(t[0])
        r_y.append(t[1])

    return r_x, r_y

# x2,y2= r_func(30)
# plt.plot(x2,y2)


# 이동 함수
def t_func(dx, dy):
    t_x = []
    t_y = []

    for i in range(len(x)):
        l = x[i]
        m = y[i]
        a = [[1, 0, dx],
             [0, 1, dy],
             [0, 0, 1]]
        b = [[l],
             [m],
             [1]]
        t = np.dot(a, b)
        t_x.append(t[0])
        t_y.append(t[1])

    return t_x, t_y

# x3,y3=t_func(20,10)
# plt.plot(x3,y3)


# 세 개 다 합친 함수
def all(sx, sy, r, dx, dy):

    s = math.sin(math.radians(r))
    c = math.cos(math.radians(r))

    sxy = [[sx, 0, 0],
           [0, sy, 0],
           [0, 0, 1]]

    sc = [[c, -s, 0],
          [s, c, 0],
          [0, 0, 1]]

    dxy = [[1, 0, dx],
           [0, 1, dy],
           [0, 0, 1]]

    a_x = []
    a_y = []

    for i in range(len(x)):
        l = x[i]
        m = y[i]
        b = [[l],
             [m],
             [1]]
        t = np.dot(np.dot(dxy, np.dot(sc, sxy)), b)
        a_x.append(t[0])
        a_y.append(t[1])
    return a_x, a_y

x4, y4 = all(0.5, 0.5, 30, 20, 20)
# plt.plot(x4, y4)


# plt.plot(x, y)
# plt.xlim(-50, 50)
# plt.ylim(-50, 50)
# plt.show()


##############################################################################


import random

position = 0
walk = [position]
steps = 1000

for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])
# plt.show()


nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
print(draws)
steps = np.where(draws > 0, 1, -1)
print(steps)
walk = steps.cumsum()
print(walk)

print(walk.min())
print(walk.max())

print(np.abs(walk >= 10).argmax())




nwalks = 5000
nesteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
print(draws)
steps = np.where(draws > 0, 1, -1)
print(steps)
walks = steps.cumsum(1)
print(walks)

print(walks.min())
print(walks.max())

hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum())

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times)
print(crossing_times.mean())


