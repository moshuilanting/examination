Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.




class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        L_max=nums[0]
        L_min=nums[0]
        final=nums[0]
        for i in range(1,len(nums)):
            L_max_old=L_max
            L_max=max(nums[i],max(nums[i]*L_max,nums[i]*L_min))
            L_min=min(nums[i],min(nums[i]*L_max_old,nums[i]*L_min))
            if L_max>final:
                final=L_max
        return final
