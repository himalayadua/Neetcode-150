
def factorial(a):
    if a == 0:
        return 1
    
    cache = [0] * (a+1)
    cache[0] = 1

    
    for i in range(1, a+1):
        cache[i] = i * cache[i-1]
        
    return cache[i]
    

a = int(input('Enter number: '))

print(f"factorial of ({a}) = {factorial(a)}")
