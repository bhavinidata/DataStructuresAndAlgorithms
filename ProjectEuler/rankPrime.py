# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math
def isPrime(num:int) -> bool:
    chkPrime = True
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                chkPrime = False
    return chkPrime

def rankPrime(n: int) -> int:
    count = 0 #count 1 for prime number 2. 2 is first prime number
    num = 0
    while count < n:
        if isPrime(num):
            count += 1
            print(f"prime: {num}")
            curr_Prime = num
        num += 1
    return curr_Prime

if __name__ == '__main__':
    n = 10001
    result = rankPrime(n)
    print(f"{n}th prime number is: {result}")

