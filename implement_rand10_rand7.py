# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        while True:
            row = rand7()
            column = rand7()
            index = column + (row - 1) * 7
            if index <= 40:
                break

        random = 1 + (index - 1) % 10
        return random
