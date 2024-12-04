def safety_count(reports ):
    count = 0

    for list_index, lists in enumerate(reports):

        increase_res = all(i < j for i, j in zip(lists, lists[1:]))
        decrease_res = all(i > j for i, j in zip(lists, lists[1:]))

        valid_differences = all(1 <= abs(lists[i] - lists[i + 1]) <= 3 for i in range(len(lists) - 1))

        if (increase_res or decrease_res) and valid_differences:
                count += 1

        print("List", list_index, "completed")

    return count 

# Read File and create lists for each line in data file
reports = [] 

with open ("data.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.rstrip().split())))

x = safety_count(reports)

print(x)