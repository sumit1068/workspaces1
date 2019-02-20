class Person(object):

    # Constructor
        def __init__(self, id,name,designation):
            self.id = id
            self.name = name
            self.designation = designation


        # To get name

        def getEmployee(self):
            return self.id+'_'+self.name+'_'+self.designation

        # To check if this person is employee
        def putAllObjectInDictionary(self):
            return self.id+'_'+self.name+'_'+self.designation

# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp1 = Person('11',"sumit",'Lead')  # An Object of Person
emp2 = Person('12',"amit",'developer')
emp3 = Person('13',"jyoti",'trster')
emp4 = Person('14',"sunil",'mamager')
mydict={emp1.id:emp1.designation+':'+emp1.name,emp2.id:emp2.designation+':'+emp2.name,emp3.id:emp3.designation+':'+emp3.name,emp4.id:emp4.designation+':'+emp4.name}
print(emp1.getEmployee())
print(emp2.getEmployee())
print(emp3.getEmployee())
print(emp4.getEmployee())
print("<--------Printing from dictionary----->")
print(mydict.get(emp1.id))
print(mydict.get(emp2.id))
print(mydict.get(emp3.id))
print(mydict.get(emp4.id))

