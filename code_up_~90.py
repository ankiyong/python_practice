#82
n=int(input())
while n != 30:
    for n in range(1,n+1):
        if n%3==0:
            print('짝!')
            if (n%3)//10 >= 0:
                print('짝짝!')
        else:
            print(n)


