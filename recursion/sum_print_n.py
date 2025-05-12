# Print 1 to n numbers.

def one_to_n(n):

    if n==1:
        print(1)
        return
    else:
        
        one_to_n(n-1)
        print(n)

def n_to_one(n):
    if n==1:
        print(1)
        return
    else:
        print(n)
        one_to_n(n-1)
        

def sum_of_n(n):


    if n == 1:
        return 1
    else:

        return n+sum_of_n(n-1)

print(sum_of_n(5))