import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        self.logger = Logger("answers.txt")
        self.population =  self._create_population(initial_infected)
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        self.time_step_counter = 1
        self.num_interactions = 0
        self.vacc_interactions = 0
        self.death_interactions = 0

    def _create_population(self, initial_infected):
        new_population =[]
        left_to_infect = initial_infected
        left_to_vacc = int(self.vacc_percentage * self.pop_size)
        self.vacc = left_to_vacc
        for index in range(self.pop_size):
            if left_to_vacc > 0:
                new_population.append(Person(index, True, None))
                left_to_vacc -= 1
            elif left_to_infect > 0:
                new_population.append(Person(index, False, self.virus))
                left_to_infect -= 1
            else:
                new_population.append(Person(index, False, None))
        return new_population

    def _simulation_should_continue(self):
        total_accounted_for = self.total_dead + self.vacc
        if total_accounted_for == self.pop_size:
            self.logger.endLog("The simulation is ending because everyone has either received the vaccine or has deceased.")
            return False
        elif len(self.newly_infected) == 0:
            self.logger.endLog("The simulation has ended because Herd Immunity has been reached!")
            return True

    def run(self):
        time_step_counter = 0
        should_continue = True
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.reprod_rate)

        while should_continue:
            self.time_step()
            should_continue = self._simulation_should_continue()
            self._infect_newly_infected()
            self.time_step_counter += 1
        print('The simulation has ended after {self.time_step_counter} turns.'.format(time_step_counter))
        
    def log_everyone(self):
        for person in self.population:
            print(person._id, 'infected: ', person.infection, ' alive: ', person.is_alive, ' vaccinated: ', person.is_vacc)


    def time_step(self):
        deceased_this_round = 0
        newly_vacc = 0

        for person in self.population:
            if person.is_alive:
                if person.infection is not None:
                    interaction_counter = 0
                    while interaction_counter < 100:
                        random_person = random.choice(self.population)
                        while random_person.is_alive is False:
                            random_person = random.choice(self.population)
                        self.interaction(person, random_person)
                        interaction_counter += 1
                    if person.survivors() is False:
                        self.total_dead += 1
                        deceased_this_round += 1
                        self.current_infected -= 1
                        person.is_alive = False
                    else:
                        self.vacc += 1
                        newly_vacc += 1
                        self.current_infected -= 1
                        person.infection = None
                        person.is_vacc = True

        self.logger.log_time_step(self.time_step_counter, deceased_this_round, newly_vacc, self.current_infected, self.total_dead, self.pop_size, self.vacc)

    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True

        infection = True

        if random_person.is_vacc:
            pass
        elif random_person.infection is not None:
            pass
        elif random_person._id in self.newly_infected:
            pass
        else:
            immune_strength = random.random()
            if immune_strength < self.virus.reprod_rate:
                self.newly_infected.append(random_person._id)
                self.total_infected += 1
                self.current_infected += 1
                return
        
    def _infect_newly_infected(self):
        for id in self.newly_infected:
            for person in self.population:
                if person._id == id:
                    person.infection = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    reprod_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, reprod_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
    # virus = Virus("covid", 0.9, 0.5)
    # sim = Simulation(virus, 10000, 0.10, 6)
    # sim.run()