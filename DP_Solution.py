from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Dynamic Programming Solution, Time Complexity: O(n^3), Space Complexity: O(n^2) 
        # Define a dictionary to map operators to their corresponding functions
        operators = {
            '*': lambda a, b: a * b,  # Multiplication
            '+': lambda a, b: a + b,  # Addition
            '-': lambda a, b: a - b   # Subtraction
        }

        # Tokenize the expression into numbers and operators
        tokens = []
        num = ""
        for char in expression:
            if char in operators:
                tokens.append(int(num))  # Append the number found so far
                tokens.append(char)      # Append the operator
                num = ""  # Reset for the next number
            else:
                num += char  # Build the number character by character
        tokens.append(int(num))  # Append the last number

        # Length of tokens
        n = len(tokens)

        # DP table where dp[i][j] stores all possible results for tokens[i:j+1]
        dp = [[[] for _ in range(n)] for _ in range(n)]

        # Initialize the DP table for single numbers (base case)
        for i in range(0, n, 2):  # Numbers are located at even indices
            dp[i][i] = [tokens[i]]

        # Iterate over subexpression lengths (must be odd to include operator)
        for length in range(3, n + 1, 2):  # Start from subexpression of length 3 (num-op-num)
            for start in range(0, n - length + 1, 2):  # Iterate over possible start positions
                end = start + length - 1  # Calculate the end index of the subexpression
                dp[start][end] = []  # Initialize this range's results
                
                # Iterate over operators within this subexpression
                for k in range(start + 1, end, 2):  # Operators are at odd indices (between two numbers)
                    operator = tokens[k]
                    
                    # Get all results from the left and right subexpressions
                    left_results = dp[start][k - 1]
                    right_results = dp[k + 1][end]
                    
                    # Combine each result from the left and right using the operator
                    for left_value in left_results:
                        for right_value in right_results:
                            dp[start][end].append(operators[operator](left_value, right_value))

        # The final result for the entire expression is stored in dp[0][n-1]
        return dp[0][n - 1]