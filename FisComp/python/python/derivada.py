import matplotlib.pyplot as plt

def derivar(f,x, deltaX):
    return (f(x+deltaX) - f(x))/deltaX

def derivar_centro(f,x, deltaX):
    return (f(x+deltaX) - f(x-deltaX))/(2*deltaX)


def f(x):
    return 5*(x**2)-(3*x)

derivada_dir = []
derivada_centro = []
deltas = [1.e-2,1.e-4,1.e-6,1.e-8,1.e-10,1.e-12,1.e-14]

derivada_dir.append(derivar(f, 1, 1.e-2))
derivada_dir.append(derivar(f, 1, 1.e-4))
derivada_dir.append(derivar(f, 1, 1.e-6))
derivada_dir.append(derivar(f, 1, 1.e-8))
derivada_dir.append(derivar(f, 1, 1.e-10))
derivada_dir.append(derivar(f, 1, 1.e-12))
derivada_dir.append(derivar(f, 1, 1.e-14))

derivada_centro.append(derivar_centro(f, 1, 1.e-2))
derivada_centro.append(derivar_centro(f, 1, 1.e-4))
derivada_centro.append(derivar_centro(f, 1, 1.e-6))
derivada_centro.append(derivar_centro(f, 1, 1.e-8))
derivada_centro.append(derivar_centro(f, 1, 1.e-10))
derivada_centro.append(derivar_centro(f, 1, 1.e-12))
derivada_centro.append(derivar_centro(f, 1, 1.e-14))

plt.plot(deltas,derivada_dir,color ='red',marker='o',linestyle='--',linewidth=2.0,markersize=5,label='dir')  #gráfico com os valores da função seno (array f1) em função de x (array x) obtidos acima
plt.plot(deltas,derivada_centro,'bs-',label='centro') # adicionando na mesma figura o gráfico com os valores da função cosseno (arra
plt.legend() #para adicionar a legenda com as labels definidas acima na função plt.plot
plt.grid()  #adicionando grade
plt.show()