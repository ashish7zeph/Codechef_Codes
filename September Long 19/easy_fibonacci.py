import math

fib = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]

def Power( n): 
    if (n < 1): 
        return 0
   
    res = 1
    for i in range(n): 
      
        curr = 1 << i 
        if (curr > n): 
             break
        res = curr 
   
    return res 

for _ in range(int(input())):

    n = int(input())
    
    print(fib[(Power(n)-1) % 60])


