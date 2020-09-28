def countwordsfromfile():
    filename = input("Enter the file path")
    numberofwords = 0
    file = open(filename, 'r')
    for line in file:
        words = line.split()
        numberofwords = numberofwords + len(words)
    print(words)
    print(numberofwords)

countwordsfromfile()