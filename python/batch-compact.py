"""
NON-PRODUCTION TEST CODE
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


def getUserInput():
    """
    Wrapped function used to call in askUserForFiles repeatedly
    """    
    userResponse = input("Please enter a file or folder (leave blank to run) > ")
    
    return userResponse


def askUserForFiles():
    """Pseudo:
    1. ask user for input
        1a. each input should be one file, or users can specify a folder to process every file in that folder
    2. validate the input, report error if invalid
    3. if valid, add to list then ask user for next file/folder
    4. if input is empty, finish and return list
    """
    # list creation
    internalAssetList = []
    
    while userResponse := getUserInput():
        fullPath = CWD + "/" + userResponse
        print(fullPath)
        
        # check if response exists, ask again if not
        exists = os.path.exists(fullPath)
        if not exists:
            print("That is not a valid file or folder. Please check your input and make sure it is in the same directory as the program.")
            continue
        
        # check if response is a file, assume folder otherwise
        if os.path.isfile(fullPath):
            internalAssetList.append(fullPath)
            print("Added {} to be processed.".format(userResponse))
        else:
            filesInFolder = os.listdir(fullPath)
            for asset in filesInFolder:
                internalAssetList.append(fullPath + "/" + asset)
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
        #process each file
        pass


def checkForMoreFiles():
    """Pseudo:
    1. check if the user would like to process more files
    2. if the input is not empty, check if it is valid (y/n)
    3. if valid, check if y and return true
    4. otherwise, return false
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
