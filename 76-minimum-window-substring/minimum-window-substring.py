from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        best = (float("inf"), 0, 0)

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                window_len = right - left + 1
                if window_len < best[0]:
                    best = (window_len, left, right)

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return s[best[1]:best[2] + 1] if best[0] != float("inf") else ""