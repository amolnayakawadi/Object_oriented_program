## Inheritance

class parent1:
    def test(self):
        print('This is test from parent1')

class parent2:
    def test(self):
        print('This is test from parent2')


class child(parent2,parent1):
    def test1(self):
        print('This is test1 from child')

    def test2(self):
        print('This is test2 from child')


c = child()

c.test1()
c.test()