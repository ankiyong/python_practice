#92
# n = int(input())
# rand = map(int,input().split())
# student = [0 for _ in range(23)]
#
# for i in rand:
#     student[i-1]+=1
# print(*student)

#93
# n = int(input())
# rand = list(map(int,input().split()))
#rand.reverse()
#print(*rand)

#94
# n = int(input())
# k = list(map(int,input().split()))
# print(min(k))

#97
# shape = [[0 for _ in range(19)]for _ in range(19)]
# n = int(input())
# for _ in range(n):
#     x , y = map(lambda num : int(num)-1,input().split())
#     shape[x][y]=1
# for s in shape:
#     print(*s)

#98
# baduk = [[0 for _ in range(19)]for _ in range(19)]
# n = int(input())
# for _ in range(n):
#     x , y = map(lambda num : int(num)-1, input().split())
#     for i in range(19):
#         baduk[x][i] = 1 if baduk == 0 else 1
#         baduk[i][y] = 1 if baduk == 0 else 1
# for s in baduk:
#    print(*s)

#99
