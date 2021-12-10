from datetime import datetime
from person import Person

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       reprod_rate, initial_infected):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        file = open(self.file_name, 'w')
        file.write(f'____________HERD IMMUNITY SIMULATION {dt_string}___________\n')
        file.write('\n')
        file.write(f'Population Size: {pop_size}\n')
        file.write(f'Initially Vaccinated: {vacc_percentage * 100}% \n')
        file.write(f'Initially Infected: {initial_infected}\n')
        file.write(f'Virus: {virus_name}\n')
        file.write(f'Mortality Rate: {mortality_rate}\n')
        file.write(f'Reproduction Rate: {reprod_rate}\n')
        file.write('\n')
        file.write(f'_____________________________________________________________')
        file.close()



    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        file = open(self.file_name, 'a')
        if random_person_sick:
            file.write(f'{person._id} did not infect {random_person._id} because they are already infected.\n')
        elif random_person_vacc:
            file.write(f'{person._id} did not infect {person._id} because they were vaccinated.\n')
        else:
            file.write(f'{person._id} infected {random_person._id}\n')
        file.close()

    def log_infection_survival(self, person, survived_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        file = open(self.file_name, 'a')
        survived = f'{person._id} survived infection\n'
        deceased = f'{person._id} deceased due to infection\n'
        file.write(survived if survived_infection else deceased)
        file.close()


    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass
    def log_summary(self, total_living, total_dead, total_vacc, number_interactions, vacc_interactions, death_interactions):
        file = open(self.file_name, 'a')
        file.write('\n')
        file.write(f'----------------------END OF SIMULATION----------------------\n')
        file.write(f'Total living: {total_living}\n')
        file.write(f'Total dead: {total_dead}\n')
        file.write(f'Number of vaccinations: {total_vacc}\n')
        file.write(f'Total number of interactions: {number_interactions}\n')
        file.write(f'Number of interactions resulting in vaccination: {vacc_interactions}\n')
        file.write(f'Number of interactions resulting in death: {death_interactions}\n')
        file.close()

        
if __name__ == '__main__':
    myLogger = Logger('answers.txt')   