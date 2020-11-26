# 단순한 선 그래프 (plot창)
# 1) 기본형 - 뺄 수 있는거 다 뺌
# from matplotlib import pyplot as plt
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.3, 14958.2]
# plt.plot(years, gdp)
# plt.show()

# 2) 추가
# from matplotlib import pyplot as plt
#
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.3, 14958.2]
#
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')      # plt.plot(x축, y축) -> 기본형, 뒤에는 추가 안해도 됨
#
# plt.title("Nominal GDP")
# plt.ylabel("Billions of $")
#
# plt.show()





# 막대 그래프 (bar창)
# from matplotlib import pyplot as plt
#
# movies = ["Tiger", "Lion", "Rabbit", "Elephant", "Dog"]
# num_oscars = [5, 10, 3, 7, 1]
#
# plt.bar(range(len(movies)), num_oscars)     # plt.bar(x좌표, y좌표)
#
# # plt.title("My Favorite Movies")
# # plt.ylabel("# of Academy Awards")
#
# plt.xticks(range(len(movies)), movies)      # x축 각 막대의 중앙에 영화 제목을 레이블로 추가
#
# plt.show()





# 히스토그램
# from matplotlib import pyplot as plt
# from collections import Counter
#
# grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
#
# # print(grades[0]//10)
# # print((grades[0]//10)*10)
# histogram = Counter(min((grade // 10) * 10, 90) for grade in grades)      # 10점 단위로 그룹화 -> 100점을 90점대 그룹에 포함시킬려고 min값 넣음
#
# plt.bar([x+5 for x in histogram.keys()],        # 각 막대를 오른쪽으로 5만큼 옮김
#         histogram.values(),                     # 각 막대의 높이 정해줌
#         10,                                     # 너비는 10
#         edgecolor=(0, 0, 0))                    # 각 막대의 테두리는 검은색으로
# """
# # plt.bar([85, 95, 75, 65, 5],        # 각 막대를 오른쪽으로 5만큼 옮김
# #         histogram.values(),         # 각 막대의 높이 정해줌
# #         10)
#
#
# # plt.bar([85, 95, 75, 65, 5],        # 각 막대를 오른쪽으로 5만큼 옮김
# #         histogram.values(),         # 각 막대의 높이 정해줌
# #         12)
# """
#
# plt.axis([-5, 105, 0, 5])       # x축은 -5부터 105, y축은 0부터 5
#
# plt.xticks([10*i for i in range(11)])       # x축의 레이블은 0, 10, ..., 100
# # plt.xlabel("Decile")
# # plt.ylabel("# of Students")
# # plt.title("Distribution of Exam 1 Grades")
# plt.show()





# 선그래프
# from matplotlib import pyplot as plt
#
# variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
# bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
# total_error = [x+y for x, y in zip(variance, bias_squared)]
# # xs = [i for _, i in enumerate(variance)]
# xs = [i for i, _ in enumerate(variance)]
#
# # 한 차트에 여러 개의 선을 그리기 위해 plt.plot 을 여러번 호출할 수 있음
# plt.plot(xs, variance, 'g-', label='variance')          # 실선
# plt.plot(xs, bias_squared, 'r-.', label='bias^2')       # 일점쇄선
# plt.plot(xs, total_error, 'b:', label='total error')    # 점선
#
# plt.legend(loc=9)       # legend: 범례, loc=9: 가운데에 위치
# # plt.xlabel("model complexity")
# # plt.xticks([])        # x축 레이블 없음
# # plt.title("The Bias-Variance Tradeoff")
# plt.show()





# 산점도 (scatter)
# 1)
# from matplotlib import pyplot as plt
#
# friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 130,105, 145, 190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#
# plt.scatter(friends, minutes)
#
# for label, friend_count, minute_count in zip(labels, friends, minutes):
#         plt.annotate(label,
#                      xy=(friend_count, minute_count),   # 화살표가 가르키는 점의 위치
#                      xytext=(5, -5),                    # 레이블블이 출력될 위치
#                      textcoords='offset points')
#
# plt.show()

# 2)
# from matplotlib import pyplot as plt
# test_1_grades = [99, 90, 85, 97, 80]
# test_2_grades = [100, 85, 60, 90, 70]
#
# plt.axis("equal")               # (자동으로 축의 범위 설정하냐 마냐 결정하는 명령어)
#                                 # -> 이 명령어 추가하면 공정한 비교 가능, 추가 안하면 공정한 비교 불가능
# plt.scatter(test_1_grades, test_2_grades)
# plt.show()




















































































