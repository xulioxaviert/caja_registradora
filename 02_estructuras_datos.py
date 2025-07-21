# ejemplo de listas y diccionarios
# listas
foo = [1, 2, 3, 4, 5]
print("foo:", foo)
print("foo[0]:", foo[0])
print("foo[1]:", foo[1])
print("último:", foo[-1])
# 10 métodos de listas
foo.append(6)
print("Después de append(6):", foo)
foo.remove(3)
print("Después de remove(3):", foo)
foo.insert(2, 10)
print("Después de insert(2, 10):", foo)
foo.pop()
print("Después de pop():", foo)
foo.sort()
print("Después de sort():", foo)
foo.reverse()
print("Después de reverse():", foo)
foo.extend([7, 8])
print("Después de extend([7, 8]):", foo)
foo.clear()
print("Después de clear():", foo)   
# diccionarios

bar = {"name": "John", "age": 30, "city": "New York"}
print("bar:", bar)
print("bar['name']:", bar['name'])
print("bar['age']:", bar['age'])
print("bar['city']:", bar['city'])
print(bar.keys())
