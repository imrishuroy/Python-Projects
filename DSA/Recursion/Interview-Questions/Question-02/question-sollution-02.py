
# x^n = n * x^n-1

def power(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent , "The exponent must me positive integer only"
    if exponent == 0:
        return 1
    if exponent == 1:
        return base    
    print(f"Base: {base}, Exponent: {exponent}")    
    return base * power(base, exponent-1)

print(power(-1, 2))