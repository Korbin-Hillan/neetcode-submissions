class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.arr = [0] * (len(nums) * 2)
        i = 0
        for val in nums:
            self.arr[i] = val
            i += 1

        for val in nums:
            self.arr[i] = val
            i += 1
            
        return self.arr