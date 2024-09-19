from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Define a dictionary to map operators to their corresponding operations
        operators = {
            '*': lambda a, b: a * b,  # Multiplication
            '+': lambda a, b: a + b,  # Addition
            '-': lambda a, b: a - b   # Subtraction
        }
        
        # Memoization dictionary to store results of subexpressions
        memo = {}

        # Helper function to compute all possible results for subexpression from 'left' to 'right'
        def computeWays(left: int, right: int) -> List[int]:
            # If the result for this subexpression has already been computed, return it
            if (left, right) in memo:
                return memo[(left, right)]

            results = []  # List to store the results of the current subexpression

            # Loop through the expression from 'left' to 'right'
            for i in range(left, right + 1):
                # If the current character is an operator, split the expression
                if expression[i] in operators:
                    # Recursively calculate the results of the left and right parts of the expression
                    left_results = computeWays(left, i - 1)
                    right_results = computeWays(i + 1, right)

                    # Combine the results from the left and right parts using the operator
                    for left_value in left_results:
                        for right_value in right_results:
                            results.append(operators[expression[i]](left_value, right_value))

            # Base case: if no operator was found, it's a single number, so return it as the result
            if not results:
                results.append(int(expression[left:right + 1]))

            # Memoize the result for the current subexpression
            memo[(left, right)] = results
            return results

        # Initiate the recursive function for the entire expression
        return computeWays(0, len(expression) - 1)
