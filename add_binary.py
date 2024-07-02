class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns their sum as a binary string.
        
        :param a: A binary string.
        :param b: A binary string.
        :return: The sum of the two binary strings as a binary string.
        """
        # Determine lengths of the input strings
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a, len_b)
        min_len = min(len_a, len_b)
        
        # Reverse strings to facilitate addition from the least significant bit
        if len_a == max_len:
            max_str = a[::-1]
            min_str = b[::-1]
        else:
            max_str = b[::-1]
            min_str = a[::-1]
        
        # Initialize result array and carry
        result = [0] * (max_len + 1)
        carry = 0
        
        # Perform binary addition
        for i in range(max_len):
            if i >= min_len:
                sum_val = ord(max_str[i]) - ord('0') + carry
            else:
                sum_val = ord(max_str[i]) + ord(min_str[i]) - 2 * ord('0') + carry
                
            result[i] = sum_val % 2
            carry = sum_val // 2
        
        result[-1] = carry
        
        # Remove leading zero if present
        if result[-1] == 0:
            result.pop()
        
        # Convert result array to string and return
        return ''.join(chr(bit + ord('0')) for bit in reversed(result))

# Example usage
s = Solution()
print(s.addBinary("1111", "1111"))  # Output: "11110"
