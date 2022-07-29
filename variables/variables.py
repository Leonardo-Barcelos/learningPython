# Creating Variables
"""
('EN-US')
Python has no command for declaring a variable.
Variables do not need to be declared with any particular type, and can even change type after they have been set.

('PT-BR')
Python não tem comando para declarar uma variável.
Uma variável é criada no momento em que você atribui um valor a ela.

"""
"""
('EN-US')                                                                  ('PT-BR')
******DATA TYPES********                                                 ******TIPOS DE DADOS********      
Text Type:	str                                                          Text Type:	str
Numeric Types:	int, float, complex                                      Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range                                       Sequence Types:	list, tuple, range
Mapping Type:	dict                                                     Mapping Type:	dict
Set Types:	set, frozenset                                               Set Types:	set, frozenset
Boolean Type:	bool                                                     Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview                             Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType                                                     None Type:	NoneType

"""
x = "John"  # str
y = 5  # int
z = True  # bool
a = 2.2  # float
b = ["html", "css", "java"]  # list
c = range(10)  # range
d = None  # NoneType
e = 1j  # Complex
f = ("apple", "banana", "cherry")  # tuple
# ('EN_US')
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.

# """(PT_BR)"""
# Tuplas são usadas para armazenar vários itens em uma única variável.
# Uma tupla é uma coleção ordenada e imutável .


g = {"name": "John", "age": 36}  # dict
h = {"apple", "banana", "cherry"}  # set
i = frozenset({"apple", "banana", "cherry"})  # frozenset
j = b"Hello"  # bytes
k = bytearray(5)  # bytearray
l = memoryview(bytes(5))  # memoryview


# TEXT TYPE
print(type(x))
print("--------")

# NUMERIC TYPE
print(type(y))
print(type(a))
print(type(e))
print("--------")

# SEQUENCE TYPE
print(type(b))
print(type(f))
print(type(c))
print("--------")

# MAPPING TYPE
print(type(g))
print("--------")

# SETTING TYPE
print(type(h))
print(type(i))
print("--------")

# BOOLEAN
print(type(z))
print("--------")

# BINARY TYPES
print(type(j))
print(type(k))
print(type(i))
print("--------")

# NONE TYPE
print(type(d))
print("--------")
