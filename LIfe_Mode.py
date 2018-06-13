class Tamagotchi:
    def __init__(self):
        self.stats = {"food": 10, "happiness": 10,
                 "health": 10, "sleep": 10}
        self.sleeping = False
        self.dead = False
        self.playing = False

    #Makes sure the statistic isn't below 0 or above 10
    def constrain(self, value):
        value = min(10, value)
        value = max(0, value)
        return value

    #Constrains all the stats
    def constrain_stats(self):
        for statistic, value in self.stats.items():
            self.stats[statistic] = self.constrain(value)

    #Takes a dictionary with statistics and adds each value
    #to the tamagotchi statistics
    def apply(self, item):
        for statistic, value in self.stats.items():
            self.stats[statistic] += item[statistic]
        self.constrain_stats()

    #Takes a statistic and decreases it to zero in "full hours" time
    def decrease_to_minimum(self, statistic, full_hours, time_given):
        self.stats[statistic] -= (time_given * 10) / (full_hours * 24)

    #Takes a statistic and increases it to max in "full hours" time
    def increase_to_maximum(self, statistic, full_hours, time_given):
        self.stats[statistic] += (time_given * 10) / (full_hours * 24)

    #The function witch decreases all the stats every second
    #or is called when tamagotchi is sleeping
    def second_pass(self, seconds=1):
        "Пока происходит сон, все показатели падают, кроме сна"
        if self.is_sleeping:
            self.increase_to_maximum("sleep", 8, seconds)
            self.decrease_to_minimum("happiness", 12, seconds)
            self.decrease_to_minimum("food", 12, seconds)
        else:
            "Пока вы играете, все показатели кроме счастья, снижаются быстрее"
            if self.is_playing:
                self.decrease_to_minimum("sleep", 3, seconds)
                self.decrease_to_minimum("food", 4, seconds)
                self.increase_to_maximum("happiness", 1, seconds)
            else:
                self.decrease_to_minimum("sleep", 4, seconds)
                self.decrease_to_minimum("food", 4, seconds)
                self.decrease_to_minimum("happiness", 4, seconds)

        self.constrain_stats()

        self.random_event()

        if (self.stats["food"] == 0 or
           self.stats["health"] == 0):
           self.is_dead = True

#time.sleep(сек) - приостановить выполнение программы на заданное количество секунд.
#time.localtime([сек]) - как gmtime, но с DST флагом
