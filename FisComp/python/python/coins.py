import numpy as np
import matplotlib.pyplot as plt

n = 10
N = 1000
resultados = []
for i in range(N+1):
    x = sum(np.random.randint(0, 2, n))        
    resultados.append(x)


plt.hist(resultados, bins=n, range=(1,n+1), align='left', color='blue', edgecolor='black')
plt.savefig('hist.png')