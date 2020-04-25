# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# ===========================================

# value of any side of the triangle must be less than the semiperimeter
import math
import time   
def pythagoreanTriplet (num: int) -> int:
    semiperimeter = num // 2
    product = 1
    for i in range(1, semiperimeter):
        for j in range(1, semiperimeter):
            k = math.sqrt(i**2 + j**2)
            if(k%1 == 0 and i + j + k == num):
                product = i*j*int(k)
                print(f"A: {i}, B: {j}, C: {k}")
                return product

if __name__ == '__main__':
    limitNumber = 1000
    t1 = time.time()
    result = pythagoreanTriplet(limitNumber)
    print(f"Product of three sides of tringle: {result}")
    t2 = time.time()
    print(f"Time taken: {t2-t1}")
            