#taking input
n = input()

if all(n[i] < n[i+1] for i in range(len(n)-1)):
    print("Yes")

else:
    print("No")
