import os, time
import shutil

curSessFilCount = 0

#Creates the text file if it doesn't exist
if "fileLocations.txt" not in os.listdir():
    crTxtF = open("fileLocations.txt", 'w')
    crTxtF.close()

    
def getDirFromText(inFile):
    locationList = inFile.readlines()
    #print(locationList)
   # print(len(locationList))
    strippedLst = []
    for loc in locationList:
        if loc.endswith('\n'):
            strippedLst.append(loc.strip('\n'))
        else:
            strippedLst.append(loc)

    #print(strippedLst)
    #print('a')
    return strippedLst


#opens the file
dirList = open("fileLocations.txt", 'r')


#Asks user to input the file locations
print("You do not need the 'C:' when entering the directory. e.g. \\Users\\User\\...")
initialDir = input("Enter the location of the files you want to move: ")
targetDir = input("Enter the target location: ")
targetFileType = input("Enter the type of file you want to move(.txt, .exe, .mp3, etc...): ")

#Checkes if the user changed the directory or not. If so overwrite
masterLst = getDirFromText(dirList)

if initialDir == '':
    initialDir = masterLst[0]
    
if targetDir == '':
    targetDir = masterLst[1]
    
if targetFileType == '':
    targetFileType = masterLst[2]

dirList.close()


dirList = open("fileLocations.txt", 'w')
dirList.write(initialDir + '\n' + targetDir + '\n' + targetFileType)
dirList.close()


#Checks each file in the directory for the file type and moves matches
while True:
    time.sleep(1)
    targetDirectory = os.listdir(initialDir)
    for i in targetDirectory:
        if i.endswith(targetFileType):
            shutil.move(initialDir + '\\' + i, targetDir + '\\' + i)
            curSessFilCount += 1
            print("Successfully moved file count this session: " + str(curSessFilCount))




