import re

def decoder_func(code):
    mul = re.findall(r"mul\(\d+,\d+\)", code)
    nums = []
    result = []
    for pairs in mul:
        remove_mul = re.findall(r"\d+,\d+", pairs)
        nums.append(remove_mul)
    for index, value in enumerate (nums):
        result.append([int (num) for num in value[0].split(",")])

    return result

def code_solver(decode):
    result = 0
    for index, value in enumerate ( decode ):
        result += value[0] * value[1]
    return result

code = open("data.txt", "r")

decode = decoder_func(code.read())



# print(decode)
print(code_solver(decode))