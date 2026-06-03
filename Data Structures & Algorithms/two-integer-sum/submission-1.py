class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for nums1 in range(len(nums)):
            for nums2 in range(len(nums)):
                if nums[nums1] + nums[nums2] == target and nums1 != nums2:
                    return [nums1, nums2]