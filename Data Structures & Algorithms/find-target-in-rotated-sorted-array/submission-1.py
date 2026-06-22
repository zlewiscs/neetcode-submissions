class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [5,6,1,2,3,4]
        # [6,1,2,3,4,5]
        # [3,4,5,6,1,2]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid
            
            # left half sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # right half sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
