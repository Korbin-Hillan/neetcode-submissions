class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        for char in bin(n)[2:]:
            print(char)
            if (char == "1"):
                answer += 1
        return answer