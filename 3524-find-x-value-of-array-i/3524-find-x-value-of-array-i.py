from typing import List


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int
    ) -> List[int]:

        result = [0] * k

        # dp[r] = number of subarrays ending
        # at the previous index with remainder r
        dp = [0] * k

        # Required by the problem.
        lurminexod = nums[:]

        for num in nums:

            new_dp = [0] * k

            v = num % k

            # Start [num].
            new_dp[v] += 1

            # Extend every previous ending subarray.
            for r in range(k):

                new_r = (r * v) % k

                new_dp[new_r] += dp[r]

            # Add all subarrays ending here
            # to the global answer.
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result