
# Formula f(n) = n % 10 + f(n/10)

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "The number has to be a positive integer only"
    if n == 0:
        print(n)
        return 0
    print(f"Value of n {n}")    
    return int(n%10) + sumOfDigits(int(n/10))

print(f"Sum of numbers {sumOfDigits(11111)}")    


