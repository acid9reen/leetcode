import typing as tp
from itertools import accumulate
from operator import mul


class Solution:
    def productExceptSelf(self, nums: tp.List[int]) -> tp.List[int]:
        prefix = accumulate(nums[:-1], mul, initial=1)
        postfix = reversed(list(accumulate(nums[:0:-1], mul, initial=1)))

        return [mul(x, y) for x, y in zip(prefix, postfix, strict=True)]
