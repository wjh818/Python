# Vector
"""
# 1) 벡터 덧셈
def f1(a, b):
    c = []
    c.append(a[0] + b[0])
    c.append(a[1] + b[1])
    c.append(a[2] + b[2])
    return c


print(f1([0, 1, 2], [3, 4, 5]))



# 2) 벡터 덧셈 - 반복문 이용해서
def f2(a, b):
    result = [i+j for i, j in zip(a, b)]
    return result


print(f2([0, 1, 2], [3, 4, 5]))



# 3) 벡터로 구성된 리스트에서 모든 벡터의 각 성분을 더할 때
def f3(a):
    num = len(a[0])
    return [sum(vector[i]
                for vector in a)
                for i in range(num)]


# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# a[0] = [1, 2]  ->  num = len(a[0]) = 2
# vector = [1,2], [3,4], [5,6], [7,8]
# vector[0] = 1, 3, 5, 7   /   vector[1] = 2, 4, 6, 8
print(f3([[1, 2], [3, 4], [5, 6], [7, 8]]))



# 4) 스칼라 곱셈
def f4(c, v):
    return [c * i for i in v]


print(f4(2, [1, 2, 3]))
print(f4(0.5, [1, 2, 3]))



# 5) 평균 구하기
def f5(v):
    n = len(v)
    return f4(1/n, f3(v))


# f3(v) = [9, 12]
# len(v) = 3
print(f5([[1, 2], [3, 4], [5, 6]]))



# 6) 내적 구하기 (성분별 곱한 값 더하기)
def f6(v, w):
    return sum(i*j for i, j in zip(v, w))


# zip(v, w) = [(1,4), (2,5), (3,6)]
#               i j    i j    i j
print(f6([1, 2, 3], [4, 5, 6]))     # 1*4 + 2*5 + 3*6 = 36



# 7) 내적 이용해서 벡터의 크기 계산
import math

def f7(v):
    return math.sqrt(f6(v, v))      # math.sqrt: 제곱근을 계산해주는 함수


# f6([3,4], [3,4]) = 3*3 + 4*4 = 25
print(f7([3, 4]))



# 8) 벡터 뺄셈
def f8(v, w):
    return [i-j for i, j in zip(v, w)]


print(f8([5, 7, 9], [4, 5, 6]))



# 9) 두 벡터 간의 거리 계산
def f9(a, b):
    return f7(f8(a, b))


# f8([4,0], [0,3]) = [4, -3]
# f7(f8(a, b)) = f7([4, -3])    -> f7은 제곱근 구하는 함수
print(f9([4, 0], [0, 3]))
"""












# Matrix
"""
# 1) 몇 행 몇 열 인지 구하기
from typing import Tuple

def f1(a):
    r = len(a)
    c = len(a[0])
    return r, c


print(f1([[1, 2, 3],
          [4, 5, 6]]))


# 2) 원하는 원소 값 출력
# 행 출력
def f2(a, i):
    return a[i]  # 행렬 a의 i번째 행 출력


# 열 출력
def f3(a, j):
    return [i[j]  # i행의 j번째 원소
            for i in a]  # 행렬 a의 i행에 대해서


print(f2([1, 2, 3], 0))
print(f2([[1, 2, 3],
          [4, 5, 6]], 0))
print(f3([[1, 2, 3],
          [4, 5, 6]], 1))


# 3) 단위행렬 만들기
# 틀 (rXc 행렬)
def f4(r, c, fn):
    return [[fn(i, j)
             for i in range(c)]
             for j in range(r)]


# 안에 값 (nXn 단위행렬)
def f5(n):
    return f4(n, n, lambda i, j: 1 if i == j else 0)


# lambda 함수 풀어 쓴거
# def f6(i, j):
#     if i == j:
#         return 1
#     else:
#         return 0

for i in f5(5):  # -> 보기 좋게 출력하기 위한 용도
    print(i)
"""



# 4) 행렬의 곱
A = [[1, 2],
     [3, 4],
     [5, 6]]

B = [[1, 2, 3],
     [4, 5, 6]]

result = []

def get_column(a, b):
    return [i[b] for i in a]

# g = zip(A,B)
# print(list(g))

# def get_column(a, b):
#     return [i[b] for i in a]        # 행렬 a에 대해서 i행의 b열 구하기


def mul_matrix(a, b):
    print(len(a[0]), len(b))        # a의 열의 개수, b의 행의 개수 출력
                                    # 두 값이 같아야 행렬의 곱이 가능하니까 확인차 출력

    for a_row in a:
        result_row = []
        for j in range(len(b[0])):      # b의 열의 개수만큼 반복
            b_col = get_column(b, j)    # b_col = get_column(b, 0), get_column(b, 1), get_column(b, 2)
                                        #               [1, 4]              [2, 5]          [3, 6]
            result_row.append(sum(a_row_v * b_col_v
                                  for a_row_v, b_col_v
                                  in zip(a_row, b_col)))
                        # zip([1,2], [1,4]) = [(1,1),(2,4)]     ->9
                        # zip([1,2], [2,5]) = [(1,2),(2,5)]     ->12
                        # zip([1,2], [3,6]) = [(1,3),(2,6)]     ->15
                        # zip([3,4], [1,4]) = [(3,1),(4,4)]     ->19
                        # zip([3,4], [2,5]) = [(3,2),(4,5)]     ->26
                        # zip([3,4], [3,6]) = [(3,3),(4,6)]     ->33
                        # zip([5,6], [1,4]) = [(5,1),(6,4)]     ->29
                        # zip([5,6], [2,5]) = [(5,2),(6,5)]     ->40
                        # zip([5,6], [3,6]) = [(5,3),(6,6)]     ->51
        result.append(result_row)



mul_matrix(A, B)
print('====================')
for rows in result:
    print(rows)