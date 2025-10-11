class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:].zfill(32)
        reversed_binary = ''.join(reversed(binary))
        return int(reversed_binary, 2)