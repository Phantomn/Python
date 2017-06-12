marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number+=1
    if mark >= 60:
        print("%d student is pass"%number)
    else:
        print("%d student is not pass"%number)

