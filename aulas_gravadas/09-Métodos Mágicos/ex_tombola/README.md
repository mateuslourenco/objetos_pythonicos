# TDD da Tombola

Uma tômbola pode ser criada da segunte maneira: 

```python
    >>> from ex_tombola import tombola
    >>> t = tombola.Tombola()

```

Após a criação os itens da tômbula são representados por uma lista vazia:

```python
    >>> t.itens
    []

```

Uma lista recem criada não possui elementos. Portanto o método "carregada" retorna falso:
```python
    >>> t.carregada()
    False

```

É possível carregar itens através do método "carregar":

```python
    >>> itens = [1, 2]
    >>> t.carregar(itens)
    >>> t.itens
    [1, 2]

```

Após ser carregada o método "carregada" retorna verdadeiro:

```python
    >>> t.carregada()
    True

```

Uma tômbola pode misturar os seus itens:

```python
    >>> def embaralhador_mock(lista):
    ...     lista[0], lista[-1] = lista[-1], lista[0]
    >>> tombola.shuffle = embaralhador_mock
    >>> t.itens
    [1, 2]
    >>> t.misturar()
    >>> t.itens
    [2, 1]

```

Uma tômbola serve para sortear elementos:

```python
    >>> t.sortear()
    1
    >>> t.carregada()
    True

```

O principal método da tombola é sortear. Portanto, se invocada diretamente, ela executa esse método

```python
    >>> t()
    2
    >>> t.carregada()
    False
    >>> itens
    [1, 2]

```