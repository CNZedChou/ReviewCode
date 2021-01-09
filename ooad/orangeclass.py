class Orange:
    '''A blueprint for making many oranges'''
    def __init__(self,weight,orchard,date_picked):
        self.weight = weight
        self.orchard = orchard
        self.date = date_picked

    def __str__(self):
        return 'Orange Info: %.2f libs picked on %s from %s ' %(self.weight,self.date,self.orchard)


cheap_orange = Orange(0.08,'Yiwu','2018-12-01')
print(cheap_orange)
expense_orange = Orange(0.12,'Jinhua','2018-11-29')
print(expense_orange)
print(cheap_orange.__dict__)
print(Orange.__dict__)
'''
Orange Info: 0.08 libs picked on 2018-12-01 from Yiwu 
Orange Info: 0.12 libs picked on 2018-11-29 from Jinhua 
{'date': '2018-12-01', 'orchard': 'Yiwu', 'weight': 0.08}
{'__module__': '__main__', '__str__': <function Orange.__str__ at 0x00000123722A3378>, '__init__': <function Orange.__init__ at 0x000001236F352BF8>, '__weakref__': <attribute '__weakref__' of 'Orange' objects>, '__dict__': <attribute '__dict__' of 'Orange' objects>, '__doc__': 'A blueprint for making many oranges'}

'''