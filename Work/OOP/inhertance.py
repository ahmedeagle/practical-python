class animal:
    #Python supports multiple inheritance directly.

    def speak(self):
        return "I am an animal"
    
class dog(animal):
    
    def bark(self):
        return "I am a dog"
    
class cat(animal):
    
    def bark(self):
        return "I am a cat"    
    
class human(animal):
    def speakdd(self):
        return "I am a human"   
    
dog1 = dog()
human1 = human()
print(human1.speak())
print(dog1.speak())
print(dog1.bark())    