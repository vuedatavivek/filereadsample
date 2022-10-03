price = 5
cashinhand = 0
def billcollector(amount):
    global cashinhand
    if(amount == price):
        cashinhand = cashinhand + price
        return True
    if(amount > price):
        balance = amount - price
        if(cashinhand >= balance):
            cashinhand = cashinhand - balance
            return True        
    return False

input = [5,5,5,10,15]
print('***input 1***')
for amount in input:
    print("amount %d:"%(amount))
    print("cashinhand b %d"%(cashinhand))
    print(billcollector(amount))
    print("cashinhand a %d"%(cashinhand))
print('***input 2***')
input = [5,5,10,20,5]
for amount in input:
    print("amount %d:"%(amount))
    print("cashinhand b %d"%(cashinhand))
    print(billcollector(amount))
    print("cashinhand a %d"%(cashinhand))
