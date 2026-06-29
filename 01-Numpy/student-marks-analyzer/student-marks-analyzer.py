import numpy as np

names = list()
marks = list()

with open("student.txt" , "r") as f:
    for line in f:
        name , mark = line.strip().split(",")
        names.append(name)
        marks.append(int(mark))


marks = np.array(marks)
print("Student Report\n")
for name , mark in zip(names,marks):
    print(f"{name}:{mark}")

print("\nAverage:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

print("\nStudents scoring above 80:")

for name, mark in zip(names,marks):
    if mark > 80:
        print(f"{name}:{mark}")
