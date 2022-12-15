


class Person():
    def __init__(self, a, n, h, b):
        self.age = a
        self.name = n
        self.hair_color = h
        self.brithday = b
    
    def happy_birthday_check(self, todays_date):
        if todays_date == self.brithday:
            self.age += 1

class Doctor(Person):
    def __init__(self, a, n, h, b, sp):
        super().__init__(a, n, h, b)
        self.specialty = sp
        
    
    

if __name__ == "__main__":
    person_amanda = Person(0, "amanda", "black", "2/25/1996")
    person_john = Person(0, "john", "brown", "4/28/1996")
    person_amanda.happy_birthday_check("12/7/2022")
    print(person_amanda.age)
    doctor_joe = Doctor(0, "joe", "brown", "4/28/1996", "neuro")
    print(doctor_joe.specialty)