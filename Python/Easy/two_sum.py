from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} #dictionary to store the value and its index

        for i, num in enumerate(nums):
            complement = target - num

            #If compliment exists in the dictionary, we found the pair
            if complement in seen:
                return [seen[complement], i]

            #otherwise, add the current number and its index to the dictionary
            seen[num] = i

        return []
        