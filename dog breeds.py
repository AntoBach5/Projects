class DogBreed:
    def __init__(self, breed, colour, characteristics):
        self.breed = breed
        self.colour = colour
        self.characteristics = characteristics

labrador = DogBreed("labradors", "yellow", "friendly, energetic")
husky = DogBreed("huskys", "grey & white", "sporty, from cold places")
beagle = DogBreed("Beagles", "brown, white & black", "curious, messy")

print(f"{labrador.breed} are {labrador.colour} and {labrador.characteristics}")
print(f"{husky.breed} are {husky.colour} and {husky.characteristics}")
print(f"{beagle.breed} are {beagle.colour} and {beagle.characteristics}")