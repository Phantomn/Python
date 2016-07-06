origin, price, fake, change = map(int, raw_input().split())
#40 70 50 20
send_money = price + change # 70 + 20 = 90
real_money = send_money - fake # 90 - 50 = 40
give_money = real_money - change # 40 - 20 = 20
profit_or_loss = origin - give_money # 40 - 20 = 20

print profit_or_loss