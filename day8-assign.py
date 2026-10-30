# List Slicing new methods

elements=[10,20,30,40,50,60,70,80,90,100]

print(elements[:3])#[10,20,30]
print(elements[2:])#[30,40,50,60,70,80,90,100]
print(elements[::2])#[10,30,50,70,90]
print(elements[::-1])#[100,90,80,70,60,50,40,30,20,10]
print(elements[:])#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(elements[-1::])#[100]

# Tuple Slicing new methods

element = (10, 20, 30, 40, 50, 60, 70)

print(element[1:4])
print(element[:3])
print(element[2:])
print(element[::2])
print(element[::-1])
print(element[-4:-1])
