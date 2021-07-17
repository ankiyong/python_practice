#71
# n = 1
# while n !=0:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         print(n)
#72
# n = int(input())
# while n != 0:
#     print(n-1)
#     n = n-1

#73


#74
# n = int(input())
# for i in range(0,n+1):
#     print(i)

#77
# n = int(input())
# isum = 0
# for i in range(0,n+1):
#     if i %2==0:
#         isum+=i
# print(isum)

#78
# s = None
# while s != 'q':
#     s = input()
#     print(s)

#79
# isum = 0
# y = 0
# x = int(input())
# while isum <=x:
#     isum+=1
#     print(isum)

#80
n,m = input().split()

for i in range(1,int(n)+1):
    for j in range(1,int(m)+1):
        print(i,j)