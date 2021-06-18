a, b, v = map(int, input().split())  # 세 정수 입력받기
# 정상에 올라간 후에는 미끄러지지 않는다.
day_count = 1  # 정상까지 가는데 필요한 일수
if (v - a) % (a - b) != 0:
    day_count += (v - a) // (a - b) + 1
else:
    day_count += (v - a) // (a - b)

print(day_count)
