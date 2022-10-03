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
output = []
for amount in input:
    status = billcollector(amount)
    output.append(status)

print('input')
print(input)
print('output')
print(output)
input = [5,5,10,20,5]
output =[]
for amount in input:
    status = billcollector(amount)
    output.append(status)
print('input')
print(input)
print('output')
print(output)
