input_name = input("Enter username: ")
input_passw = input("Enter password: ")
correct_name = "python"
correct_passw = "rules"
attempts = 1
while (input_name != correct_name or input_passw != correct_passw) and attempts != 5:
    attempts = attempts + 1
    print("Incorrect username or password. Please try again.")
    input_name = input("Enter username: ")
    input_passw = input("Enter password: ")
    if attempts == 5:
        print ("Access denied")
if input_name == correct_name and input_passw == correct_passw:
        print("Welcome")
