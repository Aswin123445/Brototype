class Home:
    def __init__(self,door,chairs,tv,fridge,stove,washingmichine,table,):
        self.door=door
        self.chairs=chairs
        self.tv=tv
        self.fridge=fridge
        self.stove=stove
        self.washingmichine=washingmichine
        self.table=table
    def room(self,width,height,bed):
        self.width=width
        self.height=height
        self.bed=bed
        print("room can be used to sleep")
    def sitout(self,sitting_area):
        self.sitting_area=sitting_area
        print("sitting area is used to sit in the outside of the room")
#putting inheritance to it
class FirstHome(Home):
    def study_room():
        print("this room as an extra study room")

class SecondHome(Home):
    def work_area(self):
        print("work area is seen outside the kitchen")
home=SecondHome("wood","big chair","panasonic","sony","butterfly","sony","table")
#calling the parent class

home.sitout(23)
home.room(20,30,2)
    