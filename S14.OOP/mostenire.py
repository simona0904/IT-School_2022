
# mostenirea = ne ajuta sa transmitem toate atributele, metodele, inclusiv constructorul intr-o alta clasa care o mosteneste.

class A:

    def __init__(self):
        self.count = 10

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


class B(A):            # sintaxa pt mostenire, B este derivat(copilul lui A) din A iar A este super-clasa sau parinte pt B.
    pass

b_obj = B()
print(b_obj.count)