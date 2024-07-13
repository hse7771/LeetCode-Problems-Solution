# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The idea to solve this problem is quite simple. It is necessary to find the minimum value on the left side of the maximum value. In other words, it is possible to search maximum value - check it on each new iteration, going through all variants, and update the minimum value on the left simultaneously.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Initialize buy and sell days.
2. Calculate the initial profit.
3. Update buy day.
4. Check if the profit becomes larger and update sell day respectively.
5. Return the result.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(N)$, where $N$ is the number of elements in the array, as $N$ iterations are needed to complete the algorithm.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $O(N)$, where $N$ is the size of the input array, to store it.

# Code
```

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day_i = sell_day_i = 0
        profit = prices[sell_day_i] - prices[buy_day_i]
        for i in range(1, len(prices)):
            if prices[i] < prices[buy_day_i]:
                buy_day_i = i
            if profit < prices[i] - prices[buy_day_i]:
                sell_day_i = i
                profit = prices[sell_day_i] - prices[buy_day_i]
        return profit
```