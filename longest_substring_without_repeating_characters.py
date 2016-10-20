class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, i, j, rec = 0, 0, 0, {}
        for j in range(len(s)):
            if s[j] not in s[i:j]:
                res = max(res, j-i+1)
            else:
                i = rec[s[j]] + 1
            rec[s[j]] = j
        return res


if __name__ == '__main__':
    s = Solution()
    #print s.lengthOfLongestSubstring('"xoithejobprotumenselsftseduwrakoosjyysmzhfpccdgpvmaptvhyyewsggiuasuak"')
   # print s.lengthOfLongestSubstring('asdfasdfasdf')
    print s.lengthOfLongestSubstring('abcabcbb')
