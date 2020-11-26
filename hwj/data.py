users = [
    {"id": 0, "name": "호랑이0"},
    {"id": 1, "name": "호랑이1"},
    {"id": 2, "name": "호랑이2"},
    {"id": 3, "name": "호랑이3"},
    {"id": 4, "name": "호랑이4"},
    {"id": 5, "name": "호랑이5"},
    {"id": 6, "name": "호랑이6"},
    {"id": 7, "name": "호랑이7"},
    {"id": 8, "name": "호랑이8"},
    {"id": 9, "name": "호랑이9"}
]

# print(len(users))

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]




# 사용자별로 비어 있는 친구 목록 리스트를 지정하여 딕셔너리를 초기화
friendships = {user["id"]: [] for user in users}
# print(friendships)




# 각 숫자가 누구랑 친구인지
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

print(friendships)


# 각 숫자가 누구랑 친구인지 -> 보기 편하게
for item in friendships.items():
    print(item)



# user들의 연결 수 구하는 함수
def number_of_friends(user):
    # user의 친구는 몇 명일까?
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


# sum 예시
""" 
# a = sum([10, 20, 30])
# print(a)
# 
# a = (i for i in range(5))
# print(type(a))      # generator 타입
# 
# b = sum(a)
# print(b)
# 
# # sum(리스트), sum(제너레이터)    -> 둘 다 사용 가능
"""
# for문 사용해서 총 연결 수 구하기
total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)


# 평균 연결 수 구하기
num_uers = len(users)
avg_connections = total_connections / num_uers
print(num_uers)
print(avg_connections)


# (user_id, number_of_friends)로 구성된 리스트 생성
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)    # 정렬 안된 결과값


# 생성한 리스트를 정렬하기
num_friends_by_id.sort(                                 # 정렬해보자
    key=lambda id_and_friends: id_and_friends[1],       # num_friends_by_id를 num_friends 기준으로
    reverse=True)                                       # reverse니까 제일 큰 숫자부터 제일 작은 숫자순으로
print(num_friends_by_id)    # 역순 정렬 결과값 (친구가 많은 순으로 나열됨)
# sort 예시
"""
a = [
    ("호랑이0", 7, 9),
    ("호랑이1", 6, 6),
    ("호랑이2", 4, 3),
    ("호랑이3", 9, 7)
]

a.sort(key=lambda k: k[1])      # a를 k[1](a의 1번 인덱스 값) 기준으로 정렬
print(a)
"""




# 이중 for문
"""
for i in range(3):
    for j in range(4):
        print([i, j], end=' ')
    print()
    
   
    
a = [(i, j)
     for i in range(3)
     for j in range(4)]

print(a)



a = [(i, j)
     for i in [0, 1, 2]
     for j in [0, 1, 2, 3]]

print(a)



a = [(i, j)
     for i in [7, 8, 9]
     for j in [4, 5, 6, 7]]

print(a)
"""
# Counter: 각각의 개수 세어주는 함수
"""
from collections import Counter

a = Counter([10, 20, 30])
print(a)

a = ["호랑이", "호랑이", "코끼리", "호랑이", "코끼리", "독수리", "호랑이"]
b = Counter(a)
print(b)        

c = [10, 20, 30, 10, 20, 10]
d = Counter(c)
print(d)
"""
from collections import Counter
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friends_id in friendships[user_id]
        for foaf_id in friendships[friends_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

for i in range(len(users)):
    print(friends_of_friends(users[i]))





# 책 이해 도움
"""
a = [i for i in [0, 1, 2, 3, 4, 99, 100]
     if i%2 == 0]
print(a)



print(15 in [10, 20, 30])
print(10 not in [10, 20, 30])
"""




# 책 내용 하기 전에...
"""
data = [
    (0, "호랑이"), (0, "코끼리"), (0, "독수리"),
    (1, "호랑이"), (1, "코끼리"), (2, "호랑이"),
    (3, "코끼리"), (3, "독수리")
]


def f1(a):
    b = [i for i, j in data
            if j == a]
    print(b)

f1("코끼리")               # 코끼리에 관심있는 사람들의 id


# 위에 껄 변형시킴
def f1(a):
    return [i for i, j in data
            if j == a]

print(f1("코끼리"))        # 코끼리에 관심있는 사람들의 id
"""
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientists_who_like(target_interest):

    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


print(data_scientists_who_like("Java"))             # Java에 관심있는 사람들의 id




# defaultdict 사용법
"""
from collections import defaultdict

wc = {}
a = ["사과", "바나나", "바나나", "사과", "바나나"]

wc = defaultdict(int)       # int

for i in a:
    wc[i] += 1

print(wc)






a = defaultdict(list)       # list

a["호랑이"].append(10)
a["호랑이"].append(20)
a["호랑이"].append(30)
a["코끼리"].append(10)
a["코끼리"].append(40)

print(a)              # 각 항목에 관심있는 사람 list로 정리해서 나옴
print(a["호랑이"])     # 호랑이에 관심있는 사람 list로 정리해서 나옴
"""
# 항목별로 관심있는 사람
from collections import defaultdict

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

print(user_ids_by_interest)




# 각 id 별로 관심사
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interests)

print(interests_by_user_id)




def most_common_interests_with(users):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[users[user_id]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != users[user_id]
    )

# print(most_common_interests_with(users[0]))





