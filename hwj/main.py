# EX01.     Shift+F10 실행키
# = 주석
# print(10)
"""
print(10)
print(20)
"""
# 더블쿼텐션"""/쿼텐션''' 3개를 감싸면 주석이 된다
# Shift """전체 블럭 주석

# EX02.
"""
# 문자열 출력 방법
print('호랑이')
# 콤마(,)는 자동으로 space 포함해서 출력됨
print(10, '문자열', 20, "독수리")
# 부동소수타입
print(3.14)
# true와 false는 반드시 첫글자가 대문자
print(True)
print(False)
# 두줄짜리 코드 한줄로 쓰고 싶을 때 앞문장에 세미콜론(;) 붙이기
print(10); print(20)
"""

# EX03.
"""
print(10, end=' ')
print(20)
print(10, end='\n')  # 자동으로 줄바꿈 end='\n' (carriage return)이 생략되어있다
print(20)
print(10, end='')
print(20)
"""

# EX04.
"""
print('------------------------------')  # 세퍼레이트 = 구분선
print('-' * 50)  # 50개의 -

print('*' * 50)  # 출력하고자하는 문자열 반복

print('%d %d %s' % (10, 20, '호랑이'))  # 입력값은 %() 안에 입력
print('코%d 끼%d 리%s' % (10, 20, '호랑이'))  # 섞어서 사용 가능
"""

# EX05.   default 값의 활용 sep, end
"""
print(10, 20, 30, 40)
print(10, 20, 30, 40, sep=' ')
print(10, 20, 30, 40, sep=',')  # default -> sep(띄어쓰기 스페이스 또는 콤마로 나타내기)
print(10, 20, 30, 40, sep=',', end='\n')  # default -> end(의 default 값으로 줄바꿈도 제어가능 )
"""

# EX06.    변수의 type
"""
print(type(10), type('호랑이'), type(3.14), type(True))  # 변수의 type 정보를 알려줌
print(type([]), type(()), type({}))  # 결과: <class 'list'> <class 'tuple'> <class 'dict'>
"""

# EX07.      숫자 문자 연산
"""
print(10 + 20)
# print(10 + '호랑이')       # 문법 성립하지 않음
# print('호랑이' + 10)       # 문법 성립하지 않음
print('호랑이' + '독수리')

print(10 + int('123'))  # 문자열 -> 숫자      int('문자열')
print('호랑이' + str(10))  # 숫자 -> 문자열       str(숫자)
"""

# EX08.      변수를 선언하는 방법
"""
# 1) python에서 변수를 선언하는 타입은 없다 -> ex) int a = 10; int b = 20; (X)
a = 10
b = 20
print(a, b)

# 2) 중복변수를 선언할 경우 과거의 변수는 사라지고 새로 만든 변수가 적용된다 (가장 마지막의 변수만 적용)
a = 30; b = 40
print(a, b)

# 3) 변수를 2,3개 동시에 사용할 수 있다
a, b = 50, 60
print(a, b)
a, b, c, = 1, 2, 3
print(a, b, c)

# 4) 두 변수의 값을 동시에 대입할 수 있다
a = b = 70
print(a, b)

# error
# a = 10, b = 20      # 콤마(,) 사용
"""

# EX09.     python의 swap
"""
a = 10
b = 20
b, a = a, b
print(a, b)
"""

# EX10.     a++
"""
a = 100
# a++       # python에서 작동X -> 아래 두가지 방법 사용하기
a = a + 1  # 방법1
a += 1  # 방법2
print(a)
"""

# EX11.     고유 식별 번호
"""
a = 10
b = 20
c = 10
print(id(a), id(b), id(c))  # a와 b의 고유번호 BUT c(a의 고유번호와 같음) 경우, 같은 id를 가진다 (only in Python)

a = '호랑이'
b = '코끼리'
c = '호랑이'
print(id(a), id(b), id(c))
"""

# EX12.     16진수 표현
"""
a = 0x20
print(a)

b = 0o0376  # 0x or 0o를 사용하여 표현한다
print(b)
"""

# EX13.     복소수의 연산이 가능
"""
a = 1 + 2j
b = 3 + 4j  # language j 복소수 i 의미
print(a + b)
"""

# EX14.     나누기
"""
a = 10
b = 3
print(a / b, a % b, a // b)  # 몫, 나머지, 몫의 정수
"""

# EX15.      pow 제곱
"""
print(2 ** 8)
"""

# EX16.      소수점 round
"""
print(round(3.1415, 2))  # 소수점 두자리까지 반올림/버림
print(round(3.1455, 2))
"""

# EX17.      배열
"""
str = "Apple"
print(str[4])

str = "무궁화꽃이피었습니다"
print(str[4])
print(str[-2])  # 끝에서 2번째 (only in Python) -> 끝에서부턴 -1부터 시작
print(str[2:5])  # 2번째 글자부터 5번째 글자 앞까지 (인덱스 번호 2번부터 (5-2)개 가져온다고 생각하면 쉬움)
print(str[:5])  # 앞에 숫자 생략되면 무조건 처음부터
print(str[5:])  # 인덱스 번호 5번부터 끝까지
print(str)
print(str[:])  # 처음부터 끝까지 다 출력

str = "Apple"
a = str[0]
print(a)
b = str[:2]
print(b)
# print(str[0] = "B")         #error -> Bpple로 바꾸고 싶다고 이렇게 쓰는건 불가능
c = 'B' + str[1:]  # Bpple로 바꾸고 싶으면 이렇게
print(c)
"""

# EX18.      값을 대입하는 3가지 방법 => %, {자릿수}, s = ''
"""
#1) % 사용
print('호%d 랑%s 이' % (10, '집'))
print('호%d 랑이' % 10)            # 짝이 1개일때는 () 생략 가능

#2) {} 사용       {0번째-10}{1번째-호랑이}
print('무궁화{0}꽃이{1} 피었습니다'.format(10, '호랑이'))

print('%s 집에 %d가고 싶다' % ('나중에', 82))
print('{0} {1} 자고 싶다'.format('지금', 82))

#3) 함수 = '' 사용
s = '무궁화{0} 꽃이 {1}피었습니다'
print(s)        # {} 포함한 결과값
s.format(10, '호랑이')
print(s)                                       # 무궁화{0} 꽃이 {1}피었습니다 와 같은 결과값
t = s.format(10, '호랑이')                      # 함수를 이용한 변경
print(t)
s = s.format(10, '호랑이')                      # s 자체를 변경
print(s)
"""

