a = int(input())
b = int(input())

print(a * int(b % 10)) #일의 자리
print(a * int(b // 10 % 10)) #십의 자리
print(a * int(b // 100)) #백의 자리
print(a * b)