numberStr = input("Enter a number: ")
all_numbers = []
while numberStr != "":
    all_numbers.append(float(numberStr))
    numberStr = input("Enter a number: ")
all_numbers.sort(reverse=True)
print("The greatest numbers in descending order:")
actual_range = min(len(all_numbers), 5)
for i in range(actual_range):
    elem = all_numbers[i]
    print (f"{elem:.1f}")