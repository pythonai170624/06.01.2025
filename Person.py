class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # override
    def __str__(self):
        # return f"Person [fname = {self.fname} lname = {self.lname}]"
        # return f"class Person, {self.fname} {self.lname}"
        return f"{self.fname} {self.lname}"

    def __len__(self):
        return len(self.fname + self.lname) + 1

    def __repr__(self):
        return f"Person('{self.fname}', '{self.lname}')"

danny = Person('dany', 'shovevani')
moshe = Person('moshe', 'ufnik')

print(danny)
print(moshe.__str__())

print('[moshe, danny] = ', [moshe, danny])
print('[len] danny = ', danny, '=', len(danny))
print(danny.__dict__)
print(repr(danny))

danny2 = Person('dany', 'shovevani')
