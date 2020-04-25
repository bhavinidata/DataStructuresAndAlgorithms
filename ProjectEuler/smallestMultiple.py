# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import time
def isPrime(num: int)->bool:
    primeChk = True
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num%2 == 0:
        return False
    else:
        # number 3, 5, 7 won't come in this loop
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num%i == 0:
                primeChk = False
    return primeChk
        

def smallestMultiple(a:int, b:int) -> int:
    prime = []
    primePower = []
    # loop through the numbers, 
    # find all the prime numbers between both the input numbers.
    for i in range(a+1, b+1):
        # if prime found then add it to a prime array
        if isPrime(i):
            prime.append(i)
    
    # loop through all the prime numbers,
    # take the power and get the highest number that is below higher input number.
    for p in prime:
        x=0
        pow_value = 0
        while (pow_value < b):
            x = x+1
            pow_value = p **x
        primePower.append(p **(x-1))
    print(primePower)
    product = 1
    for pp in primePower:
        product *= pp
    return product

if __name__ == '__main__':
    t1 = time.time()
    result = smallestMultiple(1,20)
    print(f"Smallest multiple is: {result}")
    t2 = time.time()
    print(f"Time taken: {t2-t1}")
    

        






