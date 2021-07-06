alphabet = input().lower()  # 소문자로 입력 받음 >> 개수 세기위해서 zza
a_list = list(set(alphabet))  # 중복 제거 후 리스트 형태로 변경 z a

a_count = []  # 각 알바벳별 중복횟수 입력 리스트 2 1

for i in a_list:
    count = alphabet.count(i)  # 중복 알파벳 세기
    a_count.append(count)  # 중복횟수 리스트에 반복해서 추가

if a_count.count(max(a_count)) >= 2:  # 가장 중복 많은 알파벳 두개일 때 "?" 출력
    print("?")
else:
    print((a_list[(a_count.index(max(a_count)))]).upper())
    # print(a_list.index(a_count.index((max(a_count)))))  # 가장 많은 알파벳 하나일 때 그 알파벳 출력
