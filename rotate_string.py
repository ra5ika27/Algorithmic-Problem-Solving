class Solution:
    def rotateString(self, A, B):
        n = len(A)
        m = len(B)
        if n != m:
            return False
        if not n:
            return True
        shifts = [1] * (n + 1)

        def suffix_array():
            i = -1
            for j in range(n):
                while i >= 0 and B[i] != B[j]:
                    i -= shifts[i]
                shifts[j + 1] = j - i
                i += 1

        def match():
            new_text = A + A
            match_length = 0
            for letter in new_text:
                while match_length >= 0 and B[match_length] != letter:
                    match_length = match_length - shifts[match_length]
                match_length += 1
                if match_length == n:
                    return True
            return False

        suffix_array()
        ans = match()
        return ans