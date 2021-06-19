# 최대공약수와 최소공배수
# 정수론 / 유클리드 호제법
# 반복문으로 풀기

a, b = map(int, input().split())

if a < b:
    a, b = b, a
num1 = a
num2 = b
while num1 % num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder
GCD = num2
LCM = GCD * (a // GCD) * (b // GCD)
print(GCD)
print(LCM)



# 함수로 푼다면?
# a, b = map(int, input().split())
#
# if a < b:
#     a, b = b, a
#
#
# def gcd(a, b):
#     while b != 0:
#         c = a % b
#         a = b
#         b = c
#     return a
#
#
# def lcm(a, b):
#     GCD = gcd(a, b)
#     return (a * b) // GCD
#
#
# print(gcd(a, b))
# print(lcm(a, b))
