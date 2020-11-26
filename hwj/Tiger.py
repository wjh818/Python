# def f1():
#     print(1)
#     print(1234567)
#
#
# def f2():
#     print(__name__)
#
#
# if __name__ == "__main__":
#     print(1)
#
#
# #기본꼴
# def main():
#     print(1)
#
#
# if __name__ == "__main__":
#     main()




class Apple:
    def f1(self):
        print(1)
        return self

    def f2(self, func):
        print(2)
        num = func(100)               # f3(group)인수
        return num * 3


def f3(group):
    print(group)                # 100 출력
    return group * 2



a = Apple()
b = a.f1().f2(f3)               # 함수 번호 1번에 return이 반드시 있어야한다
print(b)


























class Apple:
    def groupby(self):
        print(1)
        return self

    def apply(self, func):
        print(2)
        num = func(100)  # f3(group)인수
        return num * 3


def add_prop(group):
    print(group)  # 100 출력
    return group * 2


names = Apple()
b = names.groupby().apply(add_prop)  # 함수 번호 1번에 return이 반드시 있어야한다
print(b)