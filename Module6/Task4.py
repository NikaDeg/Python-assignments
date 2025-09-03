def sum_of_list(integers):
    sum = 0
    for i in integers:
        i = int(i)
        sum = sum + i
    return sum

all_numbers = [9, 2, 4]
result = sum_of_list(all_numbers)
print(f"The sum of the numbers in the list is: {result}")
