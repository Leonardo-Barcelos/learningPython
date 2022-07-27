"""
('EN-US')

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

('PT-BR')

Python é uma linguagem de programação orientada a objetos.
Quase tudo em Python é um objeto, com suas propriedades e métodos.
Uma classe é como um construtor de objetos, ou um "projeto" para criar objetos.

"""

"""('EN-US')"""
# Create a Class
## To create a class, use the keyword class

"""('PT-BR')"""
# Criar uma classe
## Para criar uma classe, use a palavra-chave class

class MyPersonClass:
  name = "Clark Kent"
  age = 32
  profession = "Jornalist"

print("---------------------------------------------------------------------------") 

"""('EN-US')"""
# The __init__() Function
## The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
## To understand the meaning of classes we have to understand the built-in __init__() function.
## All classes have a function called __init__(), which is always executed when the class is being initiated.
## Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created  

"""('PT-BR')"""
# A função __init__()
## Os exemplos acima são classes e objetos em sua forma mais simples e não são realmente úteis em aplicações da vida real
## Para entender o significado das classes, temos que entender a função __init__() embutida.
## Todas as classes possuem uma função chamada __init__(), que sempre é executada quando a classe está sendo iniciada.
## Use a função __init__() para atribuir valores às propriedades do objeto ou outras operações que são necessárias quando o objeto está sendo criado:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

"""('EN-US')"""
# The __init__() function is called automatically every time the class is being used to create a new object.

"""('PT-BR')"""
# A __init__()função é chamada automaticamente toda vez que a classe está sendo usada para criar um novo objeto.

print("---------------------------------------------------------------------------") 