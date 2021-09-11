#Animal Shelter

class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal , type):
        if type == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats)==0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat
    
    def dequeueDog(self):
        if len(self.dogs)==0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog


    def dequeueAny(self):
        if len(self.cats)==0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result

        

customQueue = AnimalShelter()
customQueue.enqueue('Cat1', 'cat')
customQueue.enqueue('Cat2','cat')
customQueue.enqueue('Dog1', 'dog')
customQueue.enqueue('Cat3', 'cat')
customQueue.enqueue('Dog2', 'dog')
print(customQueue.dequeueDog())
print(customQueue.dequeueCat())
print(customQueue.dequeueAny())