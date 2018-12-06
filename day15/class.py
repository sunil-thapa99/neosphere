class Car:
	pass
c = Car()
c.name = 'HAHAHAH'
# Attributes store in form of dictionary
print(c.__dict__)
c.model = 142
c.feature = 'Diesel'

f = Car()
f.name = 'FERRARI'
f.model = '1421'
f.feature = ['Petrol']
f.feature.append(c.feature)
print(f.feature)

