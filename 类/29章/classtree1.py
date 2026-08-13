class Employee: pass
class Person(Employee): pass
pat = Person()
import classtree
classtree.instancetree(pat)