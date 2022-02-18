# Criando classe matriz que sobrecarrega multiplicação de matrizes

Deve ser possível criar duas matrizes

```python
    >>> from ex_matriz import matriz
    >>> m1 = matriz.Matriz([[1], [2]])  # Matriz 2x1
    >>> m2 = matriz.Matriz([[3, 4]])  # Matriz 1x2
    >>> m3 = matriz.Matriz([[1, 2], [3, 4]])

```

Deve ser possível multiplicar matrizes. Onde o número de colunas da primeira é igual
número de linhas da segunda

```python
    >>> m1 @ m2
    Matriz([[3, 4], [6, 8]])
    >>> m3 @ m3
    Matriz([[7, 10], [15, 22]])

```