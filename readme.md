Factorial and Fibonacci Generator



A simple Python script that demonstrates two fundamental mathematical operations:



Factorial calculation using recursion

Fibonacci sequence generation using iteration





Features



Factorial Function



Computes the factorial of a non-negative integer.

Implements recursion.

Returns an error message for negative inputs.



Fibonacci Function



Generates the first n terms of the Fibonacci sequence.

Uses an iterative approach.

Returns an error message for non-positive integers.



---



Code Overview



factorial(n)



python

def factorial(n):

    if n < 0:

        return "Invalid input! Factorial is not defined for negative numbers."

    if n == 0 or n == 1:

        return 1

    return n * factorial(n - 1)





Fibonacci(n)



python

def Fibonacci(n):

    if n <= 0:

        return "Invalid input! Enter a positive integer."

    

    sequence = [0, 1]

    for I in range(2, n):

        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:n]





Program Output (Main Section)
The script demonstrates usage with sample values:


python
num_factorial = 5
num_fibonacci = 10


How to Run
1. Make sure you have Python 3 installed.
2. Save the script (e.g., main.py).
3. Run it using:



bash
python main.py


Example Output

Factorial of 5 = 120
Fibonacci sequence of 10 terms:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
