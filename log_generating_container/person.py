from datetime import datetime
import random


class Person:

    """Initialise a new person in the company"""
    _time: datetime
    _hours: int
    _name: str
    _breaks: int
    _break_start_time: datetime
    _break_end_time: datetime

    def __init__(self, name: str):

        self._name = name
        self._hours = random.randint(1, 9)
        self._breaks = 9 - self._hours
        self._break_start_time = datetime(2019, 6, 23, 17 - self._breaks)
        self._break_end_time = datetime(2019, 6, 23, 17)
        # if self._breaks > 2:
        #     self.good = False
        # else:
        #     self.good = True
        self._time = datetime(2019, 6, 23, 9)

    def give_breaks(self):
        """Return breaks taken"""
        return self._breaks

    def give_hours(self):
        """Return hours worked of person"""
        return self._hours

    def give_name(self):
        """ Return the name of person"""
        return self._name

    def give_break_time(self):
        """Return good or bad"""
        return self._break_start_time

    def give_break_end_time(self):
        """Return break end time"""
        return self._break_end_time

    def give_entry_time(self):

        return self._time





