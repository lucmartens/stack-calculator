class StackUnderflow(Exception):
    pass


class Stack(object):
    def __init__(self, data=[]):
        self.data = data

    def peek(self):
        if len(self.data) < 1:
            raise StackUnderflow
        return self.data[-1]

    def pop(self, n=1):
        if len(self.data) < n:
            raise StackUnderflow
        result = [self.data.pop() for _ in range(n)]
        return result if len(result) > 1 else result[0]

    def push(self, n):
        self.data.append(n)
        return n

    def add(self):
        n1, n2 = self.pop(2)
        return self.push(n2 + n1)

    def subtract(self):
        n1, n2 = self.pop(2)
        return self.push(n2 - n1)

    def multiply(self):
        n1, n2 = self.pop(2)
        return self.push(n2 * n1)

    def divide(self):
        n1, n2 = self.pop(2)
        return self.push(n2 / n1)
