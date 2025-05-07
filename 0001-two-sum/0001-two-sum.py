class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i, value in enumerate(nums):

            want = target - value
            if want in d:
                return [d[want],i]
            
            d[value]=i