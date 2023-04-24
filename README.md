# SMA - Desenvolvimento de um gerador de números pseudo-aleatórios

Pontifícia Universidade Católica do Rio Grande do Sul
Escola Politécnica
Engenharia de Software
4611G-04 - Simulação e Métodos Analíticos
Turma 031 - 2023/1
Aluno: Marco Goedert

## Enunciado

Utilizando o conceito do método Congruente Linear para geração de números pseudo-aleatórios, programe um método que gere 1.000 (mil) números (entre os valores 0 e 1) a fim de produzir um gráfico de dispersão. 

Você pode utilizar a linguagem de programação que desejar.

A fim de validar seu método, envie um arquivo texto com os 1.000 números pseudo-aleatórios produzidos pelo seu método, o gráfico de dispersão destes números, e também um arquivo contendo os valores utilizados para as variáveis X0 (semente), a, c e M.

## Resolução

O método congruente linear é um método de geração de números pseudo-aleatórios que utiliza uma função linear para gerar uma sequência de números pseudo-aleatórios. A função linear é dada por:

![equation](https://latex.codecogs.com/gif.latex?X_%7Bi&plus;1%7D%20%3D%20%28aX_i&plus;c%29%20%5C%25%20M)

onde X<sub>i</sub> é o número pseudo-aleatório gerado na iteração i, X<sub>i+1</sub> é o número pseudo-aleatório gerado na iteração i+1, a, c e M são constantes inteiras e X<sub>0</sub> é a semente.

Para gerar os números pseudo-aleatórios, é necessário definir os valores das constantes a, c e M. Para isso, foi utilizado o método de Park e Miller (Numerical Recipes), que utiliza os valores:

![equation](https://latex.codecogs.com/gif.latex?a%20%3D%201664525%2C%20c%20%3D%201013904223%2C%20m%20%3D%202%5E%7B32%7D)
