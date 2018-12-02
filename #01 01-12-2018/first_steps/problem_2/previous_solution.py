
def collatz(n):
    seq = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        seq += 1
    return seq

def largest_sequence(k):
    maior = 0
    ans = (0, 0)
    for i in range(1, k+1):
        t = collatz(i)
        if t > ans[1]:
            ans = (i, t)
    return ans