### Over loading 

class test:
    def data(self):
        print('this is new program')


    def __add__(self,no):
        print(no + 100)


t = test()

print(t + 100)