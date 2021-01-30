class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('enter the value and press Enter - '))
                self.my_list.append(val)
                print(f'current list  - {self.my_list} \n ')
            except:
                print(f"invalid value ")
                choice = input(f'try again? Y/N ')

                if choice.lower() == 'y':
                    print(try_except.my_input())
                elif choice.lower() == 'n':
                    break
                else:
                    break
try_except = Error(1)
print(try_except.my_input())