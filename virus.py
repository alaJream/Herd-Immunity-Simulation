class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, reprod_rate, mortality_rate):
        self.name = name
        self.reprod_rate = reprod_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.reprod_rate == 0.8
    assert virus.mortality_rate == 0.3
