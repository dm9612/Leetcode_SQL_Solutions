class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if len(nums)<k :
            return 0
        
        total = sum(nums[:k])
        maxsum = total

        for i in range(len(nums)-k):
            total -=nums[i]
            total +=nums[i+k]
            maxsum = max(total,maxsum)

        return maxsum/k