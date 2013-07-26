# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [i for i in L if i%num != 0]



## Problem 2
def myLists(L): return [[i for i in range(1,x+1)] for x in L]



## Problem 3
def myFunctionComposition(f, g): return {k:g[f[k]] for k in f.keys() } 


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5+3j 
complex_addition_b = 1j
complex_addition_c = -1+.001j
complex_addition_d = .001+9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    result = 0
    for x in L:
        result += x
    return result



## Problem 7
def myProduct(L):
    result = 1
    for x in L:
        result *= x
    return result



## Problem 8
def myMin(L):
    result = L[0]
    for i in range(1, len(L)):
        if result > L[i]:
            result = L[i]
    return result



## Problem 9
def myConcat(L):
    s = ""
    for x in L:
        s += x
    return s



## Problem 10
def myUnion(L):
    result = set()
    for s in L:
        result |= s
    return result
