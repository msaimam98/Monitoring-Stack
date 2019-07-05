from person import Person
from typing import List
import logging



class Employees:
    """Initialise an Employee Catalog"""
    _workers: List[Person]

    def __init__(self):

        self._workers = []

    def add_person(self, person: Person):
        """ Add person to the Employee Catalog"""
        self._workers.append(person)
        # logging.info('{} has been added to the list of employees'.
        #              format(person.give_name()))


    def give_workers_list(self):
        """Return all of the workers """
        return self._workers


