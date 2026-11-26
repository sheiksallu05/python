import time
import threading

def std_details():
    for i in range(101,106):
        time.sleep(1)
        print("Student Roll No",i)

marks = [85, 90, 75, 80, 95]

def std_marks():
    for mark in marks:
        time.sleep(1.2)
        print("Student Mark",mark)


t1 = threading.Thread(target=std_details)
t2 = threading.Thread(target=std_marks)

t1.start()
t2.start()