# EX19.      워드 카운트; 문자열의 길이와 갯수, 인덱스 번호
"""
s = '무궁화꽃이 피었습니다'
print(len(s))       # 문자열의 갯수

s = '무궁화꽃이무궁화피었무궁화습니다무궁화'
print(s.count('무궁화'))       # 찾고자하는 문자열의 갯수
print('무궁화꽃이무궁화피었무궁화습니다무궁화'.count('무궁화'))       # 직접 대입도 가능

s = '무궁화꽃이꽃이피었습니다'
print(s.find('피었'))     # 찾고자하는 문자열의 인덱스(번째수) 번호 / find 검색 실패 경우 항상 -1 return
"""

# EX20.      문자열 출력 결과 대소문자 + 대치
"""
s = 'Apple'         # 문자열을 관리하는 객체 생성
t = s + 'Orange'
s = s + 'Banana'
print(t, s)

print(s.lower())    # 출력 결과를 소문자로
print(s)            # s 자체는 변경X

t = s.lower()       # 원본데이터는 변경시키지 않는 것이 원칙 return 값으로
print(t)

print(s.upper())    # 출력 결과를 대문자로
print(s.replace('Banana', 'Orange'))        # 바나나 -> 오렌지
print(s)            # s값이 변경이 안됐다는 것은 대치결과를 return 값으로 받아준 것

print(s.replace('banana', 'Orange'))        # 대소문자 구분하여 찾아야한다
"""

# EX21.      list 크기, 관리, 분리
"""
s = '무궁화 꽃이 피었습니다'
print(s.split())        # 스페이스를 기준값으로 글자를 분리
                        # ['무궁화', '꽃이', '피었습니다'] -> 대괄호 list type(1개 이상의 결과값)
t = s.split()
print(t)        # s 자체의 변경 X

print(len(t))                                 # 배열의 크기 리스트의 크기
print(t[0], t[1]*3, t[2])                     # 문자열 자체가 배열로 되어있기떄문에 배열로 관리 + 반복횟수 출력
s = '무궁화:꽃:이:피었:습:니다'
print(s.split(':'))                           # default 는 스페이스며 :를대상으로 구분 (특글자 중심으로 분리)
"""

# EX22.      산술연산
"""
print(16 + 3)
print(16 - 3)
print(16 * 3)
print(16 / 3)  # 몫
print(16//3)   # 몫 (정수)
print(16 % 3)
print(16 ** 3)
"""

# EX23.      관계(비교)연산
"""
print(3 > 2)
print(3 < 2)
print(3 >= 3)
print(3 <= 3)
print(3 == 3)
print(3 != 3)
"""

# EX24.      논리연산
"""
# AND Java && 거짓이 하나라도 있으면 무조건 거짓
print("-----------")
print(False and False)
print(False and True)
print(True and False)
print(True and True)

# OR Java || 참이 하나라도 있으면 무조건 참
print("-----------")
print(False or False)
print(False or True)
print(True or False)
print(True or True)

# 부정 연산 Java ! 안에있는 결과를 변경시키지 않고 사용하려는때 사용
print("-----------")
print(not(3 > 2))

print(3 + 2 > 4 and 6 < 2 * 4)                  # 해석이 항상 산술 연산 부처
print(5 > 4 and 6 < 8)                          # 산술이 먼저 일어나기에 위의 문제와 동격
print(True and True)

print(((3 + 2) > 4) and (6 < (2 * 4)))          # 위의 모든 출력이 이러한 논리
"""

# EX25.      랜덤 데이터 random과 randInt (모사데이터; 시뮬레이션
"""
from random import *        # -> random number로 부터 제공되는 ranndom 모듈을 사용 (randint, random, unifom, randrange)

print(random())             #0.0부터 1.0 사이의 값을 랜덤하게 출력
                            
print(randint(3,5))         # 3 <= x <= 5  -> 3과 5를 포함, 3~5 사이의 수를 랜덤 출력
print(randint(10,100))      # 10 - 100 사이의 수를 랜덤하게 출력

                                # 숫자 2부터 시작해서 20 사이에 있는 숫자를 3씩 증가를 했을떄
print(randrange(2, 20, 3))      # 2 5 8 11 14 17 20 중 한개를 랜덤하게 뽑아준다
"""

# EX26.      입력값 java print scanner
"""
a = input("입력하세요: ")        
print(a, type(a))
print('----------------------')

a = int(input('점수를 입력하세요: '))       # 숫자를 입력 받기를 원할 때(앞에 int 붙여주기)
if a >= 90:
    print('a')
elif a >=80 :
    print('b')
elif a >= 70 :
    print('c')
elif a >= 60 :
    print('d')
else :
    print('e')

# string -> int 로 출력하는 방법 3가지
a = input("입력하세요: "))
#방법01.
print(int(a)*int(a))
#방법02.
print(int(a)*2)
#방법03. 정석 코드
a = int(input('입력: '))
print(type(a), a**2)
"""

# EX27.      제어문(if, while, for, switch)
# if문
"""
#1) if에 (제어문) 열고 닫아도 되지만 정석은 아니다 -> () 생략이 정석
#2) 제어문에 끝에는 :이 붙는다
#3) 조건이 만족할 때의 실행 문장은 tab 처리 (하지 않을 경우 error)

#예제01.
if 3 > 2:
    print(1)
print("-------------------")

if 3 > 4:
    print(1)
else:
    print(2)
print("-------------------")

if 3 > 4:
    print(1)
else:
    print(2)
    
print(3)        # <- 위와의 구분이 없으면 enter를 3번정도 두고 거리를 둔다 (if else 상관없이 출력되는 결과)
print("-------------------")

if 3 > 4:
    print(1)
else:
    print(2)
    print(3)        # else문에 들어가 있는 출력값으로 뜬다

#예제02.
from random import *
a = randint(10, 99)
print(a)

b = a / 10
c = a % 10

if b%2==0 and c%2==0:
    print("탕수육")
elif b%2!=0 and c%2==0:
    print("짜장면")
elif b%2==0 and c%2!=0:
    print("냉면")
else:
    print("우동")
    

#예제03.
if not(''):       # False 취급 하는 경우: False,{},[],(),None(Java 에서는 null),'', not('')
    print("호랑이")
else:
    print("코끼리")

if 10 in [10, 20, 30, 40]:                      # list 목록안에 10이 있으면
    print(10)
else:
    print(19)

s = '무궁화 꽃이 피었습니다'
t = s.split()
print(t)
if '무궁화' in t:
    print('존재')
else:
    print('존재하지 않는다')
"""

