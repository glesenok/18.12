a =  int(input('start :'))
b =  int(input('finish :'))

day = 1
while a <= b:
    if a == b:
        break
    a+=a/10
    day+=1
    print(day)
