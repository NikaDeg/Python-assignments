import random
N = int(input("How many points to generate: "))
n = 0
rounds = 0
while rounds <= N:
    x_random = random.uniform(-1.0,1.0)
    y_random = random.uniform(-1.0,1.0)
    if x_random**2 + y_random**2 < 1.0:
        n = n + 1
    rounds = rounds + 1
pi = float((4 * n) / N)
print(f"Approximation of pi: {pi:.4f}")