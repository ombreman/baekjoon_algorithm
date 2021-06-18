N = int(input())

five = N // 5  # 5킬로 봉지수
three = N % 5 // 3  # 3킬로 봉지수
r = -1  # 최종 봉지수

while five >= 0:  # 뺄 5킬로 봉지수가 더이상 없다면 바로 통과
    if 5 * five + 3 * three == N:  # 몫이 0이라면
        r = five + three  # r 값 수정
        break  # 멈춰!!!
    else:  # 몫이 0이 아니라면
        five -= 1  # 5킬로 봉지수 -1
        three = (N - 5 * five) // 3  # 3킬로 봉지수 수정

print(r)  # 총 봉지수 최종 출력
