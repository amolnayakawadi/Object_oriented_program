
class bank:


    name = 'Tempo bank' 


    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.balance = 0
        self.transation = []

    def get_balance(self):
        print(f'{self.name} your balance is {self.balance}')


    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transation.append(('DEPOSIT',amount,self.balance))
        self.get_balance

    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            self.transation.append(('WITHDRAW',amount,self.balance))
            self.get_balance
        else:
            print('Unsufficient balance')


    def print_name(self):
        width = 43
        head = '-' * width
        name = 'S.No | Transation type | Amount | Balance'
        print(head+'\n'+name+'\n+head')


    def get_passbook(self,entries=5):
        sno = 0
        for i in self.transation:
            if sno <= entries:
                ttype = i[0]
                amt = i[1]
                bal = i[2]
                print(f'{sno}   |   {ttype}   |   {amt}   |   {bal}')
                sno+=1
            else:
                break





b = bank('amol','pune')
b.get_balance()
b.get_passbook(1)

b.deposit(1000)

        

                           
