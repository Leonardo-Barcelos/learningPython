"""
('EN-US')

Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

>>>> Let us create a method in the Person class. (Note We teach you how to create objects in classes.py)


(PT-BR)

Métodos de objeto
Objetos também podem conter métodos. Métodos em objetos são funções que pertencem ao objeto.

>>>> Vamos criar um método na classe Person. (Nota Ensinamos como criar objetos no classes.py )

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John McClane", 36)
p1.myfunc()

"""('EN-US')"""
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

"""(PT-BR) """
# O self parâmetro é uma referência à instância atual da classe e é usado para acessar variáveis ​​que pertencem à classe.

print('-----------------------------------------------------------------------------')

"""('EN-US')"""
# The self Parameter

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.

"""(PT-BR) """
# O parâmetro self

# O selfparâmetro é uma referência à instância atual da classe e é usado para acessar as variáveis ​​que pertencem à classe.
# Ele não precisa ser nomeado self, você pode chamá-lo como quiser, mas deve ser o primeiro parâmetro de qualquer função da classe.


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John McClane", 36)
p1.myfunc()

"""('EN-US')"""
# Used the words mysillyobject and abc instead of self

"""(PT-BR) """
# Usei as palavras mysillyobject e abc em vez de self

print('-----------------------------------------------------------------------------')
