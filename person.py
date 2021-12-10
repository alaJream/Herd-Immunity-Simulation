import random
random.seed(42)
from virus import Virus


class Person(object):
    def __init__(self, _id, is_vacc, infection=None):
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vacc = is_vacc  # boolean
        if infection is not None:
            self.infection = infection  # Virus object or None
        else:
            self.infection = None

    def did_survive_infection(self):
        if self.infection is not None:
            survivalRate = random.random
            if survivalRate > self.infection.mortality_rate:
                return True
            else:
                return False
        #     randNum = random.uniform(0,1)
        #     if (randNum < self.infection.mortality_rate):
        #         # died from infection
        #         self.is_alive = False
        #         self.infection = False
        #         return self.is_alive
        #     else:
        #         #survived and immune
        #         self.is_vaccinated = True
        #         self.infection = None
        # return self.is_alive



''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vacc is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    assert person._id == 2
    assert person.is_alive == True
    assert person.is_vacc == False
    assert person.infection != None


def test_sick_person_instantiation():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(3, False, virus)
    assert person._id == 3
    assert person.is_vacc == False
    assert person.infection == virus


def test_did_survive_infection():
    virus = Virus("Dysentery", 0.7, 0.2)
    person = Person(4, False, virus)
    survived = person.did_survive_infection()
    if survived:
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert person.infection is None
    else:
        assert person.is_alive is False
        assert person.is_vaccinated is False
        assert person.infection is not None

if __name__ == "__main__":
    test_vacc_person_instantiation()
    test_not_vacc_person_instantiation()
    test_sick_person_instantiation()
    test_did_survive_infection()
   
