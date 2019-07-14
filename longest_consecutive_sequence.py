#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#Your algorithm should run in O(n) complexity.

#Input: [100, 4, 200, 1, 3, 2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
#Therefore its length is 4.


class Solution(object):
    # hashTable
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num_set = set(nums)
        rst = 1
        for num in nums:
            if num-1 not in num_set:
                currentNum = num
                streak = 1
                while currentNum+1 in num_set:
                    currentNum += 1
                    streak += 1
                rst = max(rst,streak)
        return rst
