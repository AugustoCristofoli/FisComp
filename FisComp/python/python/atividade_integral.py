import numpy as np
def integral(f,a,b,N):
    h = (b-a)/(N)
    odd_terms_sum = 0
    even_terms_sum = 0
    partial_sum = 0
    final_integral = 0
    #sum the odd terms 
    for i in range(1, round(N/2)+1):
        odd_terms_sum += f(a+(((2*i)-1)*h))
    
    #sum the even terms
    for i in range(1, round((N/2))):
        even_terms_sum += f(a + (2*i*h))
    
    partial_sum = f(a) + f(b) + (4*odd_terms_sum) + (2*even_terms_sum)
    final_integral = (h/3)*(partial_sum)
    
    return final_integral

def f(x):
    return 2*x

integra = integral(f, 0, 1, 10000)

print(integra)