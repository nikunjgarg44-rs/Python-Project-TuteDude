#Task 1: Read a File and Handle Errors
try:
    file1 = open("Sample_File.txt", "r")
    read = file1.read()
    print(read)
    file1.close()
except FileNotFoundError:
    print("The File /'Sample_File.txt' does not exist.")
finally:
    print("The program will now exit.")


#Task 2: Write and Append Data to a File
file2 = open("output.txt", "w")
writing=file2.write(input("Enter text to write to the file: "))
print(writing)
file2.close()

file2 = open("output.txt", "a")
appending=file2.write(input("Enter text to append to the file: "))
print(appending)
file2.close()



