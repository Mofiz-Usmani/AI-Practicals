import random

def hill_climb(f, x, steps=100):
    for _ in range(steps):
        n = x + random.choice([-1,1])     # neighbor
        if f(n) > f(x): x = n             # move if better
    return x

# Example: maximize f(x) = -(x-3)**2 + 9 (peak at x=3)
f = lambda x: -(x-3)**2 + 9
print("Best:", hill_climb(f, random.randint(-10,10)))
