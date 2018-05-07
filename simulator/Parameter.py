import time


class Parameter:
    """Object of flags for interrupt requests"""

    def __init__(self, type):
        self.type = type
        if self.type == 'sma':
            self.busy = False
            self.ack = False
            self.start_time = time.time()

    def actrstart(self):
        self.busy = True
        self.start_time = time.time()

    def actrstop(self):
        self.busy = False

    def gettype(self):
        return self.type
