# IDEA: Each node is a tuple, with the first element of the tuple being the value itself, and 
#       the second value being the minimum at that point

class MinStack:

    def __init__(self):
        self.values = []


    def push(self, val: int) -> None:
        if len(self.values) == 0:
            self.values.append((val, val))
        else:
            self.values.append((val, min(val, self.values[-1][1])))

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1][0]

    def getMin(self) -> int:
        return self.values[-1][1]
