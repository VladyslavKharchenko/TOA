from functools import lru_cache


class KnapSack:

    def __init__(self, size, value):
        self.size = size
        self.value = value

    @lru_cache()
    def solve(self, c, i=0):

        if c < 0:
            return -max(self.value), []
        if i == len(self.size):
            return 0, []

        r1 = self.solve(c,  i + 1)
        r2 = self.solve(c - self.size[i], i + 1)
        r2 = (r2[0] + self.value[i], [i] + r2[1])

        if r1[0] >= r2[0]:
            return r1
        else:
            return r2
