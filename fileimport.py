'''This script contains commands for opening, writing and
appending to files.
Do not run script without fixing the snippets'''

filename = 'karan.txt'
#opening and reading files
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

#for writing to the file
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

#for appending to the file
with open(filename, 'a') as file_object:
    file_object.write("\nI love making games.")