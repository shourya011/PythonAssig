#taking input
n = int(input())

while n >= 10:
    n = sum(int(d) for d in str(n))

print(n)