#taking input
n = int(input())

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j ** (i - 1), end=" ")

    print() # for space