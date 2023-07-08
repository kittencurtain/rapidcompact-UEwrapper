"""
file: batch-compact.py
description: Basic wrapper for RapidCompact's CLI to batch-compact multiple 3D files and prepare them for import into Unreal Engine. This module is the main script for the wrapper.
language: python3
author: Aidan Grant / kittencurtain
"""

# Imports
import os
import subprocess


# Global variables
CWD = os.getcwd()
ALLOWED_FILETYPES = ["gltf", "glb", "usdz", "usd", "fbx", "obj", "stl", "ply", "step", "iges", "ctm"]


def askUserForFiles():
    """
    Asks the user for the files or folders they would like to process. If the user enters
    nothing, the current list will be returned. Errors will be reported if the file
    or folder entered does not exist on the system.
    """
    # list creation
    internalAssetList = []
    
    while userResponse := input("Please enter a file or folder (leave blank to run) > "):
        fullPath = os.path.join(CWD + "/", userResponse)
        print(fullPath)
        
        # check if response exists, ask again if not
        exists = os.path.exists(fullPath)
        if not exists:
            print("That is not a valid file or folder. Please check your input and make sure it is in the same directory as the program.")
            continue
        
        # check if response is a file, assume folder otherwise
        if os.path.isfile(fullPath):
            internalAssetList.append(userResponse)
            print("Added {} to be processed.".format(userResponse))
        else:
            filesInFolder = os.listdir(fullPath)
            for asset in filesInFolder:
                internalAssetList.append(asset)
                print("Added {} to be processed.".format(asset))
    
    #check if the list is empty, run recursively if so
    if not internalAssetList:
        continueResponse = input("There are no files or folders to process. Continue? > y/n")
        if continueResponse and continueResponse.lower() == "y":
            askUserForFiles()
        else:
            return []
    
    return internalAssetList


def runCLICompact(assetList):
    """Pseudo:
    1. for each item in the asset list,
        1a. check if it is a valid filetype
        1b. create a subdirectory for its output
        1c. compact the asset & export it to the subdirectory
        1d. print debug information for success/failure
    """
    # guard against empty list
    if not assetList:
        print("No files/folders to process. Skipping compacting...")
        return
    else:
        for file in assetList:
            # check if the filetype is supported, skip it and tell the user if not
            fileSplit = file.split(".")
            if fileSplit[-1] not in ALLOWED_FILETYPES:
                print("File {} is of an unsupported type. Skipping file...".format(file))
                continue
            else:
                """create a subdirectory in the working directory with the file name
                if there are two files with the same name but different file types and
                the directories would clash create the directory with a dash and the file
                type instead"""
                try:
                    os.mkdir(os.path.join(CWD + "/", fileSplit[0]))
                except OSError as error:
                    newName = fileSplit[0] + "-" + fileSplit[1]
                    print("Folder {original} could not be created, using {new} instead.".format(original=fileSplit[0], new=newName))
                    os.mkdir(os.path.join(CWD + "/", newName))
                
                # TODO: run CLI compact comand here


def checkForMoreFiles():
    """    
    Checks if the user would like to process more files. The only valid input is
    Y or y - all other inputs will be handled as if the user wants to exit the program.
    """
    userResponse = input("Would you like to process more files? y/n > ")
    if userResponse:
        if userResponse.lower() == "y":
            return True        
    
    return False


def main():
    """Pseudo:
    1. run the CLI batch compact with the files provided by the user
    2. print a success/failure line for each file
    3. check to see if the user would like to process more files
    """
    print('''
    Please input either a single file or a single folder.
    You will be asked for files/folders multiple times.
    Leave the input blank to run the program.
    ''')
    runCLICompact(askUserForFiles())
  
    while checkForMoreFiles():
        runCLICompact(askUserForFiles())
  
    print("Goodnight")


# Execution Below -----------

if __name__ == '__main__':
    main()