# while문
"""
#예제01.
a = 0
while a < 10:
    a += 1
    print(a)
    
print("호랑이")

a = 0
while a < 10:
    a += 1
    if a == 3:
        continue
    if a == 6:
        break
    print(a)
    
print("호랑이")


#예제02.  우박수
num = 23

while True:
    print(num)

    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1

    if num == 1:
        break
    else:
        continue

#예제02 - 1) 우박수 삼항연산자ver.
num = 23

while True:
    print(num)
    num = (num // 2) if (num % 2 == 0) else (num * 3 + 1)     # python에서 삼항연산자

    if num == 1:
        break
    else:
        continue
"""

# for문 들어가기 전에..
"""
print(range(0, 10), type(range(0, 10)))

a = list(range(0, 10))          # 범위: 0 <= x < 10
print(a)

print(list(range(5, 10)))       # 시작, 끝 범위 주지만 그 앞까지만 출력

print(list(range(3, 20, 2)))    # 2씩 증가하는(3, 5, 7, 9, 11, 13, 15, 17, 19)
"""

# for문
"""
for i in [0, 1, 2, 3, 4]:
    print(i)

for i in [0, 1, 2, 3, 4]:   #숫자 관리
    print(i, end=' ')
print()

for i in ['월', '화', '수', '목', '금', '토', '일']:   #문자열 관리
    print(i, end=' ')
print()

for i in ['코알라', '사자', '토끼', '말', '호랑이', '여우', '곰']:
    print(i, end=' ')
print()

for i in range(0, 10):      #for문 정석 코드
    print(i, end=' ')
print()


#예제01. 구구단 5단 출력하기
print("5단")
for i in range(1, 10):
    print('5 * %d = %d' % (i, 5*i))

#예제02. 원하는 구구단 출력하기
dan = int(input("원하는 단을 입력하세요: "))
for i in range(1, 10):
    print('%d * %d = %d' % (dan, i, dan*i))

#예제03. 1에서 10까지의 합 구하기
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

#예제04.  이중for문 - 사각형 형태로 출력하기
for i in range(0, 3):
    for j in range(0, 4):
        print("[%d %d]" % (i, j), end="")
    print()

k = 0
for i in range(3):
    for j in range(4):
        print("%02d " % k , end='')
        k += 1
    print()
"""

# EX28.
"""
 print(chr(65))
 print(ord('B'))
"""

# EX29. list타입
"""
a = [10, 20, 30, 40]        # 대괄호 열고 닫고
print(a)

b = ['고양이', '코알라', '사자']
print(b)

c = [10, '사자', 3.14, True]      # 서로 다른 타입도 list 항목에 설정 가능
print(c)

#CRUD 중 R
a = [10, 20, 30, 40]
print(a)                            # 출력방법01.
print(a[0], a[1], a[2], a[3])       # 출력방법02.
# print(a[4])     # error(out of bound) 쓸 수 없는 번호
for i in a:                         # 출력방법03.
    print(i, end=' ')
print()
for i in [10, 20, 30, 40]:          # 출력방법04.
    print(i, end=' ')
print()
for value in a:                     # 출력방법05. (value/data/item)
    print(value, end=' ')
print()

#CRUD 중 U
a = [10, 20, 30, 40]
a[0] = 50                           # 업데이트 방법01.
print(a)
print(id(a[0]), id(a[1]))           # 기존에 들어있던 data 삭제하고 새로운 data 추가하는 논리 적용
a[0] = 60
print(id(a[0]), id(a[1]))

#CRUD 중 D
del(a[0])                           # 삭제 방법01.
print(a)

#길이 구하기 - length, size
print(len(a))
"""

# EX30. List 더 나아가서..
"""
#01번.
a = [10, '토끼', [20, '코끼리', [30, '독수리']]]     # list 안에 list
print(a)
print(a[2][1])
print(a[2][2][1])   # 결과값: 독수리

#02번.
a = 'apple'
b = ['a', 'p', 'p', 'l', 'e']
print(a)
print(b)
print(a[0])
print(b[0])
#a[0] = 'B'      #불가능 - 문자열은 직접적으로 업데이트 시킬 수 없음
b[0] = 'B'       #리스트는 가능함
print(b)

#03번.
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:3])       # 인덱스 번호 1번후터 (3-1)개 가져오세요

a[1:3] = ['F', 'G']     # 업데이트 방법02. 2개가 삭제되고 그 자리에 업데이트됨
print(a)

a[1:3] = ['H', 'J', 'K', 'L', 'P']       # 안에 있는 데이터 삭제하고 넣고 싶은만큼 넣는 것 가능함
print(a)

#04번.
a = ['a', 'b', 'c', 'd', 'e']

a[1:3] = []     # 삭제는 시켰는데 추가되는게 없음
print(a)

del(a[1:3])    # 삭제 방법02. 순수하게 삭제만 시키고 싶을 때
print(a)

#05번.
a = ['orange']

a.append('F')       # 맨 뒤에 추가됨
print(a)
a.append(10)
print(a)

a.insert(0, 10)     # 특정 위치(0)에 data(10)를 넣고 싶다
print(a)

#06번.
a = ['o', 'r', 'a', 'n', 'g', 'e']
a.pop()             # 안에 값 없이 단독으로 쓰이면 맨 뒤에 있는 데이터 버림
print(a)
a.pop(3)            # 숫자 위치에 맞는 데이터 버림
print(a)

#07번
a = ['o', 'r', 'a', 'n', 'r', 'e']

a.remove('r')       # 안에 들어있는 문자열을 검색해서 삭제 -> 두 개일 경우 앞에 하나만 삭제
print(a)

#a.remove('f')       # (error) 검색에 실패한 경우 -> (Exception)예외 처리한다

try:                          # 예외가 발생했을 경우 계속해서 프로그램 진행하겠다
    a.remove('f')
except:
    print('예외가 발생하였습니다.')
    pass
print('코알라')

#08번
a = ['o', 'r', 'a', 'n', 'g', 'e']

b = a.index('o')       # 안에 문자열 위치 찾기
print(a)
print(b)


#09번    sort, reverse

a = ['o', 'r', 'a', 'n', 'g', 'e']

a.sort()        # 안에 들어있는 문자열을 알파벳 순서대로 배열 -> 이런 종류의 함수들은 비용이 많이 든다
print(a)

a.reverse()     # 역순 정렬
print(a)


a = ['a', 'c', 'e', 'f', 'd', 'b']

a.sort()
print(a)

a.reverse()         # 역순 정렬이 아님 -> 나온 결과를 반대로 출력
print(a)

a.sort(reverse=True)
print(a)


#10번.   append / extend
a = [1, 2, 3]
a.append(4)
print(a)

a = [1, 2, 3]
a.append([4, 5])
print(a)        # 결과: a = [1, 2, 3, [4, 5]]

a = [1, 2, 3]
a.extend([4])
print(a)        # 결과: a = [1, 2, 3, 4]

a = [1, 2, 3]
a.extend([4, 5, 6])     # 아예 합성시킴
print(a)        # 결과: a = [1, 2, 3, 4, 5, 6]

a = [1, 2, 3]
a = a + [4, 5, 6]       # + 이용해서 extend시킴
print(a)
"""

