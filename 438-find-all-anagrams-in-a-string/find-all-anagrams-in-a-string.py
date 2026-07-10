from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        need = Counter(p)
        window = Counter()
        left = 0
        matched = 0
        res = []

        for right, ch in enumerate(s):
            window[ch] += 1
            if window[ch] == need[ch]:
                matched += 1

            while right - left + 1 > len(p):
                left_ch = s[left]
                if window[left_ch] == need[left_ch]:
                    matched -= 1
                window[left_ch] -= 1
                left += 1

            if matched == len(need):
                res.append(left)

        return res