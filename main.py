import argparse
import time
import matplotlib.pyplot as plt

class CongruentLinearGenerator:
    def __init__(self, seed=None, a=1664525, c=1013904223, m=2**32):
        if seed is None:
            self.seed = int(time.time())
        else:
            self.seed = seed
        self.a = a
        self.c = c
        self.m = m
    
    def rand(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m

def generate_numbers(clg, num):
    numbers = []
    for i in range(num):
        numbers.append(clg.rand())
    return numbers

def save_numbers(numbers, filename):
    with open(filename, 'w') as f:
        for num in numbers:
            f.write(str(num) + '\n')

def save_variables(x0, a, c, m, filename):
    with open(filename, 'w') as f:
        f.write(f'x0={x0}\n')
        f.write(f'a={a}\n')
        f.write(f'c={c}\n')
        f.write(f'm={m}\n')

def plot_scatter(numbers):
    plt.scatter(range(len(numbers)), numbers, s=1)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Gráfico de Dispersão dos Números Pseudoaleatórios')
    plt.savefig('scatter.png')

# Argumentos de linha de comando
parser = argparse.ArgumentParser(description='Gera números pseudoaleatórios usando o método congruente linear.')
parser.add_argument('--seed', type=int, help='Define a semente do gerador.')
args = parser.parse_args()

clg = CongruentLinearGenerator(seed=args.seed)
save_variables(clg.seed, clg.a, clg.c, clg.m, 'variables.txt')
numbers = generate_numbers(clg, 1000)
save_numbers(numbers, 'numbers.txt')
plot_scatter(numbers)