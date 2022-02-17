# Criando classe matriz que sobrecarrega multiplicação de matrizes

Deve ser possível criar duas matrizes

```python
    >>> from ex_matriz import matriz
    >>> m1 = matriz.Matriz([1], [2])  # Matriz 2x1
    >>> m2 = matriz.Matriz([3, 4])  # Matriz 1x2

```

Deve ser possível multiplicar matrizes. Onde o número de colunas da primeira é igual
número de linhas da segunda

```python
    >>> m1 @ m2
    Matriz([[3, 4], [6, 8]])

```