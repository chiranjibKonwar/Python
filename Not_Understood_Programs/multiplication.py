import sys

from utilities.utils.utils import *

n = 20


for i in range(0, n):

  for j in range(0, n):
      printf("%3d", j+i)

  printf("\n")


sys.exit(0)

m = list(  list(range(1*i,(n+1)*i, i)) for i in range(1,n+1)      )


max_width = len(str(m[-1][-1])) + 1

for i in m:
    i = [str(j).rjust(max_width) for j in i]
    print(''.join(i))
