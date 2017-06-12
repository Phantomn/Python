# _*_ coding: utf-8 _*_
# coffee.py


coffee = 10
while True:
    money = int(input("Input money : "))
    if money == 300:
        print("give coffee")
        coffee = coffee -1
    elif money > 300:
        print("give you left money %d and coffee"%(money-300))
        coffee-=1
    else:
        print("money back and not give coffee")
        print("left coffee is %d"%coffee)
    if not coffee:
        print("coffee is nothing.. sales over")
        break
