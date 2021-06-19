# 최대공약수와 최소공배수
# 정수론 / 유클리드 호제법
# 반복문으로 풀기

a, b = map(int, input().split())  # 10,000 이하의 자연수 두 개

if a < b:
    a, b = b, a
num1 = a
num2 = b
while num1 % num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder
GCM = num2
LCM = GCM * (a // GCM) * (b // GCM)
print(GCM)
print(LCM)
