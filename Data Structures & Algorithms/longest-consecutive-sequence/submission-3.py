class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in nset:
                l = 1
                while (n+l) in nset:
                    l = l + 1
                
                longest = max(longest, l)
        return longest