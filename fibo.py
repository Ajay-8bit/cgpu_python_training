# Function to generate Fibonacci sequence up to 'n' numbers
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Input: Number of terms
n = int(input("Enter the number of terms: "))

# Get the Fibonacci sequence
fib_seq = fibonacci(n)

# Output: Display the Fibonacci sequence
print(f"The Fibonacci sequence up to {n} terms is:")
print(fib_seq)
