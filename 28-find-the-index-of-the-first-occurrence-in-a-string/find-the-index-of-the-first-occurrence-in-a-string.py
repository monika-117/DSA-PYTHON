class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        return haystack.find(needle)