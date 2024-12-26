def readfile(file, len):
    with open(file, 'r') as file:
        for line in file:
            yield line[:len]

file = 'gen.txt' 
len = 4 
for line in readfile(file,len):
    print(line)
