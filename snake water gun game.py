import time
k = 0
a = 0  # computer
b = 0  # player
t = 0
while k < 10:
    lst = [1, 2, 3]  # 1 = Snake, 2 = water, 3 = gun
    c = int(random.choice(lst))
    # print(c)

    k = k + 1
    print("value for k", k)

    print("Press 1 For Snake")
    print("Press 2 For Water")
    print("Press 3 For Gun")
    c1 = int(input())

    if c == 1 and c1 == 2:
        print("computer win")
        a = a + 1
    elif c == 1 and c1 == 3:
        print("you win")
        b = b + 1
    elif c == 2 and c1 == 1:
        print("you win")
        b = b + 1
    elif c == 2 and c1 == 3:
        print("computer win")
        a = a + 1
    elif c == 3 and c1 == 1:
        print("computer win")
        a = a + 1
    elif c == 3 and c1 == 2:
        print("you win")
        b = b + 1
    else:
        print("ohh it's TYE Play Again")
        t = t + 1

print("\n\n")
print("Computer Win", a, "Time")
print("You Win", b, "Time")
print(t, "Time Your Game Tye")
print("\n")
lt = time.asctime(time.localtime(time.time()))
print(lt)
if a > b:
    print("Computer won the Game by", a-b, "Points")
elif a == b:
    print("Tye Between You and Computer ply again")
else:
    print("You won the Game by", b-a, "points")
