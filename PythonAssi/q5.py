#taking input
n = int(input())

s = sum(int(d) ** 3 for d in str(n))

if s == n:
    print("Armstrong")

else:
    print("Not Armstrong")