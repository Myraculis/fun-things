import random
from matplotlib import pyplot as plt
import numpy as np

size = int(input('What is the size?'))
balls = int(input('How much data?'))
r1 = int((size / 2) - 1)
r2 = int(size/2)
r3 = int(size-1)

A = [[0 for x in range(size)] for y in range(size)]

x = []
y = []

for r in range(balls):

  col = random.choice([r1,r2])
  for s in range(r1):
    k = random.choice([1,-1])
    col = col + k
  f = 0
  for d in range(size):
    q = r3 - d
    if A[q][col] == 0:
      if f == 0:
        A[q][col] = 1
        f = 1

for i in range(size):
  for j in range(size):
    if A[i][j] == 1:
      y.append((size-i))
      x.append(j)
      
sizes = np.random.uniform(15, 15, len(x))
colors = np.random.uniform(80, 80, len(x))

fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, size),
       ylim=(0, size))
  
plt.show()