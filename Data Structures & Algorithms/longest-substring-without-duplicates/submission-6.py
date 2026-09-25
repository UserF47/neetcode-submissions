class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        lastest_dup = -1
        ch_lastest_show_up_index = dict()

        for i in range(len(s)):
            if s[i] in ch_lastest_show_up_index and ch_lastest_show_up_index[s[i]] > lastest_dup:
                res = max(res, i - ch_lastest_show_up_index[s[i]])
                lastest_dup = ch_lastest_show_up_index[s[i]]
                ch_lastest_show_up_index[s[i]] = i
            else:
                ch_lastest_show_up_index[s[i]] = i
                res = max(i-lastest_dup, res)
        
        return res