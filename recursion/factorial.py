# Function to provide n factorial.

def factorial(n):

    if n <=2:
        return n
    else:
        return n*factorial(n-1)

print(factorial(3))