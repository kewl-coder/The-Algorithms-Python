import sys

def matrix_chain_multiplication(dims):
    n = len(dims) - 1  # Number of matrices
    dp = [[0] * n for _ in range(n)]  # Initialize a 2D DP table

    # Fill the DP table using a bottom-up approach
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize  # Initialize the minimum cost to a large value

            for k in range(i, j):
                # Calculate the cost of multiplying matrices (i, i+1, ..., k) and (k+1, k+2, ..., j)
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]  # Minimum cost of multiplying all matrices

# Example usage:
if __name__ == "__main__":
    matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]
    min_cost = matrix_chain_multiplication(matrix_dimensions)
    print("Minimum cost of matrix chain multiplication:", min_cost)
