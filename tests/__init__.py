import unittest


class ManualClock:
    def __init__(self):
        super(ManualClock, self).__init__()
        self.now = 0

    def add(self, value):
        self.now = self.now + value

    def time(self):
        return self.now

    def time_string(self):
        return str(int(round(self.time())))


class TimedTestCase(unittest.TestCase):
    clock = ManualClock()
