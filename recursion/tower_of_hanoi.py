# This is not in leetcode.

# Recursive Python function to solve tower of hanoi


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):

    if n == 0:
        return
    
    else:
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        print(f"Move {n} from {from_rod} to {to_rod} using {aux_rod} ")
        TowerOfHanoi(n-1,aux_rod, to_rod, from_rod)


TowerOfHanoi(3,"A","C","B")







