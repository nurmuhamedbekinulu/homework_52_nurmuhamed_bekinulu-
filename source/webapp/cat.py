import random

class Cat():
    def __init__(self, name='nameless'):
        self.name = name
        self.age = self.age_rand()
        self.satiety = self.satiety_lvl()
        self.happines = self.happines_lvl()
        self.awake_status = True

    def age_rand(self):
        min_age = 1
        max_age = 20
        return random.randint(min_age, max_age)

    def satiety_lvl(self):
        cat_satiety = random.randint(20, 40)
        return cat_satiety

    def happines_lvl(self):
        cat_happines = random.randint(20, 40)
        return cat_happines
    
    def play(self):
        if self.awake_status == False:
            self.happines = self.happines - 5
            self.awake_status = True
        else:
            self.happines = self.happines - 10
            if random.randint(1, 3) == 1:
                self.happines = 0
            else:
                self.happines = self.happines + 15
    
    def feed(self):
        if self.satiety >= 100:
            self.happines = self.happines - 30
        if self.awake_status == False:
            return 'Спящего кота нельзя покормить.'
        else:
            self.satiety = self.satiety + 15
            self.happines = self.happines + 5
    
    def sleep(self):
        self.awake_status = False