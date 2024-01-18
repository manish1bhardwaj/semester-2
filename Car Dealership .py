class car:
    def __init__(self,name,model,maker,year,price,color):
       self.name  = name
       self.model = model
       self.maker = maker
       self.year = year
       self.price = price
       self.color = color
       self.available_car = True
    def display_car(self):
           return(f'''Name:{self.name},
Model:{self.model},
Maker:{self.maker},
Year:{self.year},
Price:{self.price},
Color:{self.color}''')
       

class dealership:
    def __init__(self,dealer_name):
        self.dealer_name = dealer_name
        self.inventory = []
    def add_car_to_inventory(self,car):
        self.inventory.append(car)    
    def display_available_car(self):
        count =1
        for car in self.inventory:
            if car.available_car:
                print(count)
                print(car.display_car())
                print('--------------\n')
                count+= 1

    def sell_car(self,c,index):
        if 0 <index<len(self.inventory) and self.inventory[index-1].available_car:
            c.purchase(self.inventory[index-1])
            return self.inventory[index-1]

class costomer:
    def __init__(self,name):
        self.name = name
        self.purchase_car = []
    def purchase(self,car):
        self.purchase_car.append(car)
        car.available = False
        

#main code
       
car1 = car('Mustang-GT','678','Ford',2024,50000000,'Black')
car2 = car('Lamborgini','563','Lamborgini',2024,40000000,'Black')
car3 = car('Alto','800','Maruti suzuki',2023,500000,'Black')

d1 = dealership('TATA MOTORS')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)

d1.display_available_car()


c1 = costomer(input('Enter costumer name :'))
car_num = int(input('Enter car number :' ))
ret = d1.sell_car(c1,car_num)
if ret:
    print(f'{c1.name}Purchased car\n{ret.display_car()}')
else:
    print('Not available for selling')
print('\n\nAfter selling... Available car :')
d1.display_available_car()

