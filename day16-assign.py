
# write a code to implement multi level inheritance

class Signal1:
    def stop(self):
        print("RED")


class Signal2(Signal1):
    def ready(self):
        print("YELLOW")


class Signal3(Signal2):
    def go(slef):
        print("GREEN")


obj = Signal3()

obj.stop()
obj.ready()
obj.go()

# write a code to implement multiple inheritance

class Signal1:
    def stop(self):
        print("RED")


class Signal2:
    def ready(self):
        print("YELLOW")


class Signal3(Signal1,Signal2):
    def go(slef):
        print("GREEN")


obj = Signal3()

obj.stop()
obj.ready()
obj.go()
