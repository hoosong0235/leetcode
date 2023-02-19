class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sol = []
        for i in range(1, n + 1):
            if not(i % 3 or i % 5):
                sol.append("FizzBuzz")
            elif not(i % 3):
                sol.append("Fizz")
            elif not(i % 5):
                sol.append("Buzz")
            else:
                sol.append(str(i))
        return sol