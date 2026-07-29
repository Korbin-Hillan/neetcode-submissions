import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        reversed_string = s[::-1]

        if (s == reversed_string):
            return True
        print(s)
        print(reversed_string)
        return False