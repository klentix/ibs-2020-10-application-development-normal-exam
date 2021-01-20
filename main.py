from fish import Fish,Clownfish,Tang,Kong
from aquarium import Aquarium

def main():


    dory = Tang("tang", "doreeee", 6, "blue")
    dory.feed("tang")
    dory.status()

    nemo = Kong("kong", "nemo", 3, "red")
    nemo.status()
    nemo.feed("kong")
    nemo.feed("kong")
    nemo.status()

    clown = Clownfish("clownfish","joker",4,"purple")
    clown.status()
    clown.feed("clownfish")
    clown.status()

    aquarium = Aquarium("Underworld")
    aquarium.addFish(dory)
    aquarium.addFish(nemo)
    aquarium.addFish(clown)
    aquarium.get_status()
    aquarium.feed(20)
    dory.status()
    clown.status()
    nemo.status()
    aquarium.feed(10)
    dory.status()
    clown.status()
    nemo.status()
    aquarium.removeFish()
    aquarium.get_status()

if __name__ == "__main__":
    main()