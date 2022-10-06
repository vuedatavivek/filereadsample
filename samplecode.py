import pandas as pd
source = {
    "1": 'a',
    "2": 'b',
    "3": 'c',
    "4": 'a',
    "5": 'a',
    "6": 'd',
    "7": 'e',
    "8": 'b',
    "9": 'c',
}
# output = {'a': [1,4,5], 'b': [2,8], 'c': [3,9], 'd': [6], 'e': [7]}
df = pd.DataFrame(source, index=[1])
df = pd. Index(source)
# df = pd.DataFrame(sour)
output = {}
def getduplicated():
    for key in source:
        value = source[key]
        if(output.get(value) != None):
            output[value].append(key)
        else:
            output[value] = [key]
getduplicated()
print(output)




