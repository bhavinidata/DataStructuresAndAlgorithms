# The problem is that we want to find duplicates in 
# a one-dimensional array of integers in O(N) running time 
# where the integer values are 
# smaller than the length of the array!

# =============================================
# Option:1 
# Brute force method. Take one integer and compare with all the other integer.
# But it will be O(N**2) complexity. So not good.

# Option :2 
# Using has map. If integer is not in has map then add in has map 
# otherwise it is in has map and it is duplicate number.
# it is O(N) complexity but it is not in-place. we can do better here when each integer in array 
# is less than the size of the array.

# Option: 3
# Using absolute values. where we can achieve O(N) time complexity with efficient memory usage(in place)

def findDuplicates(inputArr):
    duplicateNums = []
    for num in inputArr:
        if inputArr[abs(num)]>=0:
            inputArr[abs(num)] = -inputArr[abs(num)]
        else:
            duplicateNums.append(abs(num))
    return duplicateNums

if __name__ == '__main__':
    # items (integer values) in an array are less than the length of the array
    inputArr = [2,5,6,5,0,3,5,2,9,0,6,4,5]
    duplicateNums = findDuplicates(inputArr)
    print(f"duplicate numbers in a given array : {duplicateNums}")
