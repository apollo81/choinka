# monety 5 2 1 0.5 0.2 0.1
# indeksowanie lisy dla 10 zl [ 2,0,0,0,0,0]


coins = [5, 2, 1, 0.5, 0.2, 0.1]
coins_amunts = [0,0,0,0,0,0]

to_pay = 12.5
cash = 20

rest = cash - to_pay
for index, coin in enumerate(coins):
    if coin <= rest:
        quantity = rest // coin
        coins_amunts[index] = quantity
        rest -= quantity * coin
print(coins_amunts)