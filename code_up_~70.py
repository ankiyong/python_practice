#65
# a,b,c = input().split()
# if int(a) % 2 == 0:
#     print(a)
# if int(b) % 2 == 0:
#     print(b)
# if int(c) % 2 == 0:
#     print(c)

#66
# a,b,c = input().split()
# if int(a) % 2==0:
#     print('even')
# else:
#     print('odd')
# if int(b) % 2==0:
#     print('even')
# else:
#     print('odd')
# if int(c) % 2==0:
#     print('even')
# else:
#     print('odd')

#67

# a = int(input())
#
# if a % 2 ==0 and a < 0:
#     print("A")
# elif a % 2 ==0 and a > 0:
#     print('C')
# elif a % 2 != 0 and a > 0:
#     print('D')
#
# else:
#     print('B')

#68
# score = int(input())
#
# if score >= 90:
#     print('A')
# elif score >= 70:
#     print('B')
# elif score >= 40:
#     print('C')
# else:
#     print('D')

#69
# a = input()
# if a == "A":
#     print("best!!!")
# elif a == "B":
#     print("good!!")
# elif a == "C":
#     print("run!")
# elif a == "D":
#     print("slowly~")
# else:
#     print('what?')

#70
mon = int(input())

if mon == 12 or mon // 3 == 0:
    print('winter')
elif mon // 3 == 1:
    print('spring')
elif mon // 3 == 2:
    print('summer')
else:
    print('fall')
