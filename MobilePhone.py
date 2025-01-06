class MobilePhone:
    def __init__(self, brand, model, color, battery=100, is_vip:bool=False): # ctor
        print('__init__ is running')  # will run every time i create a new phone
        self.brand = brand  # this variable will stay in the mobile phone...
        self.model = model
        self.color = color
        self.battery = battery
    def ring(self) -> None:
        print(f'{self.brand} {self.model} is ringing')

my_iphone = MobilePhone('IPhone', '16 PRO', 'white', 79)  # new devicde created. __init__ is called auto
print(my_iphone.brand)
# print(my_iphone.__dict__)
my_iphone.ring()

friend_galaxy = MobilePhone('Galaxy', 'S20', 'Black')  # new devicde created. __init__ is called auto
# print(friend_galaxy.__dict__)
friend_galaxy.ring()

type(friend_galaxy)