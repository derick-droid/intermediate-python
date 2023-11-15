"""

"""

L = [[1, 2, 3],
  [4, 5, 6],
[7 ,8 ,9]]

count = sum([1 for r in range(5) for c in range(5) if L[r][c] % 2 == 0])

print(count)