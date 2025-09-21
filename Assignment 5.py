#Task 1: Create a Dictionary of Student Marks
try:
    Dict = {}
    for i in range(int(input("How many students yor want to add? "))):
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        Dict[key] = value
    print(Dict)
    print(Dict[input("Enter Student Name: ")])
except KeyError:
    print("Student not found")
finally:
    print("The program has ended")


#Task 2: Demonstrate List Slicing

L=[i for i in range(1,11)]
print("ORIGINAL LIST: ",L)
Y=L[0:5]
print("EXTRACTED FIRST FIVE ELEMENTS: ",Y)
Y.reverse()
print("REVERSE EXTRACTED ELEMENTS: ",Y)