# EX31) 튜플(Tuple)
"""
a = ()      #튜플
b = []      #리스트
print(a, b, type(a), type(b))

a = (10,)
print(type(a))
b = 10,
print(type(b))      # 괄호 생략 가능
c = 10
d = (10)
print(type(c), type(d))     # 콤마를 붙였는지 아닌지에 따라 tuple/int로 나뉨

e = (10, 20, 30,)           # 요소가 2개 이상일 때
print(type(e))
f = 10, 20, 30              # 괄호 생략 가능
print(type(f))

a = (10, 20, 30)
b, c, d = a
print(a, b, c, d)       # a가 갖고있는 요소를 b, c, d에 한개씩 줌

a = [10, 20, 30]
b, c, d = a
print(a, b, c, d)       # 리스트도 가능함

a = 10
b = 'icecream'
a, b = b, a
print(a, b)

a = [10, 20, 30]
b = tuple(a)            # 리스트 자료형을 튜플 자료형으로 바꿔주는 함수, 리턴값(b)이 있음
print(type(a))
print(type(b))

a = (10,) + (20, 30)        # 튜플과 튜플이 +로 연결됨
print(a)
print((10,) + (20, 30))     # 출력코드에 바로 넣는 것도 가능
"""

# 크기 비교
"""
a = (1, 2, 3)
b = (1, 3)
print(a == b)
print(a <= b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a < b)
print(a <= b)

a = [1, 2, 3]
b = [1, 2, 3, 4]
print(a < b)
print(a <= b)

a = [1, 2, 3]
b = [1, 2, 3, -4]
print(a < b)
print(a <= b)

a = [1, 2, 3, 4, 5]
b = [1, 3, 4]
print(a < b)
print(a <= b)

print('tiger' < 'tager')    # 알파벳 순으로 크기 비교
print('tiger' < 'tzger')

a = [1, 2, 3]
b = [1, 2, 3, 4, 5]
"""

# update
"""
for i in a:
    print(i)

a = (10, 20, 30)
b = [10, 20, 30]
print(a[0])     # 튜플이라고 () 사용하는거 아님
b[0] = 20       # 리스트에서는 가능
a[0] = 20       # 튜플에서는 불가능 -> error 뜨는게 맞음
"""

# EX32) 튜플, 리스트
"""
a = [10, '호랑이', [20, 30, (40, '코끼리', [50, 60], [70, 80])]]      # 안에 얼마든지 넣을 수 있음
print(a)

a = []
b = list()      # 리스트 함수(괄호 조심)
print(type(a), type(b))

c = ()
d = tuple()     # 튜플 함수
print(type(c), type(d))

e = [10, 20]
f = list('apple')
print(e)
print(f)
"""

# EX33) 리스트 복습
"""
a = []
b = tuple(a)
c = list(b)
print(type(a), type(b), type(c))

a = '호 랑 이'
b = a.split(' ')        # 공백 기준으로 분할 -> 리스트로 저장됨
print(b)

# offset: 기준점으로부터 상대적으로 떨어진 거리
a = [10, 20, 30]
print(a[0], a[1], a[2])      # 음수는 끝에서부터 해석(-1이면 뒤에서 첫번째)
print(a[-1], a[-2], a[-3])
"""

# EX34) 딕셔너리
"""
# a = {k:v, k:v, k:v, ...}
# k:key 값, 고유의 key 값
# v:value 값, key에 대응하는 값
# 배열처럼 순서를 나타내는 index 값 없음

a = {}
print(type(a))

a = {1:10, 2:20, 5:40}
print(a)

a = {10:'호랑이', 20:'코끼리', 30:'독수리'}      # 문자열 가능
print(a)

a = {1:10, 2:20, 2:30, 5:40}        # 중복된 데이터 -> 가장 최근에 들어온 값으로 갱신됨
print(a)

a = {1:[10, 20], 2:[30, 40], 3:[50, 60]}        # 리스트 가능
print(a)

a = {1:(10, 20), 2:(30, 40), 3:(50, 60)}        # 튜플 가능
print(a)

a = {1:30, 2:'코알라', 3:[5, 10], 4:(6, 17), 5:{6:10, 7:99}}       # 모두 들어갈 수 있음
print(a)

a = {'호랑이':10, '코끼리':15, '독수리':20}      # key 값 문자열로도 가능함
print(a)

a = {100:10, '코끼리':15, '독수리':20}      # key 값 섞어서 사용 가능하지만 가급적 하나로 통일해서 쓰자
print(a)

a = {'name':'홍길동', 'age':20, 'salary':300}     # json
print(a)

a = {'name':'이순신', 'age':20, 'salary':300}      # 갱신 방법, 없는 항목(salary)은 새로 추가함
print(a)

print(a['name'])        # name 값 뽑아내기

a['height'] = 180       # 새로운 항목 추가
print(a)
"""

