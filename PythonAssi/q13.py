#taking input
n = int(input())

s = sum(int(d) for d in str(n))

if n % s == 0:
    print("Yes")

else:
    print("No")
