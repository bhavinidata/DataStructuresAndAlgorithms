from typing import List
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultSum = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                result = nums[i] +nums[j]
                if result == target:
                    resultSum.append(i)
                    resultSum.append(j)
                    return resultSum

if __name__ == '__main__':
    re =  Solution().twoSum([2, 7, 11, 15], 9)
    print(re)
    re1 =  Solution().twoSum([0, -4, 11, 4], 0)
    print(re1)

        # resultSum = []
        # while i < len(nums):
        #     while j < len(nums):
        #         result = nums[i] +nums[j]
        #         if result == target:
        #             resultSum.append(nums[i])
        #             resultSum.append(nums[j])
        



