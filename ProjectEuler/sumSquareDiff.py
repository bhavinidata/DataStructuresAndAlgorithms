# The sum of the squares of the first ten natural numbers is,

# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time
def sumSquareDiff(num: int)-> int:
    sum = 0
    sumSquare = 0
    for i in range (num +1):
        sum +=i
        sumSquare += i**2
    print(sum)
    print(sumSquare)
    difference = sum**2 - sumSquare
    return difference

if __name__ == '__main__':
    t1 = time.time()
    result = sumSquareDiff(100)
    print(f"Answer is: {result}")
    t2 = time.time()
    print(f"Time taken: {t2-t1}")