import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def congruential_random_numbers(X0, a, c, m, n):
    random_numbers = []
    Xn = X0
    for _ in range(n):
        Xn = ((a * Xn) + c) % m
        random_numbers.append(Xn)
    return random_numbers

X0 = 1
a = 13
c = 0
m = 64
n = 100

random_numbers = congruential_random_numbers(X0, a, c, m, n)

print("Números aleatorios", random_numbers)

# Calcular la media R
mediaR = np.mean(random_numbers) / m

# Calcular la varianza R
varianzaR = np.var(random_numbers) / m

print("Media R:", mediaR)
print("Varianza R:", varianzaR)

# Calcular la media X
mediaX = np.mean(random_numbers) 

# Calcular la varianza R
varianzaX = np.var(random_numbers) 

print("Media X:", mediaX)
print("Varianza X:", varianzaX)

# Histograma
plt.figure(figsize=(8, 6))
sns.histplot(random_numbers, bins=10, kde=True, color='blue')
plt.title('Histograma de números pseudo-aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(range(1, n+1), random_numbers, color='red')
plt.title('Scatter plot de números pseudo-aleatorios')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.show()