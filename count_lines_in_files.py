# File objects
import os

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

# - - -

dirName = 'FILE_DIRECTORY_NAME_HERE';
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)

numberoflines = 0


for files in listOfFiles:
    my_file_text = os.path.splitext(files)
    my_file_ext = my_file_text[1]

    if my_file_ext == "SPECIFIC_EXTENSION":
        f = open(files)
        data = f.read()
        numOfLines = len(data.splitlines())
        numberoflines = numberoflines + numOfLines
        print(numberoflines)
        f.close


print(listOfFiles)

