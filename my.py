#classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' ' + ' is walking')
        print('hello my name is ' + self.name + ' ' + ' i am ' + str(self.age) + ' ' + ' years old')

peligah = Person('peligah', 20)
haq = Person('haq', 12)

print(peligah.name + ' ' + str(peligah.age))
print(haq.name + ' ' + str(haq.age))

peligah.walk()
haq.walk()