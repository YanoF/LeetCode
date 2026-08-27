# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i, ch in enumerate(s):
            value = values[ch]
            if i + 1 < len(s) and value < values[s[i + 1]]:
                total -= value
            else:
                total += value
        return total