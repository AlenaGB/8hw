class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'device model': self.name, 'price per unit': self.price, 'quantity': self.quantity}
    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'

    def reception(self):
        try:
            unit = input(f'enter product ')
            unit_p = int(input(f'enter price per unit '))
            unit_q = int(input(f'enter the product quantity '))
            unique = {'device model': unit, 'price per unit': unit_p, 'quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'current list -\n {self.my_store}')
        except:
            return f'error'

        print(f'exit - Q, continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'entire list -\n {self.my_store_full}')
            return f'exit'
        else:
            return StoreMashines.reception(self)
class Printer(StoreMashines):
    def to_print(self):
        return f' print  {self.numb} times'

class Scanner(StoreMashines):
    def to_scan(self):
        return f' scan {self.numb} times'

class Copier(StoreMashines):
    def to_copier(self):
        return f' copier  {self.numb} times'

unit_1 = Printer('hp', 5700, 4, 8)
unit_2 = Scanner('kyocera', 19000, 1, 12)
unit_3 = Copier('Xerox', 1300.4, 3, 4)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())