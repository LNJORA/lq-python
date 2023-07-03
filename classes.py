class Magari:
    def __init__(self, modelname, color, yearmade, enginecapacity):
        self.model = modelname
        self.mycolor = color
        self.myyear = yearmade
        self.myenginecc = enginecapacity
    def onyesha(self):
        print(self.model, self.mycolor, self.myyear, self.myenginecc)
#create an object
myobj = Magari("Toyota-Crown", "White", 2020, "2000cc")
myobj.onyesha()
myobj = Magari("Ford-Ranger", "lagoonblue", 2018, "4000cc")
myobj.onyesha()