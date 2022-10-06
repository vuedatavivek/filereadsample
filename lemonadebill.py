price = 5
total_balance = 0
cashinhand = {}

def billcollector(amount):
    global cashinhand
    global total_balance
    if(amount == price):
        if(cashinhand.get(price) != None):
            cashinhand[price] += 1
            total_balance += price
            return True
        else:
            cashinhand[price] = 1
            total_balance = price
            return True
    balance = int(amount - price)
    available_coins = sorted(cashinhand.keys(), reverse=True)
    settled = False
    if(cashinhand.get(balance) != None and cashinhand.get(balance) >= 0):
        cashinhand[balance] -= 1
        balance = 0
        settled = True
    while settled == False:
        for coin in available_coins:
            req_coin_count = int(balance / coin)
            if(req_coin_count > 0 and cashinhand[coin] >= req_coin_count):
                cashinhand[coin] -= req_coin_count
                balance -= (coin * req_coin_count)
                if(balance == 0):
                    settled = True
                    break
        settled = True
    if(balance == 0 ):
        total_balance += price
        if(cashinhand.get(amount) == None):
            cashinhand[amount] = 1
        else:
            cashinhand[amount] += 1
    print(cashinhand)
    print(total_balance)
    return balance == 0

_input = [5,5,5,10,20]
_input = [5,5,10,10,20]
output = []
for amount in _input:
    status = billcollector(amount)
    output.append(status)
#input = [5,10,5]

cus_count = input("Enter no of customers")
print(cus_count)
output = []
for i in cus_count:
    cus_amount = input("Enter amount for cus")
    status = billcollector(int(cus_amount))
    output.append(status)
print(output) 
# input = [5,5,10,20,5]
# output =[]
# for amount in input:
#     status = billcollector(amount)
#     output.append(status)
# print('input')
# print(input)
# print('output')
# print(output)
