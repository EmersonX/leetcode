class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, l, result,  = 0, len(s), ''

        while i < l:
            interval = 0
            while i - interval >= 0 and i + interval < l:
                if not s[i-interval] == s[i+interval]:
                    break
                interval += 1
            interval = interval - 1 if interval else 0
            if (interval * 2 + 1) > len(result):
                result = s[i-interval:i+interval+1]

            interval = 0
            while  i - interval >= 0 and i + 1 + interval < l:
                if not s[i-interval] == s[i+interval+1]:
                    break
                interval += 1
            if interval:
                interval = interval - 1
                if (interval * 2 + 2) > len(result):
                    result = s[i-interval:i+interval+2]

            i += 1
        return result


if __name__ == '__main__':
    testcases = ('zxabac', 'asaaa', 'maambbccddmn', 'abb')
    s = Solution()
    for case in testcases:
        print("{}: {}".format(case, s.longestPalindrome(case)))
