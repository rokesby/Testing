# File: lib/present.py

class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents


'''
Test creation of the class and check that no contents have been wrapped.
Add contents and try to wrap again.
Try to unwrap a present with no contents
'''