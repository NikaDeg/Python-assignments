def filter_even_numbers(integers):
    even_integers = []
    for i in integers:
        if i % 2 == 0:
            even_integers.append(i)
    return even_integers

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = filter_even_numbers(original_list)
print (f"Original list: {original_list}\nList with even numbers only: {new_list}")