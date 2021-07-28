n = int(input())
rand = map(int,input().split())
student = []
for i in rand:
    student.append(i)
    student.reverse()
print(student)