# CRUD
"""
a = {}
a['name'] = '황원정'       # C
a['age'] = 24
print(a)

b = a['name']             # R
print(b, a['age'], a)

a['name'] = '이순신'       # U
a['age'] = 100
print(a)

del(a['name'])            # D
print(a)

# del a['name']           # D (괄호 생략 가능)
# print(a)
"""

# EX35) a.keys() /  a.items()  /  a.values()
"""
a = {'name':'이순신', 'age':20, 'salary':300}
b = a['name']
c = a.get('name')
print(a)
print(b)
print(c)

print(a.keys())          # 사용하고 있는 모든 key 보여줌
for i in a.keys():       # 사용하고 있는 모든 key 보여줌2
    print(i)

for item in a.items():      # key, value 값 모두 보여줌
#   print('호랑이')
    print(item)
    print(type(item))

for item in a.items():      # 각각의 데이터 뽑아내기
    print(item[0])          # item[0] = name, age, salary
    print(item[1])          # item[1] = '이순신', 20, 300

for value in a.values():        # 안에 들었있는 value 값 모두 보여줌
    print(value)
"""

# lol = ['ab',  'cd', 'ef']
# print(dict(lol))
#
# print(len(lol))
#
# first = {'a':'agony', 'b':'bagels'}
# second = {'b':'bagels', 'c':'candy'}
# a = {**first, **second}
# print(a)
# print(first)
#
# third = {'f':'fruit', 'b':"baby"}
# first.update(third)
# print(first)
#
# del(first['a'])
# print(first)
#
# print(len(third))
# third.pop('f')
# print(len(third))
# #third.pop('f')

# EX36)  얕은 복사 - 메모리 공유
"""
a = [1, 2, 3]
b = a           
print(id(a))    # 같은 id 가짐
print(id(b))

a[0] = 4        # a를 변경시키면 b도 같이 변경됨
b[2] = 5        # b를 변경시키면 a도 같이 변경됨
print(a)
print(b)

a.append(99)
print(a)
print(b)
"""

# EX37)  깊은 복사
"""
a = [1, 2, 3]
b = a[:]
print(id(a))    # 다른 id 가짐
print(id(b))

a[0] = 4        # a만 변경
b[2] = 5        # b만 변경
print(a)
print(b)

a.append(99)    # 다른 결과
print(a)
print(b)


# 또 다른 예
# c = 10
# print(id(c))
# c = 20          # 재할당
# print(id(c))    # 그 전 데이터는 삭제하고 재할당 한거라서 id 다름

# import copy
#
# a = {1:100, 2:200, 3:300}
# b = copy.deepcopy(a)
# print(id(a))
# print(id(b))
"""

# EX38)  함수형태
"""
#함수 형태01
def func01():
    print(1)
    print(2)
    print(3)

print(99)
func01()
print(100)
func01()

#함수 형태02
def func02(a):
    print(a)
    print(a*a)

func02(50)
func02(80)

#함수 형태03
def func03():
    print('함수03 call')
    return 100

func03()             # 호출방법01 - return 값은 못 받음
a = func03()         # 호출방법02 - return 값 변수로 받아주는 방법
print(a)
print(func03())      # 호출방법03 - 변수로 안 받고 return 값 받아줌
#print(func01())     # !!!!!!!주의!!!!!!! 이렇게 쓰면 안됨 -> func01은 return 값으로 받을 게 없음
print(func03()*7)    # return 값에 x7한 값 출력

#함수 형태04
def func04(num):
    print('함수04 call', num)
    return (777 + num)

print(100)          # 호출방법01 - return 값 무시
a = func04(100)     # 호출방법02
print(a)    
print(func04(100))  # 호출방법03

#함수 형태05
def func05(a, b, c):
    print('함수05 call')
    sum = a * b + c
    print(sum)
    print(a*a + b*b + c*c)

func05(2, 3, 4)

#함수 형태06
def func06():
    print('함수06 call')
    return;
    print(2)        # 이게 출력될 방법은 없!음! (도달할수 없는 코드 = unreadched code)

func06()

#함수 형태07
def func07(a, b):
    print(a, b)
    print(type(a), type(b))

func07(10, '호랑이')       # 숫자, 문자 상관없이 다 받음

#함수 형태08
# 주의: 맨 끝에서부터 초기화 시켜야 함 (d는 초기화 안하고 c는 초기화 하고는 안됨)
def func08(a, b, c = 10, d = 20):       # 함수 인수 초기값 지정 가능
    print(a, b, c, d)

func08(5, 4)
func08(1, 5, 3)
func08(1, 3, 5, 7)
#func08(5)       # 불가능 -> a, b는 인수 꼭 받아야함

#함수 형태09
def func09(*args):      # 가변 인수 전달
    print('*' * 30)
    for data in args:
        print(data)

func09()
func09(10, 20)
func09(10, 20, '호랑이', 30)

#함수 형태10
def func10(a, b, *args):
    print(a, b)
    for data in args:
        print(data)

func10(10, 20)
func10(10, 20, 30)

#함수 형태11
def func11(a, b, *, color, data):  
    print(a, b, color, data)

func11(1, 2, color = 3, data = 4)

#함수 형태12
def func12(**star):
    print(star)
    for i in star.keys():
        print(i)
    for i in star.items():
        print(i)
    for i in star.values():
        print(i)
    for k, v in star.items():   # key랑 value 따로따로
        print(k, v)

func12(a = 10, b = 20)
"""

# 함수 정리
"""
#01 전달인수 없고 return 없다
def func01():
    print('함수01 호출')

func01()


#02 전달인수 있고 return 없다
def func02(a):
    print('함수02 호출')
    print(a)

func02(50)


#03 전달인수 없고 return 있다
def func03():
    print('함수03 호출')
    return 100

print(func03())     # 호출방법01
result = func03()   # 호출방법02
print(result)


#04 전달인수 있고 return 있다
def func04(b):
    print('함수04 호출')
    return (500 + b)

print(func04(5))        # 호출방법01
result2 = func04(30)    # 호출방법02
print(result2)
"""

