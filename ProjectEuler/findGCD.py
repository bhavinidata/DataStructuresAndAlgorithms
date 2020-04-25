# find GCD from given array.

# arr = [2,4,6,8]
# gcd = 2

def findGCDofArray(arr) -> int:
    gcd = getGCD(arr[0], arr[1])
    for i in range(len(arr)):
        gcd = getGCD(gcd,arr[i])
    return gcd

def getGCD(numA:int, numB:int) -> int:
    while(numB):
        numA, numB = numB, numA%numB
    return numA

if __name__ == '__main__':
    arr = [14,56,7,28]
    result = findGCDofArray(arr)
    print(f"Greatest common divisible number is: {result}")