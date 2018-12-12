# Python Dictionary

# Example_01

a = {'name': "Deborah", 'birth': '1128', 'age': '30'}

print(a.keys())

# Example_03
b = {'A': 90, 'B': 80, 'C': 70}

result = b.pop('B')
print(a)

print(result)

# Example_04

c = {'A':90, 'B':'80'}

#dic.get(ket,default)
print(c.get('C',70))

# Example_05

min(b.values())


# Example_06

#  a = {'A':90, 'B':80, 'C':70} to [('A', 90), ('B', 80), ('C', 70)]

b = list(b.items())

print(b)
