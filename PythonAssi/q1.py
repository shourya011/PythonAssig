#taking input
n = int(input())

for i in range(n): #column 
    for j in range(n, i, -1): # rows
        print(j, end="")

    print()
