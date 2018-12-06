# Immutable => If updated, any object's value; all the assigned object  
# changes its value as they point to same address in the memory.
# Mutable => If updated, any object's value; just the changed object's value
# changes, as they point different address in the memory
a = [1, 2, 3]
b = a
c = b
print('b => ' + hex(id(b)))
print('a => ' + hex(id(a)))
print('c => ' + hex(id(c)))
b.append(9)
print(b)
print(c)
print(a)
print('<--------- After changing ------------->')
print('b => ' + hex(id(b)))
print('a => ' + hex(id(a)))
print('c => ' + hex(id(c)))

s = 'Sunil'
t = s
u = t
print('<--------- String changing ------------->')
print('s => ' + hex(id(s)))
print('t => ' + hex(id(t)))
print('u => ' + hex(id(u)))
t = 'Thapa'
print('<--------- String After changing ------------->')
print('s => ' + hex(id(s)))
print('t => ' + hex(id(t)))
print('u => ' + hex(id(u)))