'''
Implement an Xrange iterator class whose constructor takes three arguments in the following order:

start — integer or real number
end — integer or real number
step — integer or real number, default value is 1
An Xrange iterator must generate a sequence of members of the arithmetic progression from start to end, including
start and not including end, with step step, and then raise a StopIteration exception.
'''

class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.step > 0 and self.start >= self.end:
            raise StopIteration
        elif self.step < 0 and self.start <= self.end:
            raise StopIteration
        return self.start
# Check
xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')
# Output:
# 0.0; 0.5; 1.0; 1.5; 2.0; 2.5