"""
file: batch-compact.py
description: Basic wrapper for RapidCompact's CLI to batch-compact multiple 3D
files and prepare them for import into Unreal Engine. This module is the main
script for the wrapper.
language: python3
author: Aidan Grant / kittencurtain
"""

# Imports
import os
import subprocess


# Global variables
os.chdir(os.path.dirname(os.path.abspath(__file__))) # change directory to current file's directory before setting global CWD variable
CWD = os.getcwd()
ALLOWED_FILETYPES = [".gltf", ".glb", ".usdz", ".usd", ".fbx", ".obj", ".stl",
                     ".ply", ".step", ".iges", ".ctm"]


def askUserForFiles():
    """
    Asks the user for the files or folders they would like to process.
    If the user enters nothing, the current list will be returned. Errors will
    be reported if the file or folder entered does not exist on the system.
    """
    # list creation
    internalAssetList = []
    
    while userResponse := input("Please enter a file or folder (leave blank to run) > "):
        fullPath = os.path.join(CWD, userResponse)
        
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
                internalAssetList.append(os.path.join(fullPath,asset))
                print("Added {} to be processed.".format(asset))
    
    #check if the list is empty, run recursively if so
    if not internalAssetList:
        continueResponse = input("There are no files or folders to process. Continue? y/n > ")
        if continueResponse and continueResponse.lower() == "y":
            askUserForFiles()
        else:
            return []
    
    return internalAssetList


def runCommand(cmd):
    """
    Helper function for runCLICompact. Runs a command on the command line, and
    returns the subprocess object.
    """
    completed = subprocess.run(cmd, capture_output=True)
    return completed


def runCLICompact(assetList):
    """
    Primary command for the wrapper. Checks if the asset is a valid type, then
    processes a simple compact command with each file, printing a success or
    failure message. Exports the files to the same location with the same name
    in the .glb format.
    """
    # guard against empty list
    if not assetList:
        print("No files/folders to process. Skipping compacting...")
        return
    else:
        for file in assetList:
            # check if the filetype is supported, skip it and tell the user if not
            fileSplit = os.path.splitext(file)
            if fileSplit[-1] not in ALLOWED_FILETYPES:
                print("File {} is of an unsupported type. Skipping file...".format(file))
                continue
            else:
                returnData = runCommand("rpdx -i " + file + " -c -e " + fileSplit[0] + ".glb")
                if returnData.returncode != 0:
                    print("Error with {filename}: {err}".format(filename=file, err=returnData.stderr))
                else:
                    print("Processed {filename}, continuing...".format(filename=file))
        print("All files processed.")


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
