# The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well!

# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
# ============================================

def reverseArray(nums):
    for i in range(len(nums)//2):
        nums[i], nums[-1-i] = nums[-1-i], nums[i]
    return nums

if __name__ == '__main__':
    nums = [1,2,3,4,5,8]
    reversedArr = reverseArray(nums)
    print(f"Reversed Array is: {reversedArr}")