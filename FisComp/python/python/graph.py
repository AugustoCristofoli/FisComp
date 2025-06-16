import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.15)
f1 = np.sin(x)
f2 = np.cos(x)

p1 = np.random.rand(10)  # array com 50 números aleatórios entre 0 e 4
p2 = np.random.rand(10)  # array com 50 números aleatórios entre 0 e 10




fig, ax = plt.subplots(figsize=(6,4))
ax.plot(x, f1, '--', color='r', lw=1, ms=4)
ax.text(0.85, 0.7, 'texto aqui', transform=ax.transAxes) ## coordenadas relativas aos Axes da figura
                                                        ## esses vão de (0,0) no canto inferior esquerdo
                                                        ## a (1,1) no canto superior direito
                                                        ## Compare com próximo gráfico
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$\sin(\alpha)$', fontsize=15)     ## Latex para gerar o texto das labels
plt.show()

fig, ax = plt.subplots(figsize=(6,4))
ax.plot(x, f1, 'o--', color='b', lw=0.6, ms=4)
ax.text(3., 0.75, 'texto aqui', transform=ax.transData)  ## coordenadas relativas aos dados da figura,
                                                        ## controlados por xlim e ylim
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$\sin(\alpha)$', fontsize=15)
plt.show()
