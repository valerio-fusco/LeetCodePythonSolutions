# LeetCode problem: https://leetcode.com/problems/two-sum/

from typing import *


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        n1 = nums[i]

        for j in range(i + 1, len(nums)):
            n2 = nums[j]

            if (n1 + n2) == target:
                return [i, j]

