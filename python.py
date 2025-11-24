# Factorial and Fibonacci Generator
# Author: Your Name
# Date: 2025

# Function to compute factorial using recursion
def factorial(n):
    if n < 0:
        return "Invalid input! Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Function to generate Fibonacci sequence using iteration
def fibonacci(n):
    if n <= 0:
        return "Invalid input! Enter a positive integer."
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Main section to display output
if __name__ == "__main__":
    num_factorial = 5
    num_fibonacci = 10

    print(f"Factorial of {num_factorial} =", factorial(num_factorial))
    print(f"\nFibonacci sequence of {num_fibonacci} terms:")
    print(fibonacci(num_fibonacci))
