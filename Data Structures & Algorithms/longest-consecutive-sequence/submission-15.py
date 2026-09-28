class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in numbers:
            if num - 1 not in numbers:
                next_num = num + 1
                length = 1
                while next_num in numbers:
                    length += 1
                    next_num += 1
                longest = max(length,longest)
        return longest



                