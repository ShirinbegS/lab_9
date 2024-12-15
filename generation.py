def readfile(file, len):
    with open(file, 'r') as file:
        for line in file:
            yield line[:len]

file = 'gen.txt' 
len = 4 #максимальная длина строки
for line in readfile(file, len):
    print(line)
