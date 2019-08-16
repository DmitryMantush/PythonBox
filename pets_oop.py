class Pets:
    def __init__(self, name, age, age_scale, human_scale_age, communication):
        self.name = 'Josh'
        self.age = 2
        self.age_scale = 7
        self.human_scale_age = age * age_scale
        self.communication = 'some noise'

    def feed(self):
        return self.communication

    def set(self, name, age, communication):
        self.name = name
        self.age = age
        self.communication = communication


class Cats(Pets):

    age_scale = 5
    communication = 'meow'


class Dogs(Pets):
    age_scale = 7
    communication = 'woof'


Spike = Dogs()
Spike.set(Spike, 3, 'woof-woof')


Bomber = Cats()

print(Spike.feed())
print(Bomber.feed())
