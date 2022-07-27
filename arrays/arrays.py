"""
('EN-US')
 Python does not have built-in support for Arrays, but Python Lists can be used instead.
 To work with arrays in Python you will have to import a library, like the NumPy library.

What is an Array?
An array is a special variable, which can hold more than one value at a time.


-------- Array Methods

    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the first item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list


('PT-BR')
 O Python não possui suporte integrado para Arrays, mas as Listas do Python podem ser usadas.
 Para trabalhar com arrays em Python você terá que importar uma biblioteca, como a biblioteca NumPy.

O que é uma Matriz?
Um array é uma variável especial, que pode conter mais de um valor por vez.


--------  Métodos de matriz

    append()	Adiciona um elemento no final da lista
    clear()	    Remove todos os elementos da lista
    copy()	    Retorna uma copia da lista
    count()	    Retorna o número de elementos com o valor especificado
    extend()	Adicione os elementos de uma lista (ou qualquer iterável) ao final da lista atua
    index()	    Retorna o índice do primeiro elemento com o valor especificado
    insert()	Adiciona um elemento na posição especificada
    pop()	    Remove o elemento na posição especificada
    remove()	Removes the first item with the specified value
    reverse()	Inverte a ordem da lista
    sort()	    Classifica a lista

"""

print("---------------------------------------------------")


cars = ["Ford", "Volvo", "BMW"]
print(cars)

print("---------------------------------------------------")


('EN-US')
# Lenght of an Array

('PT-BR')
# O comprimento de uma matriz

lenght = len(cars)
print(lenght)

print("---------------------------------------------------")

('EN-US')
# Looping Array Elements
## You can use the for in loop to loop through all the elements of an array.


('PT-BR')

# Elementos de Matriz em Loop
## Você pode usar o for inloop para percorrer todos os elementos de uma matriz.

for element in cars:
  print(element)

print("---------------------------------------------------")

('EN-US')
# Adding Array Elements
## You can use the append() method to add an element to an array.

('PT-BR')
# Adicionando elementos de matriz
## Você pode usar o append()método para adicionar um elemento a uma matriz.


cars.append("Honda")
print(cars)

print("---------------------------------------------------")

('EN-US')
# Removing Array Elements
## You can use the pop() method to remove an element from the array.

('PT-BR')
# Removendo elementos da matriz
## Você pode usar o pop()método para remover um elemento da matriz.

cars.pop(1) # using the position of element you wanna remove.
print(cars)

print("---------------------------------------------------")