class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # a = len(nums)
        # min_length = float('inf')
        # for i in range(a):
        #     total = 0
        #     for j in range(i,a):
        #         total +=nums[j]
        #         if total >= target:
        #             min_length = min(min_length, j-i+1)
        #             break

        # return min_length if min_length != float('inf') else 0  

        l = 0
        total = 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total>=target:
                res = min(r-l+1, res)
                total -= nums[l]
                l+=1
        
        return 0 if res == float('inf') else res
