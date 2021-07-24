#82
# n=int(input())
# for i in range(1,n+1):
#      if i%10==3 or i%10==6 or i%10==9:
#          print('X',end=" ")
#          if i//11 ==3 or i//11 ==6 or i//11 ==9:
#              print('X', end=" ")
#      else:
#          print(i, end=" ")
# print( )

#83
# r,g,b = map(int,input().split())
# for i in range(0,r):
#     for j in range(0, g):
#         for k in range(0, b):
#             print(i,j,k)
# print(r*g*b)

#84
# h,b,c,s = map(int,input().split())
# print('%.1f MB' % (h*s*c*b / 8 / 1024 / 1024))

#85
# w,h,b = map(int,input().split())
# print('%.1f MB' % (w*h*b/8/102/1024))

#86
# n = 0
# summ = 0
# a = int(input())
# while summ < a:
#     n+=1
#     summ +=n
# print(summ)

#87
# n = int(input())
# a = 0
# while a != n:
#     a+=1
#     if a % 3 == 0:
#         continue
#     else:
#         print(a)


#87-1
# n = int(input())
# for i in range(1,n+1):
#     if i % 3==0:
#         continue
#     else:
#         print(i)

#88
# a,d,n = map(int,input().split())
# count = 0
# data = []
# while count < n-1:
#     a+=d
#     data.append(a)
#     count += 1
# print(data[-1])

#89
# a,r,n = map(int,input().split())
# count = 0
# data = []
# while count < n-1:
#     a*=r
#     data.append(a)
#     count += 1
# print(data[-1])

#90
a,m,d,n = map(int,input().split())
count = 0
data = []
while count < n-1:
    a = a*m+d
    data.append(a)
    count += 1
print(data[-1])


