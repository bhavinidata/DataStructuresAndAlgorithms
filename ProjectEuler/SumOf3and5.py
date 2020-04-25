# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sumOf3and5(n:int) -> int:
    totSum = 0
    # for i in range(n):
    #     if (i%3 == 0 or i%5 == 0):
    #         totSum = totSum+i
    totSum = sum([i for i in range(1000) if (i%3 == 0 or i%5 == 0)])
    return totSum

if __name__ == '__main__':
    result = sumOf3and5(1000)
    print(result)