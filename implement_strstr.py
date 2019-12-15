class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        target_hashcode = 0
        for i in range(len(needle)):
            target_hashcode = (target_hashcode * 31 + ord(needle[i]) - ord('a')) % 10 ** 5

        multiplier = 31 ** (len(needle) - 1)
        new_hashcode = 0
        for i in range(len(haystack)):
            if i > len(needle) - 1:
                new_hashcode = (new_hashcode - multiplier * (ord(haystack[i - len(needle)]) - ord('a'))) % 10 ** 5

            new_hashcode = (new_hashcode * 31 + ord(haystack[i]) - ord('a')) % 10 ** 5
            if new_hashcode == target_hashcode:
                if self.check(needle, haystack[i - len(needle) + 1:i + 1]):
                    return i - len(needle) + 1
        return -1

    def check(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True