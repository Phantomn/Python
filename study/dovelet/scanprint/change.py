money = 1000

bill = input()


change = money - bill
hun = change / 100
change %= 100
fif = change / 50
change %= 50
ten = change / 10

print hun, fif, ten