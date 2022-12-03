"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = {}
        for key, value in kwargs.items():
            self.kwargs[key] = value
        


    def get_pay(self):
        pay = 0
        if 'salary' in self.kwargs:
            pay = self.kwargs['salary']
        elif 'hours' in self.kwargs and 'rate' in self.kwargs:
            pay = self.kwargs['hours'] * self.kwargs['rate']

        if 'bonus' in self.kwargs:
            pay += self.kwargs['bonus']
        elif 'commissions' in self.kwargs and 'commission_pay' in self.kwargs:
            pay += self.kwargs['commissions'] * self.kwargs['commission_pay']
        
        return pay

    def __str__(self):
        extra = ''
        if 'salary' in self.kwargs:
            pay_type = 'monthly salary'
            base_pay = self.kwargs['salary']
        elif 'hours' in self.kwargs and 'rate' in self.kwargs:
            pay_type = 'contract'
            base_pay = '{} hours at {}/hour'.format(self.kwargs['hours'], self.kwargs['rate'])
        if 'bonus' in self.kwargs:
            extra = ' and receives a bonus commission of {}'.format(self.kwargs['bonus'])
        elif 'commissions' in self.kwargs and 'commission_pay' in self.kwargs:
            extra = ' and receives a commission for {} contract(s) at {}/contract'.format(self.kwargs['commissions'], self.kwargs['commission_pay'])

        return '{} works on a {} of {}{}. Their total pay is {}.'.format(self.name, pay_type, base_pay, extra, self.get_pay())



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, commissions=4, commission_pay=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, rate=25, commissions=3, commission_pay=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, rate=30, bonus=600)
