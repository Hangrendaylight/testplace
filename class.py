#dict
from datetime import date
class dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    def call_out(self):
        return f"{self.name} is barking"
    def human_year(self):
        return self.age*7
    def dog_info(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old"
d1=dog("Rex","Keple",4)
d2=dog("Bonke","Chihuahua",2)
print (d1.name)
print (d2.call_out())
print(f"{d1.name} is",d1.human_year(),f"{d2.name} is",d2.human_year())
print(d1.dog_info())
print(d2.dog_info())
today=date.today()
print("today is",today)
meeting_date=date(2026,7,10)
print("meeting date is",meeting_date)
class Booking:
    def info(self,room_name:str,Date:date,time:str):
        self.room_name=room_name
        self.Date=Date
        self.time=time
booking1=Booking("A101",date(1758,7,4), "10:00 AM")
print(f"Booking info: Room {booking1.room_name} on {booking1.Date} at {booking1.time}")