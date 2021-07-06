# 자연수 리스트 만들기
natural_numbers = list(range(10001))


def d(num):  # num = 1, 10, 100
    천 = num // 1000  # 천의 자리 0, 0, 0
    백 = num // 100 % 10  # 백의 자리 0, 0, 1
    십 = num // 10 % 10  # 십의 자리 0 , 1, 0
    일 = num % 10  # 일의 자리 1, 0, 0
    return num + 천 + 백 + 십 + 일  # 1, 11, 101


# 낫 셀프넘버 리스트 만들기
not_self_numbers = []
a = d(1)
num = 1
for num in range(10001):
    a = d(num)
    if a < 10000:
        not_self_numbers.append(a)
    num += 1
not_self_numbers.sort()

sorting = list((set(natural_numbers)) - set(not_self_numbers))
(sorting.sort())
(sorting.pop())

i = 0
for i in sorting:
    print(i)
