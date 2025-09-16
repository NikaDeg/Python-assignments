def greet(greeting, times):
    for i in range(times):
        print(greeting + " round: " + str(i+1))
    return

greet( "hello", 2)