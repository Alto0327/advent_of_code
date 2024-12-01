def similarity(list1, list2):
    result = 0

    for value in list1:
        count = list2.count(value)
        result += value * count
    
    return result


list1, list2 = [], []

with open ("data.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

similarities = similarity(list1, list2)

print(similarities)