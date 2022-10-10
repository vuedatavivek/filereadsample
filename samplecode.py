#10-10-2022
def fib_generator(limit):
    a = 0
    b = 1
    output = []
    if limit < 0:
        print("Incorrect input")
    elif limit == 0:
        return [a]
    elif limit == 1:
        return [a,b]
    else:
        output.append(a)
        for i in range(0, limit):            
            c = a + b
            a = b
            b = c
            output.append(a)
        return output
# Driver Program
limit = int(input("Enter the limit\n"))
for i in range(0, limit + 1):
    c = fib_generator(i)
    print(f'{i} ==>', c)


# import math
# import pandas as pd


# myNumber = 3
# print(myNumber)  
# myNumber = -4.5
# print(myNumber)
# print(math.fabs(myNumber))
  
# myNumber ="helloworld"
# print(myNumber)

# myset = set(["Geeks", "For", "Geeks"])
# print(myset)
# student_id = ["S004", "S005", "S003", "S001", "S002"]
# student_name = ["MS Dohni", "Ajith Kumar", "Cristiano Ronaldo", "David Beckham", "Sachin"]
# student_grade = [85, 98, 89, 92, 100]  
# output = []
# for idx, id in enumerate(student_id):
#     stu_obj = {id:{student_name[idx]: student_grade[idx]}}
#     output.append(stu_obj)
# print(output)



# source = {
#     "1": 'a',
#     "2": 'b',
#     "3": 'c',
#     "4": 'a',
#     "5": 'a',
#     "6": 'd',
#     "7": 'e',
#     "8": 'b',
#     "9": 'c',
# }
# # output = {'a': [1,4,5], 'b': [2,8], 'c': [3,9], 'd': [6], 'e': [7]}
# df = pd.DataFrame(source, index=[1])
# df = pd. Index(source)
# # df = pd.DataFrame(sour)
# output = {}
# def getduplicated():
#     for key in source:
#         value = source[key]
#         if(output.get(value) != None):
#             output[value].append(key)
#         else:
#             output[value] = [key]
# getduplicated()
# print(output)




