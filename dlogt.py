from person import Person
from Employees import Employees
import logging
import sys
# import random

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')


# root = logging.getLogger()
# # filename='logg/data.log', level=logging.DEBUG
# root.
# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
# handler.setFormatter(formatter)
# root.addHandler(handler)


logging.basicConfig(filename='logg/data.log'
                    , format='%(asctime)s:%(name)s:%(message)s',
                    level=logging.DEBUG)
root = logging.getLogger()
# this just gets the logging portion
# format='%(asctime)s:%(name)s:%(message)s',
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
handler.setFormatter(formatter)
# so the handler that is added has to be formatted in the way the maintainer
# wants the logs to flow through
root.addHandler(handler)

handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
handler.setFormatter(formatter)
# so the handler that is added has to be formatted in the way the maintainer
# wants the logs to flow through
root.addHandler(handler)

PEOPLE = []
for i in range(400):
    PEOPLE.append('John')


def lay_out_day(person3: str):
    """ lay out the day for each person """

    # all_workers = employee_catalog.give_workers_list()
    days = len(PEOPLE)
    finish = False
    day = 1
    root.info('name of employee: {}'.format(person3))
    # person_working = all_workers[]
    while not finish:
        if day <= days:
            person2 = Person(person3)
            root.info('day {}'.format(day))
            root.info('Start of day')
            entrance_time = person2.give_entry_time()
            root.info('Entry time: {}'.format(entrance_time))
            break_length = person2.give_breaks()
            break_time = person2.give_break_time()
            hours_worked = person2.give_hours()
            break_end_time = person2.give_break_end_time()
            if break_length == 0:
                    root.error('break lenghth not 0')
                    root.info(
                        '{} took no break'.format(person2.give_name()))
                    root.info('{} hours worked'.format(hours_worked))
            else:
                root.info('break start time: {}'.format(break_time))
                root.info('break length: {} hours'.format(break_length))
                root.info('break end time: {}'.format(break_end_time))
                root.info('total hours worked: {}'.format(hours_worked))
            root.info('End of day')
            day += 1
        else:
            finish = True
            root.info('Day400')

if __name__ == '__main__':

    employee_catalog = Employees()
    person1 = Person('Jenni')
    employee_catalog.add_person(person1)
    for guy in employee_catalog.give_workers_list():
        lay_out_day(guy.give_name())




