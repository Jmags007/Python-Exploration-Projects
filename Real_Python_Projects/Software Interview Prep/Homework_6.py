#write out if __name__ == "__main__": 15 times
'''
if __name__ == "__main__":
if __name__ == "__mina__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
if __name__ == "__main__":
'''
'''
#individual          #group             #admin/root
   rwx                    rwx                 rwx
base2   101                     100            001
base 10   5                      4               1

chmod homework_6.py 777

'''

#gethub names: Jmags

#think of one exmaple whre a user might be lazy and want a simple set of functionalilty for a class. Ideas: calculator, eltronic store, mall
#have the class have at least 5 properties and 2 methods, 2 instaciations

#my idea: cars
#properties: type, color, miles, years old, fuel efficiency
#method1: add millage to car
#method2: change color


class Cars():
    def __init__(self, t, c, mi, ma, e):
        self.type = t
        self.color = c
        self.miles = mi
        self.make_year = ma
        self.efficiency = e
    
    def millage_update(self, trip_miles):
        self.miles = self.miles + trip_miles
    
    def color_update(self, color):
        self.color = color

if __name__ == "__main__":

    car1 = Cars("Tesla", "red", 100000, "2000", "50 mi/kW")
    car2 = Cars("Ford", "blue", 10000, "2015", "15 mi/gal")
    print(car1.miles)
    print(car2.miles)
    car1.millage_update(27)
    car2.millage_update(346)
    print(car1.miles)
    print(car2.miles)
    print(car1.color)
    print(car2.color)
    car1.color_update("yellow")
    car2.color_update("black")
    print(car1.color)
    print(car2.color)




