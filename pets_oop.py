class Pets:
    name = 'Josh'
    age = 2
    age_scale = 7
    human_scale_age = age * age_scale
    communication = 'some noise'

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
