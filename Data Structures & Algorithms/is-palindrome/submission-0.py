import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = s.translate(str.maketrans('', '', string.punctuation))

        if (s == s[::-1]):
            return True

        return False