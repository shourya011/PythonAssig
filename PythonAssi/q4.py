#taking input
n = input()

even = 0
odd = 0

for digit in n:
    if int(digit) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even, ", Odd:", odd)