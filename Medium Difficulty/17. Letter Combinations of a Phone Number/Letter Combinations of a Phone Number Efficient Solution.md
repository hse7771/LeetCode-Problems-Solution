# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Remember about algorithm to generate combinations using recursion.

# Approach
<!-- Describe your approach to solving the problem. -->
1. Create hashtable for number - letters equivalence.
2. Implement combination generation algorithm.
3. Apply modification tracking what set of symbols to use on the next call.
4. Return list of generated combinatios.

On each new call in the function the already generated part of combination is remembered and in a loop it adds every new possible element sequentially making the next call respectievely.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $O(C^N)$, where n is the number of digits in the input string, as the number of combinations calculates as product of all potential elements on each place in the particular combination.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity $O(C^N)$,  where n is the number of digits in the input string, to store all combinations.

# Code
```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(map(int, digits))
        l = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        alphabeth = [l[digit] for digit in digits]
        combinations = []


        def generate_combinations(aphabeth, ind, n, combinations, combination=None):
            combination = combination or ""

            if n == 0:
                if len(combination) != 0:
                    combinations.append(combination)
                return
            for i in range(len(aphabeth[ind])):
                combination += aphabeth[ind][i]
                generate_combinations(aphabeth, ind+1, n-1, combinations, combination)
                combination = combination[:-1]
        generate_combinations(alphabeth, 0, len(alphabeth), combinations)
        return combinations
```