# implement virtual and abstract function using any custom requirement

# Virtual Function

class SLAclasses:
    def classes(self):
        print("SLA class is starting")


class Communication(SLAclasses):
    def start(self):
        print("Communication class is starting")


class Aptitude(SLAclasses):
    def start(self):
        print("Aptitude class is starting")


c = Communication()
a = Aptitude()

c.start()
a.start()

# -----------------------------------------------------------------

# Abstract Function

from abc import ABC, abstractmethod

class Students(ABC):

    @abstractmethod
    def stdwork(self):
        pass

class OfflineStudents(Students):
    def stdwork(self):
        print("Offline Students")

class  OnlineStudents(Students):
    def stdwork(self):
        print("Online Students")

off = OfflineStudents()
on = OnlineStudents()

off.stdwork()
on.stdwork()
