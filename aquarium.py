from fish import Fish, Tang, Kong, Clownfish

class Aquarium:

    def __init__(self,name):
        self.name = name
        self.fishes = []

    def addFish(self,Fish): # add on fish
        self.fishes.append(Fish)
        return self.fishes

    def removeFish(self): # remove if fish weighs at least 11gram
        for i in self.fishes:
            if i.weight >= 11:
                self.fishes.remove(i)
                return self.fishes

    def feed(self,num):
        for i in self.fishes:
            if i.type == "clownfish" or i.type == "tang":
                i.weight += i.max_addon  # feed according to weight gain
                print("Feed " + i.type + " " + str(i.max_addon) + " gram of food.")

            elif i.type == "kong":
                i.weight += i.max_addon # feed according to weight gain
                print("Feed " + i.type + " " + str(i.max_addon) + " gram of food.")


    def get_status(self):
        for i in self.fishes:
            print ("Aquarium has: type: " + i.type
                   + " name: " + i.name
                   + " weight: " + str(i.weight) + " gram")


