# reduced space complexity

def factorial(a):
    if a == 0:
        return 1
    
    mul = 1

    
    for i in range(1, a+1):
        mul = i * mul
        
    return mul
    

a = int(input('Enter number: '))

print(f"factorial of ({a}) = {factorial(a)}")
