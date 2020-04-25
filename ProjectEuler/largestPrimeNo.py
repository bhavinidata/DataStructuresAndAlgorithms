# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math
def largestPrime(n: int) -> int:
    
    #find the factor of input number n
    for i in range(math.floor(math.sqrt(n)),1, -1):
        
        if n%i == 0:
            noPrimeFactor = False
            print(f"factor: {i}")
            #i is factor of n. 
            #let's find if it is prime number or not
            for d in range(math.floor(math.sqrt(i)),1,-1):
                if i%d == 0:
                    noPrimeFactor = True
            if noPrimeFactor == False:
                return(i)

if __name__ == '__main__':
    result = largestPrime(600851475143)
    print(f"Largest prime factor is: {result}")