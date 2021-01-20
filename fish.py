class Fish:

    def __init__(self, type = "X", name = "JaneDoe",weight = 1 ,color = "black"):
        self.type = type
        self.name = name
        self.weight = weight
        self.color = color

    def status(self):
       print(self.type + " type fish, " +
              self.name +
              ", weight: " + str(self.weight) + " gram"
              + ", color: " + self.color)

    def feed(self,type):
        if self.type == "clownfish" or self.type == "tang":
            self.weight += 1
        elif self.type == "kong":
            self.weight += 2
        return self.weight


class Clownfish(Fish):
    def __init__(self,type = "X", name = "JaneDoe",weight = 1 ,color = "black",color2 = "yellow"):
        super().__init__(type,name,weight,color)
        self.color2 = color2
        self.max_addon = 1

    def status(self):
        print(self.type + " type fish, " +
              self.name +
              ", weight: " + str(self.weight) + " gram"
              + ", color: " + self.color + " and " + self.color2
             )


class Tang(Fish):
    def __init__(self,type = "X", name = "JaneDoe",weight = 1 ,color = "black"):
        super().__init__(type,name,weight,color)
        self.memory = "True"
        self.max_addon = 1

    def status(self):
        print(self.type + " type fish, " +
              self.name +
              ", weight: " + str(self.weight) + " gram"
              + ", color: " + self.color
              + ", short term memory loss: " + self.memory)


class Kong(Fish):
    def __init__(self,type = "X", name = "JaneDoe",weight = 1 ,color = "black"):
        super().__init__(type,name,weight,color)
        self.max_addon = 2

    def status(self):
        print(self.type + " type fish, " +
              self.name +
              ", weight: " + str(self.weight) + " gram"
              + ", color: " + self.color)
