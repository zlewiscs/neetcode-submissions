class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            # 2 pointers
            l = i + 1
            r = len(nums) - 1
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            while l < r:
                curr_sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if curr_sum == 0:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1        
        
        return res