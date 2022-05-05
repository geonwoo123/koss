#Q1
#for문 사용
A = int(input())
B = int(input())
for i in range(1,B+1):
    if A*i<B+1:
        print(A*i)
    else:
        print("조건에 맞지않다.")

#while문 사용
A = int(input())
B = int(input())
x = 1
while A*x<=B:
    print(A*x)
    x += 1

#Q2

list = [1,3,2,4,5,5,7]
print(list)
print(sum(list))
print(max(list))
print(min(list))
print(sum(list)/len(list))


#Q3

x = int(input("년도"))
y = int(input("월"))
z = int(input("일"))
day = 0
for i in range(1, x):
    if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
        day += 366
    else:
        day += 365
for j in range(1, y):
    if j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12:
        day += 31
    elif j == 2:
        if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
            day += 29
        else:
            day += 28
    else:
        day += 30
day += z
if day % 7 == 0:
    print("일요일")
elif day % 7 == 1:
    print("월요일")
elif day % 7 == 2:
    print("화요일")
elif day % 7 == 3:
    print("수요일")
elif day % 7 == 4:
    print("목요일")
elif day % 7 == 5:
    print("금요일")
elif day % 7 == 6:
    print("토요일")