# 실습 해보기 전...
"""
a = defaultdict(list)

a[1].append(10)
a[2].append(20)
a[3].append(30)
a[1].append(40)
a[2].append(50)
a[3].append(60)


b = {
    i: j
    for i, j in a.items()
}
print(b)


b = {
    i: sum(j)
    for i, j in a.items()
}
print(b)


b = {
    i: sum(j) / len(j)
    for i, j in a.items()
}
print(b)
"""
# 연봉과 경력
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# key = 근속 연수, value = 해당 근속 연수에 대한 연봉 목록
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)


# key = 근속 연수, value = 해당 근속 연수의 평균 연봉
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print(average_salary_by_tenure)




def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# key = 근속 연수 구간, value = 해당 구간에 속하는 사용자들의 연봉
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

print(salary_by_tenure_bucket)



# key = 근속 연수 구간, values = 해당 구간에 속하는 사용자들의 평균 연봉
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print(average_salary_by_bucket)






a = "Tiger Lion"
b = a.lower().split()
print(b)


# words count
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())
print(words_and_counts)









a = 2 + \
    3


a = "무궁화 꽃"
b = "무궁화\t꽃"
print(a)
print(b)


a = [0, 1, 2, 3, 4, 5, 6]
print(a[::2])


x, y = [1, 2]
print(x, y)

_, y = [1, 2]   # y값만 사용하고 싶을 때

a = [3 for _ in range(5)]       # _: i 사용하지 않고 just looping용
print(a)


def f():
    return 1+2, 1-2, 1*2

print(f())



a = {10, 20, 30}
print(type(a))
print(a)

a.add(40)
print(a)

a.add(30)
print(a)



assert 1 + 1 == 2
# assert a + 2 == 2

def f(a):
    return min(a)

# a = [10, 1, 3, 4]
# assert print(f(a)) == 4





# sort/sorted 정렬
from collections import Counter

x = [4, 1, 2, 3]
x.sort()
print(x)

x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
print(x)


word_counts = Counter(x)
print(word_counts)

wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)
print(wc)



# 10이 5번 반복
a = [10 for _ in [1, 1, 1, 1, 1]]
print(a)



# 이중for문
a = [(i, j)
     for i in range(3)
     for j in range(4)]
print(a)

# 위에 이중for문을 사각형 형태로 출력하기
for i in range(3):
    for j in range(4):
        print(a[i*4+j], end=' ')
    print()









class Apple:
    def __init__(self, count = 0):
        self.count = count

    def click(self, num_times = 1):
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


a1 = Apple()
a2 = Apple(10)
a3 = Apple(count = 20)


a1 = Apple()
print(a1.read())
assert a1.read() == 0, "a4 should start with count 0"
a1.click()
a1.click()
print(a1.read())
assert a1.read() == 2, "after two clicks, a4 should have count 2"
a1.reset()
print(a1.read())
assert a1.read() == 0, "after reset, a4 should be back to 0"



class Orange(Apple):
    def reset(self):
        pass


a2 = Orange()
print(a2.read())
assert a2.read() == 0
a2.click()
print(a2.read())
assert a2.read() == 1
a2.reset()
print(a2.read())
assert a2.read() == 1, "reset shouldn't do anything"








# 이터레이터와 제너레이터
def f1():
    yield 10
    yield 20
    yield 30

for i in f1():
    print(i)




def f2(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in f2(10):
    print(i)
    # print(f"i: {i}")




def f3():
    n = 1
    while True:
        yield n
        n += 1

a = f3()
print(a)

# for i in a:
#     print(a)

# b = (i for i in a if i % 2 == 0)
# for i in b:
#     print(b)



a = [1, 2, 3]
for i, v in enumerate(a):
    print(i, v)     # index와 key 값

b = {0:10, 1:20, 2:30}
for i, v in b.items():
    print(i, v)     # 딕셔너리에서 index와 key값 출력







# random
from random import *

print(random())
print(randint(10, 20))
print(randrange(0, 10, 3))      # 3의 배수 중에서 랜덤하게 출력

# seed(10)        # 이걸 쓰면 실행 할 때 마다 같은 랜덤한 수 나옴
for i in range(5):
    print(random())


a = [1, 2, 3, 4, 5]
shuffle(a)          # shuffle -> 안에 들어있는걸 랜덤하게 섞어줌
print(a)
b = choice(a)       # choice -> 랜덤한 항목 하나 선택
print(b)
c = sample(a, 3)    # smaple -> 중복된 데이터 없이 랜덤한 수 뽑기 (a에서 3개 뽑기)
print(c)







# zip
a = [1, 2, 3]
b = [4, 5, 6]
c = [i for i in zip(a, b)]      # 하나씩 짝 지어서 튜플 형태로 출력해줌
print(c)        # [(1, 4), (2, 5), (3, 6)]

d, e = zip(*c)      # *: 묶여있는 것을 다시 풀 때
print(d, e)            # (1, 2, 3) (4, 5, 6)






# 타입 어노테이션
def f1(a: int, b: int) -> int:
    return a + b

print(f1(3, 4))
print(f1("hi", " there"))       # error 나는건 아니지만 가독성을 위해 앞으로 정확하게 써주겠다


# 타입 어노테이션 하는 방법
a: list = []

from typing import List
b: List = []

print(type(a), type(b))

c: List[int] = []
print(type(c))

# d: list[int] = []
# print(type(d))

