# EX39)  CLASS + 기본함수 4개
"""
#class 01번
class Apple:
    def __init__(self):      # 생성자 (self는 dafault값)
        print("생성자 call")

a = Apple()     # 객체 생성


#class 02번
class Apple:
    def __init__(self):
        # print("class02 생성자 call")
        pass        # 출력코드 안 쓸거니까 그냥 넘어가라

a = Apple()


#class 03번
class Apple:
    def __init__(self):
        pass

    def func01(self):
        print("func01 호출")
        print(1)

a = Apple()     # 객체 생성
a.func01()      # 함수 호출


#class 04번
class Apple:
    def __init__(self):
        pass

    def func02(self, a):
        print("func02 호출")
        print(a*a)

a = Apple()
a.func02(10)        # self에 대한 인수는 지정 안해줘도 됨


#class 05번
class Apple:
    def __init__(self):
        pass

    def func03(self):
        print("func03 호출")
        return 100

a = Apple()             # 객체 생성
a.func03()              # 호출방법01 -> return값 없이
print(a.func03())       # 호출방법02 -> return 값이랑 같이
result = a.func03()     # 호출방법03 -> return 값이랑 같이
print(result)


#class 06번
class Apple:
    def __init__(self):
        pass

    def func04(self, a):    # self 꼭 넣어줘야 함 (변수입력은 따로 안해줘도 됨)
        print("func04 호출")
        return 100+a

a = Apple()

a.func04(50)            # 호출방법01 -> return값 없이
print(a.func04(50))     # 호출방법02 -> return 값이랑 같이
result = a.func04(50)   # 호출방법03 -> return 값이랑 같이
print(result)
"""

# EX40)
"""
class Apple:
    def __init__(self, num):
        print(id(self))     # self는 생성된 객체 -> java에서는 this문법
        pass

a = Apple(20)
print(id(a))


# Field
class Apple:
    num = 10
    def __init__(self):
        pass

a = Apple()
print(a.num)


# Field 자동 생성
class Apple:
    def __init__(self, num):
        self.num = num    # 필드 선언 안해도 필드 자동 생성 : 동적
    def func(self, num):    # 필드 선언을 안했기에 바로 num 을 사용 할 수 없다.
        print(num)

a = Apple(20)
print(a.num)
a.func(30)


# 동적(Dynamic) : 필요할 때 만들어 쓰는 것
# 정적(Static) : 처음부터 만들어져 있는 것
class Apple:
    a1 = 10     # 필드 생성
    def __init__(self, a2):
        self.a2 = a2
    def func(self):
        a3 = 30     # a3는 지역변수
        print(self.a1)      # 정적
        print(self.a2)      # 동적
        print(a3)           # 지역변수(잠시 쓰고 버림)

a = Apple(20)
a.func()
"""

# EX41)  상속
"""
class Apple:
    def __init__(self):
        pass

    def f1(self):
        print(1)
    def f3(self):
        print("부모3")

class Orange(Apple):    #상속 끝
    def f2(self):
        print(2)
    def f3(self):
        print("자식3")
    def f4(self):
        print(4)
        self.f2()   # 자기꺼 f2 부르고 싶을 때
        self.f3()   # 자기꺼 f3 부르고 싶을 때
        super().f3()  # 부모의 f3 부르고 싶을 때

a = Orange()
a.f1()
a.f2()
a.f3()  # 자기꺼에 없으면 부모꺼 찾아봄
a.f4()

print(Apple.mro())  # 클래스의 특성 보여줌
print(Orange.mro())

a1 = Apple()    # 파이썬에서 업캐스팅의 개념은 없음 (받는 놈이 타입이 없어서)
"""

# EX42)
"""
class Cat:
    def __init__(self):
        pass
    def cry(self):
        print("야옹")

class Dog:
    def __init__(self):
        pass
    def cry(self):
        print("멍멍")

class Snake:
    def __init__(self):
        pass
    def cry(self):
        print("안운다")

a1 = Cat()
a2 = Dog()
a3 = Snake()
# 사용방법1
a1.cry()
a2.cry()
a3.cry()

a4 = [Dog(), Cat(), Snake()]
print(a4)
# 사용방법2
for obj in a4:
    obj.cry()
"""

# EX43)
"""
class Apple:
    def f1(self):
        print(1)


def f2(a):
    print(2)
    a.f1()

f2(Apple())
"""

# EX44)  다형성
"""
class Zoo:
    def __init__(self, animal):
        self.animal = animal

    def cry(self):
        self.animal.cry()

class Dog:
    def cry(self):
        print("멍멍")

class Cat:
    def cry(self):
        print("야옹")


t1 = Zoo(Dog())
t1.cry()

t2 = Zoo(Cat())
t2.cry()
"""

# EX45) 예외처리
"""
# a = 4/0
# print(1)

#try-except문
try:
    print(0)
    a = 4/0
except:
    print(1)

print(2)


#except Exception as e: 어떤 Exception이 떴는지 알고싶을 때
try:
    print(0)
    a = 4/0
except Exception as e:
    print(e)


#try-except-finally문
try:
    print(0)
    a = 4/0
except Exception as e:
    print(e)
finally:    #exception이 발생하던지말던지 나오는 코드
    print(30)


#실사용 예제
a = [10, 20, 30]
b = a.index(30)
print(b)

try:
    c = a.index(100)
except Exception as e:
    print(e)

print("오류가 있긴 하지만 정상적으로 진행되고 있음")
"""

# EX46)  파일 입출력
"""
# 기본 형태
file = open("sample.txt", "w", encoding="UTF-8")

file.write("코끼리")

file.close
"""

# for i in range(5):
#     print(i)
#
# for i in range(2, 7):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)

