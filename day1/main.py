def sort_list(num):
    return sorted(num)
    # left = 0
    # right = len(num) - 1
    # sorted_list = []
    # while left < right:
    #     if num[left] < num[right]:
    #         sorted_list.append(num[left])
    #         left += 1
    #     else:
    #         sorted_list.append(num[right])
    #         right -= 1
    # return sorted_list
    

def find_diff(list1, list2):
    foo = 0
    result = 0
    while foo < len(list1):
        result += abs(list1[foo] - list2[foo])
        foo += 1  
    return result

list1, list2 = [], []

with open ("data.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1_sort = sort_list(list1)
list2_sort = sort_list(list2)


difference = find_diff(list1_sort, list2_sort)

print(difference)


