n = int(input())
set1 = 3
set2 = 5
num1 = n // set2
num2=(n % set2) // set1
if (set2 * num1) + (set1 * num2) != n:
    print(-1)
else:
    print(num1+num2)