# EX47) 파일 Write
"""
# 호랑이 다섯번 출력
# file = open("sample.txt", "w", encoding="UTF-8")
#
# for i in range(5):
#     file.write("호랑이")
#
# file.close


# 0,1,2,3,4 출력 -> 숫자를 문자열로 바꿔서 출력해야 됨
# file = open("sample.txt", "w", encoding="UTF-8")
#
# for i in range(5):
#     file.write(str(i))
#
# file.close


# 호랑이0 호랑이1 호랑이2 ... 줄 바꿔서 출력
# file = open("sample.txt", "w", encoding="UTF-8")
#
# for i in range(5):
#     file.write("호랑이" + str(i) + '\n')
#
# file.close


# 다른 방법으로 파일 입력(with-as문: file.close 자동으로 일어남) -> file.close 지우기
# with open("sample.txt", "w", encoding="UTF-8") as file:
# 
#     for i in range(3):
#         file.write("호랑이" + str(i) + '\n')
"""

# EX48) 파일 Read
"""
file = open("sample.txt", "r", encoding="UTF-8")

data = file.readline()
print(data)

if data:
    print(10)                   # 데이터 읽음


data = file.readline()
print(data)

if data:
    print(20)                   # 데이터 못 읽음 

file.close



if "호랑이":
    print(1)

if "":
    print(2)
"""

# EX49) 파일 Read (여러줄 읽기)
"""
# 방법1
# file = open("sample.txt", "r", encoding="UTF-8")
#
# while True:
#     data = file.readline()
#     print(data)
#
#     if not data:    # 읽은 data가 null이라면 탈출해라
#         break
#
# file.close

# 방법2
# file = open("sample.txt", "r", encoding="UTF-8")
#
# data = file.readlines()
# print(data)
#
# file.close
#
# for i in data:
#     print(i, end='')

# 방법3
file = open("sample.txt", "r", encoding="UTF-8")

file.close

data = file.read()
print(data)     # 문자열 타입으로 읽음
"""

# EX50)  공백 없이 출력
"""
# 방법1
a = ['호랑이0\n', '호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4']
a[0] = a[0].replace('\n', '')

for i in a:
    print(i)

#방법2
for i in range(len(a)):
    a[i] = a[i].replace('\n', '')
    print(a[i])

#방법3
a = ['호랑이0\n', '호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4']
print(a)

for index, value in enumerate(a):
    print(index, value)
    a[index] = value.replace('\n', '')
print(a)
"""

# EX51)  Import
"""
# 예제1. 잘 쓰진 않지만 기본적인 형태
import Tiger

Tiger.f1()

# 예제2.  Tiger 적지 않고도 함수 부를 수 있음
from Tiger import *

f1()

# 예제3.  Tiger라고 다 적을 필요없이 t만 적고 불러오면 됨
# import A as b   # A를 쓸건데 별칭으로 b라고 하겠다 (기본 형식)
import Tiger as t

t.f1()
"""
"""
print(__name__)

import Tiger as t

t.f1()
t.f2()  # 이 함수가 실행되고 있는 위치 보여줌: Tiger
"""

"""
import Tiger as t

if __name__ == "__main__":
    print(1)    # __name__ = "__main__"이니까 1 출력

t.f1()  # Tiger import 했으니까, tiger f1에 있던 코드 불러옴
"""

# 기본꼴
"""
def f1():
    print(100)

def main():         # entry point
    print(1)
    f1()

if __name__ == "__main__":
        main()
"""

# EX52) 딕셔너리
"""
apple = {"n1":"호랑이", "n2":"코끼리", "n3":"독수리"}
print(apple["n1"])
print(apple["n2"])
print(apple["n3"])


Orange = {10:20, 20:"조랑말", 30:True}
print(Orange[10], Orange[20])


Kiwi = {"이름":"홍길동",
        "나이":20,
        "특기":["독서", "무술", "프로그래밍"],
        "가족":{"아버지":"아빠", "어머니":"엄마"}}
print(Kiwi["이름"], Kiwi["나이"])
print(Kiwi["특기"], Kiwi["특기"][2])
print(Kiwi["가족"]["어머니"])


data = {
    "response":{
        "body":{
            "items":[{
                    "addr":1234,
                    "name":"홍길동"
                },
                "득템"
            ]
        },
        "page":100
    },
    "header":{
        "result":200,
        "msg":"OK"
    }
}
print(data["response"]["body"]["items"][0]["addr"])
print(data["response"]["body"]["items"][0]["name"])
print(data["response"]["body"]["items"][1])
print(data["response"]["page"])
print(data["header"]["result"])
print(data["header"]["msg"])
"""

"""
apple = {"n1":"호랑이", "n2":"코끼리", "n3":"독수리"}
Orange = {10:20, 20:"조랑말", 30:True}

print(apple["n1"])      # n1 value 값 출력방법1
print(apple.get("n1"))  # 출력방법2

print(Orange[10])
print(Orange.get(10))


try:
    apple["n4"]   # Exception 발생
except:
    print("검색하지 못했습니다.")


num = apple.get("n4") # Exception 발생 X
print(num)

if num == None:
    print("검색하지 못했습니다")
"""

# a = [10, 20, 30, 40]
# print(sum(a))
#
# print(sum([1, 2, 3, 4]))
#
# a = sum([3, 4, 5, 6])
# print(a)


# def f1(a):
#     return a > 0        # 0보다 큰 값만 return
#
#
# # print(filter(f1, [-2, -1, 0, 1, 2]))    -> 오류
# print(list(filter(f1, [-2, -1, 0, 1, 2])))     # -> 결과를 리스트로 변환시켜서 오류 안남


# EX53)  함수 참조
# 예제1
"""
def f1():
    print(1)


f1()        # 호출 방법1

a = f1      # 호출 방법2 -> 함수 참조
a()         # 이렇게도 호출 가능
"""

# 예제2
"""
def f2():
    print(2)


def f3(tt):
    tt()
    print(3)


f3(f2)
"""

# 예제3
"""
def f4():
    return 999

def f5(tt):
    print(tt)


f5(999)

f5(f4())    # f4에서 return 된 값을 출력
"""

# EX54)  SWITCH
"""
def f1(num):
    t = {10:"호랑이", 20:"독수리", 30:"앵무새"}
    return t[num]


print(f1(10))
"""


