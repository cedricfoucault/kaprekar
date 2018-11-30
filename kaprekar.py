MIN = 0
MAX = 10000

def is_kaprekar(n):
    """Returns True if n is a Kaprekar number"""
    n2 = n ** 2
    ndecimals = len(str(n2))
    for i in range(0, ndecimals):
        left = n2 // (10 ** i)
        right = n2 % (10 ** i)
        if left + right == n:
            return True
    return False    
        
print("Nombres de Kaprekar de {:d} à {:d} :".format(MIN, MAX))
for n in range(MIN, MAX + 1):
    if is_kaprekar(n):
        print(n)
    