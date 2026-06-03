class Solution:
    def countBits(self, n: int) -> List[int]:
        my_list = []
        for i in range(n + 1):
            num = 0
            binary = bin(i)
            binary_no_prefix = binary[2:]
            binary_string = str(binary_no_prefix)
            for char_digit in binary_string:
                if char_digit == '1':
                    num += 1
            
            my_list.append(num)
        return my_list