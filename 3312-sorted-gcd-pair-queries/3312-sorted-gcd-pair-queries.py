from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        div_cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for m in range(g, mx + 1, g):
                div_cnt[g] += freq[m]

        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            c = div_cnt[g]
            exact[g] = c * (c - 1) // 2
            for m in range(g * 2, mx + 1, g):
                exact[g] -= exact[m]

        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        return [bisect_right(prefix, q) for q in queries]