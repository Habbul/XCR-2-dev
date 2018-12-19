import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, func, arg):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.func = func
        self.arg = arg

    def run(self):
        self.func(self.arg)
