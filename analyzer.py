import time

class Analyzer:
    def __init__(self,inputLength):
        self.start = 0
        self.end = 0
        self.inputLength = inputLength
    def start(self):
        self.start = time.time()
    def end(self):
        self.end = time.time()
    def result(self):
        return self.start - self.end

def timeAnalyzer():
    start = time.time()
    
    def finish():
        return round(time.time() - start)

    return finish
    

