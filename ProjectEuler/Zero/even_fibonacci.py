def fib(n):
    fibonacci = [0, 1]

    # Iterate from 2 to n. It will nver reach n though because curr outgrows n.
    for i in xrange(2, n):
        # Find the next term in the sequence and append to list.
        curr = fibonacci[i - 1] + fibonacci[i - 2]

        # curr could go over n at this point so check.
        if curr > n:
            break

        fibonacci.append(curr)

        # Increment i to calculate next.
        i += 1

    return fibonacci

def solve(n):
    sequence = fib(n)

    return sum([i for i in sequence if i % 2 == 0])