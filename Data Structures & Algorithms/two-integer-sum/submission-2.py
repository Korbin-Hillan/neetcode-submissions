class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for key, value in enumerate(nums):
            compliment = target - value

            if compliment in hashmap:
                print("Compliment: ", compliment)
                print("Value: ", value)
                return [hashmap[compliment], key]
            hashmap[value] = key
                
        return []