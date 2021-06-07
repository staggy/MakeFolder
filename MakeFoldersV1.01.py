"""
Written by Carl Gager
2021/6/3

Ask for day/month/year that the program should run in

Error handling.

"""
import os
import time
from datetime import date

folderNum = 1
newFolderName = ""


def makeDir(parent_dir, directory):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % (parent_dir + "/" + directory))


def makeSubs(parent_dir, directory):
    subData = ""
    global newFolderName

    # Make New Folder under week.
    subNF = parent_dir + directory  # Set up locations
    directory = newFolder()

    newFolderName = directory

    #path = os.path.join(subData, directory)
    makeDir(subNF, directory)  # New Folder
    # update subNF to WeekFolder
    subNF += "/" + directory
    
    directory = "Documents"
    path = os.path.join(subNF, directory)
    makeDir(subNF, directory)  # Documents

    directory = "Data"
    path = os.path.join(subNF, directory)
    makeDir(subNF, directory)  # Data

    # update subNF to data
    subNF += "/" + directory
    directory = "Excel"
    path = os.path.join(subNF, directory)
    makeDir(subNF, directory)  # Excel
    print()

def newFolder():
    global folderNum
    folderNum = folderNum + 1
    if folderNum <= 1:
        return "New Folder"
    return "New Folder" + str(folderNum - 1)


def main():
    sure = False
    today = str(date.today().strftime('%d-%m-%Y'))
    yearMonth = today[2:len(today)]
    #parent_dir = "C:/Users/Mike Palanza/One Drive-AYAPS/"
    weekDir = ""
    directory = ""

    parent_dir = input("Please enter path E.G. \"C:/Users/Mike Palanza/One Drive-AYAPS/\": ")
    path = os.path.join(parent_dir, directory)
    print(f'{today}')
    print("Folders will be created under: " + parent_dir)
    #startWeek = input("Please enter date of the start of week (1-31): ")
    # startWeek = "1"
    
    
    
    numberFolders = input("Please enter the number of folders: ")
    if int(numberFolders) > 10:
        check = input(f"Are you sure you want to make {numberFolders}?(y or n)")
        if check == "y" or check == "Y" or check == "yes" or check == "YES":
            pass
        else:
            print("Woops try again!")
            time.sleep(2)
            exit()

    # if len(startWeek) <= 1:
    #     startWeek = "0" + startWeek
    # directory = startWeek + yearMonth
    # weekDir = parent_dir + directory
    # 
    # # set path and create directory
    #makeDir(parent_dir, directory)
    
    try:
        makeSubs(parent_dir, directory)
        
        #print(numberFolders)
        # loop numberFolders times
        for i in range(int(numberFolders) - 1):
            makeSubs(parent_dir, "")
            #print(numberFolders)
        print("Done you can close or it will close in 15 seconds.")
        time.sleep(5)
        print("10")
        time.sleep(5)
        print("5")
        time.sleep(4)
        print("1")
    except:
        print("There was an error! Closing . . .")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
main()