from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Brute force method
        # resultSum = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         result = nums[i] +nums[j]
        #         if result == target:
        #             resultSum.append(i)
        #             resultSum.append(j)
        #             return resultSum

        # get empty dictionary/hashmap
        hash_table = {}
        # Loop through the input list of numbers and index
        for i, num in enumerate(nums):
            # subtract number from target number
            # check if the number is present in has table key
            if (target-num) in hash_table:
                # if it is there then return the value of that key (which is stored as hash_table       value)
                return(hash_table[target-num], i)
                break
            hash_table[num] = i
        return([])

if __name__ == '__main__':
    result =  Solution().twoSum([2, 7, 11, 15], 9)
    print(result)
    result1 =  Solution().twoSum([0, -4, 11, 4], 0)
    print(result1)
    result2 =  Solution().twoSum([5, -4, 11, 4, 10], 6)
    print(result2)
        