#EX55)  Comprehension
"""
# a = [10, 20, 30]
# print(a*2)      # 두번 반복

# 반복문과 조건문을 이용하여 list를 생성하는 것을 'comprehension' 이라고 한다
a = [i for i in range(5)]  # list 안에서 반복문 (for 뒤에 i 값이 맨 앞 i로 나옴)
print(a)

a = [i * 3 for i in range(5)]
print(a)

a = [10, 20, 30, 40]
b = [i * 3 for i in a]  # a에서 하나씩 꺼내서 x3해서 출력
print(b)

a = [10, 20, 30, 40]
b = [i + 2 for i in a if i > 25]  # a에서 하나씩 꺼내서 25보다 큰 숫자들에 한해서 +2해서 출력
print(b)

############################################################

print(dir({}))  # 딕셔너리와 관련된 함수 출력됨
print(dir([]))  # 리스트와 관련된 함수 출력됨
print(dir(()))  # 튜플과 관련된 함수 출력됨

# 복습
a = [10, 20, 30, 40]

a.insert(3, 99)  # 3번 자리에 99 추가
print(a)

###################################################

a = [10, 20, 30, 40]

a.append("호랑이")
a.append(100)  # 맨 끝에 추가1
print(a)

a.insert(len(a), 99)  # 맨 끝에 추가2
print(a)

###################################################

a = [10, 20, 30, 40]

print(a + [50, 60])  # 확장1

a.extend([50, 60])  # 확장2
print(a)

###################################################

a = [10, 20, 30, 40]
b = a
c = a.copy()

print(a, b, c)  # 생긴건 똑같음
print(id(a), id(b), id(c))  # copy를 하면 완전히 새로운 객체가 생성됨 (a의 id랑 c의 id랑 다름)

a[0] = 99
print(a[0], b[0], c[0])  # id가 같으니까 서로 같은 객체 참조 -> a, b 둘이 같이 바뀜
# but, c는 다름

###################################################

a = [10, 20, 30, 40]
a.clear()
print(a)

###################################################

a = [10, 20, 30, 40, 10]
a.remove(10)
print(a)
# 삭제하려고 하는데 없으면 exception 발생함
# 중복된 데이터 있으면 첫 데이터만 삭제됨

###################################################

a = [10, 20, 30, 40]

print(a[2])
del (a[2])
print(a)

###################################################

a = [10, 20, 30, 40]
b = a.pop(2)  # 인덱스 번호로 하나를 꺼내서 그 수를 삭제시킨다
print(b)  # return 값 있어서 꺼낸값 출력해서 볼 수 있음
print(a)  # 꺼낸 값 삭제됨

###################################################

# filter 함수 이용해서 6을 제외한 리스트 만들기
a = [0, 3, 6, 9, 0, 3, 6, 9]


def f1(num):
    return num != 6


print(list(filter(f1, a)))
"""


#EX56)  내장함수
"""
a = 10
print(id(a), type(a))

# 절댓값
print(abs(-10))

a = [10, 20, 30, 40]
for i in a:
    print(i)

# 리스트의 index와 value 값 같이 얻고 싶을 때
for key, value in enumerate(a):         # key 대신 index라고 적기도 함
    print(key, value)

# eval 함수
a = "print(10+20)"      # 문자열
eval(a)     # 안에 있는 문자열을 코드로 해석해서 결과 출력
print(a)

# min, max 함수
print(min([3, 5, 7]))
print(max([3, 4, 5, 6]))
a = [1, 2, 3, 4]
print(min(a))
print(max(a))

# bin 함수: 2진수로 출력해주는 함수
print(bin(100))
print(bin(200))
# oct 함수: 8진수로 나타내주는 함수
print(oct(100))
# hex 함수: 16진수로 나타내주는 함수
print(hex(100))

# 문자열을 숫자로
a = int("123")
print(type(a))
# 숫자를 문자열로
a = str(123)
print(type(a))
# 문자열을 리스트로
a = list("APPLE")
print(a, type(a))
a = list(range(5))
print(a)

# divmod: 몫과 나머지
a = divmod(7, 3)
print(a)        # 결과를 튜플로 보여줌 -> (2, 1)=(몫, 나머지)
print(type(a))
print(a[0], a[1])
for i in a:
    print(i)

# all, any
print(True & True & True)           # 모두 참이여야 참
print(all([True, True, True]))      # and 개념 = all 개념
print(False | False | True)         # 하나라도 참이면 참
print(any([False, False, True]))    # or 개념 = any 개념

# sort: 정렬함수
a = [9, 6, 3, 7, 2]
a.sort()        # a 값 갱신
print(a)

a = [9, 6, 3, 7, 2]
b = sorted(a)   # a 자체의 값은 변경되지 않음, 원본 그대로 냅둠
print(a)        
print(b)
"""


#EX57)  Time
"""
import time
a = time.localtime(time.time())
print(a)
print(a.tm_year, "년")
print(a.tm_mon, "월")
print(a.tm_mday, "일")
print(a.tm_hour, "시")
print(a.tm_min, "분")
print(a.tm_sec, "초")

b = ["월", "화", "수", "목", "금", "토", "일"]
print(b[a.tm_wday], "요일")


import datetime
print(datetime.datetime.now())


for i in range(5):
    print(i)
    time.sleep(1)       # 1초씩 텀을 두고 출력
"""


#EX58)  Lambda
# 일반 함수
def f1():
    print(1)

f1()


# 람다 함수
f2 = lambda: print(2)
f2()
print(type(f2))


f3 = lambda x: print(x)
f3(3)


f4 = lambda x, y: print(x+y)
print(10, 20)


f5 = lambda: 99         # return 안써줌
print(f5())


f6 = lambda x, y: x+y
print(f6(2, 4))

#########################

def f1(ff):
    ff()

def f2():
    print("호랑이")

f1(f2)

f1 (lambda: print("코끼리"))


def f3(ff):
    ff(10, 20)

f3(lambda x, y: print(x+y))


# 필터 함수
def f4(a):
    return a > 0


a = filter(f4, [-2, -1, 0, 1, 2])
print(list(a))

# 람다함수 + 필터함수
a = filter(lambda a: a > 0, [-2, -1, 0, 1, 2])
print(list(a))


















































