input = int(input("Enter an integer: "))
results_list = []
for number in range (1, input+1):
    result = float(input/number)
    if result == int(result):
        results_list.append(result)
if len(results_list) != 2:
    print(f"{input} is not a prime number.")
else: print(f"{input} is a prime number.")