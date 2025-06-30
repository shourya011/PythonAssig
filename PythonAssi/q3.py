#taking input
n = int(input())

a = n // 10
b = n % 10

if a * b + a + b == n:
    print(True)

else:
    print(False)