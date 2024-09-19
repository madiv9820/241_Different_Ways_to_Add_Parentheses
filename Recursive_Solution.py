from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Recursive Solution, Time Complexity: O(2^n), Space Complexity: O(n)
        # Dictionary to store the available operations and their corresponding functions
        operations = {
            '*': lambda x, y: x * y,  # Multiplication
            '+': lambda x, y: x + y,  # Addition
            '-': lambda x, y: x - y   # Subtraction
        }

        # Recursive helper function to evaluate the expression in various ways
        def evaluateExpression(start: int, end: int) -> List[int]:
            results = []  # Stores the results of all possible computations for the current subexpression
            
            # Loop through the expression from 'start' to 'end'
            for i in range(start, end + 1):
                # If the current character is an operator, split the expression
                if expression[i] in operations:
                    # Recursively solve the left and right parts of the expression around the operator
                    left_results = evaluateExpression(start, i - 1)
                    right_results = evaluateExpression(i + 1, end)

                    # Combine the results from left and right subexpressions using the operator
                    for left_value in left_results:
                        for right_value in right_results:
                            # Apply the operation (e.g., +, -, *)
                            results.append(operations[expression[i]](left_value, right_value))
            
            # If no operator was found, the expression is a single number; add it as a result
            if not results:
                results.append(int(expression[start:end + 1]))

            return results

        # Call the recursive function starting with the full expression
        return evaluateExpression(0, len(expression) - 1)