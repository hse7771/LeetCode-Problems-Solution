from typing import List


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
                generate_combinations(aphabeth, ind + 1, n - 1, combinations, combination)
                combination = combination[:-1]

        generate_combinations(alphabeth, 0, len(alphabeth), combinations)
        return combinations
