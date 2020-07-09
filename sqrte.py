

def square_root(n,k):
    xk = 1 #when x=1
    for i in range(k): 
        xk = 1/2 * (xk + n/xk)
    return xk

print(square_root(36, 100))
