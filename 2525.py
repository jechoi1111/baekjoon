now = input().split()
h = int(now[0])
m = int(now[1])

cook = int(input())

if m + cook >= 60:
    plusHour = (m + cook) // 60
    newHour = h + plusHour
    newMinute = (m + cook) % 60

    if newHour > 24:
        print(str(newHour - 24) + ' ' + str(newMinute))
    elif newHour == 24:
        print(str(0) + ' ' + str(newMinute))
    else:
        print(str(newHour) + ' ' + str(newMinute))

else:
    print(str(h) + ' ' + str(m + cook))
