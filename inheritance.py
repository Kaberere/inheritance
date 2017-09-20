import csv


class School:

    def __init__(self, EITs, fellows):
        self.EITs = EITs
        self.fellows = fellows


class EITs (School):

    def __init__(self, names, nationalities, tech_fun_fact):
        self.names = names
        self.nationalities = nationalities
        self.tech_fun_fact = tech_fun_fact

    def names(self):
        return self.names

    def nationalities(self):
        return self.nationalities

    def tech_fun_fact(self):
        return self.tech_fun_fact

    def __str__(self):
        return"My name is %s, from %s and a fun fact in tech class is that %s" % (self.names, self.nationalities, self.tech_fun_fact)

eit1 = EITs("Eve", "Kenya", "Tech is awesome")
print(eit1)
eit2 = EITs("Bright", "Nigeria", "Python is bae")
print(eit2)


class fellows (School):

    def __init__(self, names, nationalities, happiness_level=10):
        self.names = names
        self.nationalities = nationalities
        self.happiness_level = happiness_level

    def names(self):
        return self.names

    def nationalities(self):
        return self.nationalities

    def eating(self):
        fellow1.happiness_level += 1
        return self.happiness_level

    def teaching(self):
        fellow2.happiness_level -= 1
        return self.happiness_level

    def __str__(self):
        return "I am a fellow at MEST and my name is %s, from %s and my happiness level is %s;" % (self.names, self.nationalities, self.happiness_level)

fellow1 = fellows("Andrew Berkowitz", "USA")
fellow1.eating()
print(fellow1)

fellow2 = fellows("Edem", "Ghana")
fellow2.teaching()
print(fellow2)


class Person:

    def __init__(self, names, nationalities):
        self.names = names
        self.nationalities = nationalities


class EITs(Person):

    def __init__(self, names, nationalities, tech_fun_fact):
        super().__init__(names, nationalities)
        self.tech_fun_fact = tech_fun_fact


class fellows(Person):

    def __init__(self, names, nationalities, happiness_level):
        super().__init__(names, nationalities)
        self.happiness_level = happiness_level


with open('eits.csv', 'r') as file:
    nationalities = ['Kenyan', 'Nigerian', 'Ivorian',
                     'South African', 'Ghanaian', 'Zimbabwe']
    tracker = 0
    for line in file:
        if tracker == 0:
            tracker += 1
            continue
        eit = line.strip('\n').split(',')
        if eit[1] in nationalities:
            print(eit)
        else:
            raise ValueError("Invalid nationality of EIT")
